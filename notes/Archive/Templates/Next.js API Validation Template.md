Next.js doesn't have a clean validation piping pattern or method checking so this will have to do.

```ts
import type { NextApiRequest, NextApiResponse } from "next";
import { z } from "zod";

const schema = z.object({
  product_code: z.string(),
  blacklisted: z.boolean(),
});
type Schema = z.infer<typeof schema>;

export default async function handler(req: NextApiRequest, res: NextApiResponse<{ error: string | z.ZodError<any> }>) {
  switch (req.method) {
    case "POST":
      const response = schema.safeParse(req.body);
      if (!response.success) {
        return res.status(400).json({
          error: response.error,
        });
      }
      const body = req.body as Schema;
      //do things
      break;
    default:
      return res.status(405).json({ error: "Invalid method" });
  }
}
```