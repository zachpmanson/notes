---
date: 2024-06-03
tags:
  - posts
  - venting
  - dirty-hacks
---
RTK Query with [[React]] is pretty great! The primary pattern you find yourself using with it is: 

1. writing a small API definition that provides 
	1.  the endpoint url 
	2. type definitions for request args and response schema
	3. (usually) simply logic for converting passed argument type into request params/body
	4. (usually) simple logic for converting response payload into the response schema
2. importing a hook that RTK Query automatically generates for you
3. reuse the same hook across multiple components

 RTK Query handles loading states, stale while revalidate states, error states, type safety, and caching.

When writing React components, the caching is the most impactful of these.   You can just call the same hook in many different components, and as long as the params are the same the same it will only be a single network request. This removes the need for many invocations `useState` and Redux state calls, since you can just feign a call to the backend every time you need that data.

There is a little boilerplate you have to write, but the meat of a basic RTK Query definition will look something like this:

```ts
    getLocation: build.query<Location, { id: number }>({
      query: ({ ids }) => ({
        url: "api/v1/location",
        params: { id },
      }),
      transformResponse: (response: any) => response.data,
    }),
```

This will generate a hook called `useGetLocation` which will be cached.  Suddenly you never need to store a `Location` object in state to share it across components and you can just call `useGetLocation({id:5})` every time you need it. It also provides a lazy version of the hook that returns a normal function you can use to retrieve the data, which is good for APIs that need to be called multiple times.

```jsx
function LocationCard({id}: {id:number}) {
	const {data: location, isLoading} = useGetLocation({id:id});
	const [getLocationsLazy] = useLazyGetLocation();
	...
	return (
		<div>
			{location.address}
		</div>
	);
}
```

For straightforward GET requests this pattern stellar.  RTK Query encourages you to put all the API definitions into a single file (`src/api/api.ts`), or into a small number files with particular scopes.  For small-medium applications this works well, if you know the URL of an endpoint you want to hit you can just search within the `api.ts` file, use the accompanying hook and you are good to go, type safety and all.  I'm sure this single file approach would breakdown for big applications but its very pleasant at smaller scales.

RTK Query also lets you do POST/PUT/PATCH requests with a similar definition style. Instead of using `build.query`, you use `build.mutation`.

```ts
    addLocation: build.mutation<
      { location_id: number; site_id: number; address: string; abn: string; user_id: number },
      NewLocation
    >({
      query: (body) => ({
        url: "api/v1/location",
        method: "POST",
        body: body,
      }),
    }),
	patchLocation: build.mutation<void, { id: number; data: Partial<Location> }>({
      query: ({ id, data }) => {
        return {
          method: "PATCH",
          url: `api/v1/location/${primaryKey}`,
          body: data,
        };
      },
      transformResponse: (response: any) => response.data,
    }),
```

The hooks generated here will return a function that can be used to send requests.

```jsx
function LocationCard({id}: {id:number}) {
	const {data: location, isLoading} = useGetLocationQuery({id:id})
	const [patchLocation, isPatchLoading] = usePatchLocationMutation()

	function onUpdate(locationUpdate:Partial<Location>) {
		patchLocation(locationUpdate)
	}
	...
	return (
		<div>
			{location.address}
			...
			{/* some input that calls onUpdate on change */}
		</div>
	)
}
```

But wait! If I patch a location, how will the useGetLocation hook know that it's cache is invalid?

## Cache Invalidation

RTK Query uses a tag system for cache invalidation, where a tag represents a kind of query.  Queries can assign themselves tags, and mutations can provide a list of tags they will invalidate. 

These can be static

```ts
    getLocation: build.query<Location, { id: number }>({
      query: ({ ids }) => ({
        url: "api/v1/location",
        params: { id },
      }),
      transformResponse: (response: any) => response.data,
	  providesTags: ['Location'],
    }),
```

or dynamic, based on the params given

```ts
    getLocation: build.query<Location, { id: number }>({
      query: ({ ids }) => ({
        url: "api/v1/location",
        params: { id },
      }),
      transformResponse: (response: any) => response.data,
	  providesTags: (result, error, arg) => [{type:"Location", id: id}]
    }),
```

And similarly for mutations

```ts
	patchLocation: build.mutation<void, { id: number; data: Partial<Location> }>({
      query: ({ id, data }) => {
        return {
          method: "PATCH",
          url: `api/v1/location/${primaryKey}`,
          body: data,
        };
      },
      transformResponse: (response: any) => response.data,
      invalidatesTags: (result, error, arg) => [{ type: 'Location', id: arg.id }] // or just ["Location"] to invalidate the whole category
    }),
```

Where you can, dynamic tags are generally better since you have much more granular control.  Again, this works pretty well for straightforward queries.

## Pagination

RTK Query doesn't include a mechanism for paging data, but passing a page number as a param works fine if you have discrete pages.

```ts
    getLocations: build.query<Location, { page: number }>({
      query: ({ page }) => ({
        url: "api/v1/locations",
        params: { page }
      }),
      transformResponse: (response: any) => response.data,
	  providesTags: (result, error, arg) => [...result.map(location => {type:"Location", id: location.id}), {type:"Location", id: "LIST"}],
	}),
```

