---
tags:
  - javascript
---
To send define a mutation in RTK Query that uses form data rather than a JSON payload, you need to use the **undocumented** `formData` attribute.  This is useful for sending files to endpoints.

```ts
    uploadSiteDocuments: build.mutation<{ file: string; uri: string }[], { files: File[] }>({
      query: (body) => {
        let formData = new FormData();
        body.files.forEach((file) => {
          formData.append(file.name, file);
        });

        return {
          url: "site/documents",
          method: "POST",
          body: formData,
          formData: true,
        };
      },
      transformResponse: (response: any) => response.data,
    }),

```

Do not change the encoding header as this is done automatically.