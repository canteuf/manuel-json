export type JsonPrimitive = string | number | boolean | null;
export type JsonObject = { [cle: string]: JsonValue };
export type JsonArray = JsonValue[];
export type JsonValue = JsonPrimitive | JsonObject | JsonArray;

// Le compilateur refuse ce qui n'est pas du JSON
const ok: JsonValue = { nom: "Ada", roles: ["admin"], actif: true, titre: null };
// const ko: JsonValue = { creeLe: new Date() }; // erreur : Date n'est pas JSON

console.log(JSON.stringify(ok));