## But what about infinite scroll?

When infinitely scrolling, normally you'd have an array that stores all the results that have been loaded so far, and then you'd append new results to the end of this list when they are loaded in (maybe even dropping some entries from the start if you are memory constrained).  The hook generated by the previous example will only ever let you access one page's entries at a time. 

RTK Query doesn't have any special functions for infinite scrolling, but the pieces it gives you are enough to make it work. When writing a query definition you can explicitly set which params contribute are used to define unique cache entries, and another function to say how old cache entries should be overwritten by new ones.

```ts
    getLocations: build.query<Location, { page: number }>({
      query: () => ({
        url: "api/v1/locations",
        params: { page }
        
      }),
      transformResponse: (response: any) => response.data,
	  providesTags: (result, error, arg) => [...result.map(location => {type:"Location", id: location.id}), {type:"Location", id: "LIST"}],
	  
	  // overwrite cached value when page value changes, treat page
	  serializeQueryArgs: ({ queryArgs }) => ({ ...queryArgs, page: undefined }),
	  
	  // when overwriting cache value, append new data to old list
	  merge: (currentCache, newData, otherArgs) => {
          currentCache.items.push(...newData);
      },
	}),
```

This works riiiiight until you need to invalidate the cache. Say you have a page with infinite scroll via pressing a load more button at the bottom, and the user has pressed it 3 times. At this stage, the hook will look like `const {data} = useGetLocationsQuery({page: 4});`. If page size is 20, data, will contain 80 entries. Then you edit an entry that appears on page 3. Or you add a new location.  Both of these operation will invalidate the cache, but the merge strategy provided will simply add the new cache to the end of the previous cache, so  `const {data} = useGetLocationsQuery({page: 4});` will now have 100 entries, 80 from the original 4 pages and 20 from the 4th page repeated again.  **Ideally the merge function would have a way of distinguishing cache updates that are due to tag invalidation from cache updates due to parameter changes, but there is currently no way to do this**.

## Workarounds

There are a [number](https://github.com/reduxjs/redux-toolkit/discussions/1163) [of](https://github.com/reduxjs/redux-toolkit/issues/3733) [discussion](https://github.com/reduxjs/redux-toolkit/discussions/3174) of how to mitigate this.  The solution I went with looks like this.

Firstly, the response payload must include the page number metadata.  This is usually the case with paginated endpoints, but this data now needs to be included in the cached result in the query definition.

When merging the cache, only append the new data if the new data page number is greater than the old value:

```ts
type PaginatedData<ItemType> = {
  page: number;
  pages: number;
  per_page: number;
  total: number;
  items: ItemType[];
};
...

    getLocations: build.query<PaginatedData<Location>, { page: number }>({
      query: () => ({
        url: "api/v1/locations",
        params: { page }
        
      }),
      transformResponse: (response: any) => response.data,
	  providesTags: (result, error, arg) => [...result.map(location => {type:"Location", id: location.id}), {type:"Location", id: "LIST"}],
	  
	  // overwrite cached value when page value changes, treat page
	  serializeQueryArgs: ({ queryArgs }) => ({ ...queryArgs, page: undefined }),
	  
	  // when overwriting cache value, append new data to old list if page value increases
	  merge: (currentCache, newData, otherArgs) => {
	    if (newData.page > currentCache.page) {
          currentCache.items.push(...newData.items);
          currentCache = { ...newData, items: currentCache.items };
        } else {
          return newData;
        }
      },
	}),
```

Then in the component where the hook is called, ensure that the page number is reset to 1 whenever a mutation occurs that will invalidate the `useGetLocationsQuery` data.  Since this page isn't an increase from the previous, the old cache will be discarded. This can be annoying since the component that triggers the mutation and invalidates the data may be completely seperate from the component that queries for the data.  

```tsx
function EditLocationAddress({id}: {id:number}) {
	const [patchLocation, isPatchLoading] = usePatchLocationMutation();

	function onUpdate(locationUpdate:Partial<Location>) {
		patchLocation(locationUpdate);
		// TODO somehow reset the page number to 0 in all relevant places
	}
	...
	return (
		<div>
			{/* some input that calls onUpdate on change */}
		</div>
	);
}
```

There is probably a clever way of doing this where the cached page number is used as the canonical page number across all components, and then you could force a reset back to one from any component, but I haven't needed to implement this just yet in any applications.

Maybe something like this? I haven't tried it yet.

```jsx
function EditLocationAddress({id}: {id:number}) {
	const [patchLocation, isPatchLoading] = usePatchLocationMutation();
	const [getLocationsLazy] = useLazyGetLocationsQuery();

	function onUpdate(locationUpdate:Partial<Location>) {
		patchLocation(locationUpdate);
		getLocationsLazy(
			{ page: 1 },
			true // lazy queries ignore cache by default, true overrides this
		);
	}
	...
	return (
		<div>
			{/* some input that calls onUpdate on change */}
		</div>
	);
}
```