// 📘 TypeScript Generics - Full Guide

// -------------------------------------
// 🔧 Why Use Generics?
// -------------------------------------
// Without Generics
function identityAny(arg: any): any {
  return arg;
}

// With Generics
function identity<T>(arg: T): T {
  return arg;
}

identity<string>("hello"); // returns "hello"
identity<number>(123);     // returns 123

// -------------------------------------
// 🧠 Basic Syntax
// -------------------------------------
function identityBasic<T>(arg: T): T {
  return arg;
}

// -------------------------------------
// 💼 Use Case in Functions
// -------------------------------------
function getFirst<T>(arr: T[]): T {
  return arr[0];
}

getFirst<number>([1, 2, 3]); // returns 1
getFirst(["a", "b", "c"]);   // returns "a"

// -------------------------------------
// 📦 Generic Interfaces
// -------------------------------------
interface Box<T> {
  contents: T;
}

const stringBox: Box<string> = { contents: "books" };
const numberBox: Box<number> = { contents: 42 };

// -------------------------------------
// 🧱 Generic Classes
// -------------------------------------
class Container<T> {
  value: T;
  constructor(val: T) {
    this.value = val;
  }
}

const c1 = new Container<number>(10);
const c2 = new Container<string>("data");

// -------------------------------------
// 🎯 Generic Constraints
// -------------------------------------
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

getLength("hello");        // ✅ OK
getLength([1, 2, 3]);       // ✅ OK
// getLength(100);          // ❌ Error: number has no length

// -------------------------------------
// 🔁 Multiple Type Parameters
// -------------------------------------
function pair<K, V>(key: K, value: V): [K, V] {
  return [key, value];
}

const p = pair("id", 123); // ["id", 123]

// -------------------------------------
// ⛓️ Generic with Default Type
// -------------------------------------
function wrap<T = string>(x: T): T[] {
  return [x];
}

wrap(10);         // [10]
// wrap();        // ❌ Error: Argument required

// -------------------------------------
// ✅ Summary Table
// -------------------------------------
/*
| Concept          | Syntax / Example                          |
|------------------|--------------------------------------------|
| Generic Function | function identity<T>(arg: T): T            |
| Generic Class    | class Box<T> { value: T }                  |
| Constraints      | T extends SomeType                         |
| Multiple Params  | function pair<K, V>(k: K, v: V): [K, V]    |
*/

// Generics Classes
