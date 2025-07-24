// 📘 TypeScript: `type` vs `interface` - Full Guide

// -------------------------------------
// ✅ Basic Usage
// -------------------------------------

// Using type
type UserType = {
  name: string;
  age: number;
};

// Using interface
interface UserInterface {
  name: string;
  age: number;
}

// Both are functionally similar here
const user1: UserType = { name: "Alice", age: 25 };
const user2: UserInterface = { name: "Bob", age: 30 };

// -------------------------------------
// 🔁 Extension / Inheritance
// -------------------------------------

// Interface extends interface
interface Animal {
  name: string;
}
interface Dog extends Animal {
  breed: string;
}

// Type extends type (using intersection)
type Vehicle = {
  wheels: number;
};
type Car = Vehicle & {
  brand: string;
};

// -------------------------------------
// 📦 Adding Properties Later (Declaration Merging)
// -------------------------------------

interface Book {
  title: string;
}
interface Book {
  author: string;
}

const b: Book = {
  title: "1984",
  author: "George Orwell"
};

// type does NOT support declaration merging
type Movie = {
  title: string;
};
// type Movie = { director: string }; ❌ Error: Duplicate identifier

// -------------------------------------
// 🧠 With Functions
// -------------------------------------

type GreetType = (name: string) => string;

interface GreetInterface {
  (name: string): string;
}

const greet1: GreetType = (name) => `Hello ${name}`;
const greet2: GreetInterface = (name) => `Hi ${name}`;

// -------------------------------------
// 🛠️ With Classes
// -------------------------------------

interface Shape {
  getArea(): number;
}

class Circle implements Shape {
  constructor(public radius: number) {}
  getArea(): number {
    return Math.PI * this.radius * this.radius;
  }
}

// type can also be used with classes
type Logger = {
  log(message: string): void;
};

class ConsoleLogger implements Logger {
  log(message: string) {
    console.log(message);
  }
}

// -------------------------------------
// 🧩 Complex Types & Utility Types
// -------------------------------------

// Only type can do unions, intersections, tuples, mapped types

type Status = "success" | "failure"; // ✅ Union
type Point = [number, number];       // ✅ Tuple
type ReadonlyUser = Readonly<UserType>; // ✅ Mapped utility

// interface Status = "success" | "failure"; ❌ Not allowed
// interface Point = [number, number]; ❌ Not allowed

// -------------------------------------
// ✅ Summary: `type` vs `interface`
// -------------------------------------
/*
| Feature                    | interface     | type            |
|----------------------------|---------------|------------------|
| Object shape               | ✅ Yes        | ✅ Yes           |
| Function type              | ✅ Yes        | ✅ Yes           |
| Extending                 | ✅ extends    | ✅ & (intersection) |
| Declaration merging        | ✅ Yes        | ❌ No            |
| Tuples, unions, primitives | ❌ No         | ✅ Yes           |
| Recommended for objects    | ✅ Yes        | ✅ Yes           |
*/

// -------------------------------------
// 🚀 Best Practice
// -------------------------------------
/*
- Use `interface` when designing **object structures** or **class contracts**
- Use `type` when:
  - You need **union, intersection, tuple**, or **primitive aliases**
  - You want advanced type composition
*/
