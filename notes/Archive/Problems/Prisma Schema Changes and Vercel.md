---
tags:
  - nextjs
  - prisma
---
When you change a schema using Prisma, Vercel won't automatically regenerate the Prisma client until you add a `postinstall` command to `package.json`.

```json
"scripts": {
	"dev": "next dev",
	"build": "next build",
	"start": "next start",
	"lint": "next lint",
	"generate": "prisma generate", // add these two
	"postinstall": "npm run generate"
},
```

Solution found [here](https://github.com/prisma/prisma/issues/5175).
