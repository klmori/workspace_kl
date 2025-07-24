// 📘 TypeScript: Discriminated Unions + Exhaustiveness Checking

// -------------------------------------
// 🧠 What is a Discriminated Union?
// -------------------------------------
// A union of object types that **share a common literal property**
// (usually `kind`, `type`, `tag`, etc.)

type Circle = {
  kind: "circle";
  radius: number;
};

type Square = {
  kind: "square";
  side: number;
};

type Rectangle = {
  kind: "rectangle";
  width: number;
  height: number;
};

// The discriminated union
type Shape = Circle | Square | Rectangle;

// -------------------------------------
// 📦 Example with switch-case
// -------------------------------------

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side * shape.side;
    case "rectangle":
      return shape.width * shape.height;
  }
}

// -------------------------------------
// 🔐 Why Use Discriminated Unions?
// -------------------------------------
/*
- Safe type narrowing using `.kind`
- Helps avoid unsafe object access
- Great for union of structured types
*/

// -------------------------------------
// 🛡️ Exhaustiveness Checking
// -------------------------------------
// Ensures that all cases are handled. If a new type is added to the union,
// TypeScript will warn us if it's not covered.

function getAreaSafe(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.side * shape.side;
    case "rectangle":
      return shape.width * shape.height;
    default:
      // ⛔ This should never happen — helps with future-proofing
      const _exhaustiveCheck: never = shape;
      throw new Error(`Unhandled shape: ${JSON.stringify(shape)}`);
  }
}

// -------------------------------------
// ❗ If we forget to handle a type, TypeScript catches it:
// Add this type for testing
/*
type Triangle = { kind: "triangle"; base: number; height: number };
type Shape = Circle | Square | Rectangle | Triangle;

TypeScript will give error:
  Type 'Triangle' is not assignable to type 'never'
*/

// -------------------------------------
// ✅ Best Practice: Always use `default` + `never`
// -------------------------------------
/*
- Acts as a safety net
- Prevents silent failures when union types grow
- Helps during refactoring
*/

// -------------------------------------
// 🔁 Real-world Example: Form Field Discriminated Union
// -------------------------------------

type TextField = {
  kind: "text";
  label: string;
  value: string;
};

type CheckboxField = {
  kind: "checkbox";
  label: string;
  checked: boolean;
};

type NumberField = {
  kind: "number";
  label: string;
  value: number;
};

type FormField = TextField | CheckboxField | NumberField;

function renderField(field: FormField) {
  switch (field.kind) {
    case "text":
      console.log("Text Field:", field.label, field.value);
      break;
    case "checkbox":
      console.log("Checkbox:", field.label, field.checked ? "✓" : "✗");
      break;
    case "number":
      console.log("Number Field:", field.label, field.value);
      break;
    default:
      const _never: never = field;
      throw new Error(`Unhandled field type: ${JSON.stringify(field)}`);
  }
}

// -------------------------------------
// ✅ Summary
// -------------------------------------
/*
| Feature                  | Description                               |
|--------------------------|-------------------------------------------|
| Discriminated Union      | Union of types with common literal key    |
| Key Benefit              | Safe narrowing using `switch` or `if`     |
| Exhaustiveness Checking  | Catches missing cases using `never`       |
| Common Discriminator     | Use `kind`, `type`, or `tag` as string key|
| Real-world Use Cases     | Form fields, API responses, UI events     |
*/

