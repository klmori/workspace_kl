// 📘 TypeScript Type Narrowing - Full Guide

// -------------------------------------
// 🧠 What is Type Narrowing?
// -------------------------------------
// Narrowing is when TypeScript reduces a broader type (like `string | number`) to a more specific one 
// using checks (typeof, instanceof, etc.)

function printId(id: number | string) {
  if (typeof id === "string") {
    console.log(id.toUpperCase()); // ✅ narrowed to string
  } else {
    console.log(id.toFixed(2));    // ✅ narrowed to number
  }
}

// -------------------------------------
// 🔍 typeof Narrowing
// -------------------------------------

function doSomething(x: string | number | boolean) {
  if (typeof x === "string") {
    console.log("String:", x.toLowerCase());
  } else if (typeof x === "number") {
    console.log("Number:", x.toFixed(1));
  } else {
    console.log("Boolean:", x ? "true" : "false");
  }
}

// -------------------------------------
// 🧱 instanceof Narrowing
// -------------------------------------

class Dog {
  bark() {
    console.log("Woof");
  }
}

class Cat {
  meow() {
    console.log("Meow");
  }
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark(); // ✅ narrowed to Dog
  } else {
    animal.meow(); // ✅ narrowed to Cat
  }
}

// -------------------------------------
// 🔒 Equality Narrowing
// -------------------------------------

function compare(x: string | number, y: string | boolean) {
  if (x === y) {
    // x and y are both string
    console.log(x.toUpperCase());
  } else {
    console.log("Not equal");
  }
}

// -------------------------------------
// ❓ in Operator Narrowing
// -------------------------------------

type A = { kind: "a"; aProp: number };
type B = { kind: "b"; bProp: string };

function handle(x: A | B) {
  if ("aProp" in x) {
    console.log("A's property:", x.aProp);
  } else {
    console.log("B's property:", x.bProp);
  }
}

// -------------------------------------
// 📦 Discriminated Union Narrowing
// -------------------------------------

type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; side: number };

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side * shape.side;
  }
}

// -------------------------------------
// 🧩 Type Predicate Narrowing
// -------------------------------------

function isString(x: any): x is string {
  return typeof x === "string";
}

function logValue(val: string | number) {
  if (isString(val)) {
    console.log(val.toUpperCase()); // ✅ narrowed to string
  } else {
    console.log(val.toFixed(2));    // ✅ narrowed to number
  }
}

// -------------------------------------
// 🔄 Narrowing with Array.isArray
// -------------------------------------

function logItems(items: string[] | string) {
  if (Array.isArray(items)) {
    items.forEach(i => console.log(i));
  } else {
    console.log(items);
  }
}

// -------------------------------------
// 🧠 Summary of Narrowing Techniques
// -------------------------------------
/*
| Technique            | Example Keyword     | Use Case                        |
|----------------------|----------------------|---------------------------------|
| typeof               | typeof x === "..."   | Primitives (string, number, etc)|
| instanceof           | x instanceof Class   | Class instances                 |
| in                  | "prop" in obj        | Object type discrimination      |
| Equality             | x === y              | Type refinement on value check  |
| Discriminated Union  | switch on .kind      | Tagged union types              |
| Type Predicates      | x is SomeType        | Custom narrowing logic          |
| Array Check          | Array.isArray(x)     | Arrays vs single value          |
*/

// -------------------------------------
// 🚀 Best Practice
// -------------------------------------
/*
- Use `typeof` for primitives
- Use `instanceof` for class instances
- Use `in` or discriminated union for objects
- Write type predicates for reusable checks
*/

