Examples of all styles for CSS debugging.

This is *some text* with **formatting** applied to it with Markdown.  ***This has even more formatting applied to it.***

To split text  
over multiples lines put  
two spaces at the end.

>This is a quote

-- Zach Manson

>Citation for this quote is a hyperlink

-- [Zach Manson](https://zachmanson.com)

---

# Heading

## Subheading

### Subsubheading

---

Backlink: [[Projects]]

[[Projects|Aliased backlink]]

[[Ochrs#ochrs-deploy|Backlink with anchor]]

[External link](https://suricrasia.online/unfiction/basilisk/)

This has `some inline` code text.

```
This is an untyped codeblock
```

```ts
let codeblock: TypeScript = "this should have code highlighting"
```

---

Ordered list:

1. First item
2. Second
3. ...
4. ...

Unordered list:

- unordered list
- ...
- ...

Ordered list with codeblock:

1. List with codeblock
2. Grant the user account access to the database with the SQL command. 

    ```sql
    GRANT ALL PRIVILEGES ON DATABASE "my_db" to my_user;
    ```

3. Modify `/etc/postgresql/14/main/pg_hba.conf` (or equivalent). Set the `ADDRESS` field for IPv4 connections to this:

Unordered list with line breaks:

- **[zachmanson.com](https://zachmanson.com)**  
  main home page and blog  
  gh pages
	- **[notes.zachmanson.com](https://notes.zachmanson.com)**  
	  this site  
	  gh pages
	- **[tracker.zachmanson.com](https://tracker.zachmanson.com)**  
	  likely defunct [[COVID-19 Tracker]] for WA  
	  trackstar

---

Run-time Ochrs variables:

Last build time: <ochrs:build-time>

List of Ochrs variables: <ochrs:ochrs-vars>

More explanation of these can be found on [[Ochrs Syntax]].

---

Backlink image:

![[ADM3A.png]]


External image:

![gh display pic](https://avatars.githubusercontent.com/u/24368336)