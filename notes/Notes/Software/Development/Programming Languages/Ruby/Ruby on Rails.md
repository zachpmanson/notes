Routes are defined in `config/routes.rb`.

Rails has a generate command similar to Angular.

```bash
rails g model BirdAlias alias:string origin:string description:string bird:references
```

This example generates a new database table and matching model files, and migration.