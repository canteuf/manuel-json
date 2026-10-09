import { z } from "zod";

const Produit = z.object({
  sku: z.string().regex(/^[A-Z]{3}-[0-9]{4}$/),
  prix: z.number().positive(),
});

// Zod 4 produit directement le JSON Schema correspondant
console.log(JSON.stringify(z.toJSONSchema(Produit), null, 2));
