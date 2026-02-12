I hate `__init__.py`. It has an awful name, it encourages duplicating exports, circular imports, its difficult to type, hard to search for. I know it is required(ish) for [[Python]] module resolution, so create it in every file. But leave it completely empty.

The only case where I support re-exporting from this file is if you are creating a library.