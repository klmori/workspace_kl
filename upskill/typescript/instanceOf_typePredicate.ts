// 📘 TypeScript: `instanceof` and Type Predicate - Full Guide

// -------------------------------------
// 🧱 What is `instanceof`?
// -------------------------------------
// `instanceof` checks if an object was created by a specific class or constructor function.

class Car {
  drive() {
    console.log("Driving a car");
  }
}

class Bike {
  ride() {
    console.log("Riding a bike");
  }
}

function move(vehicle: Car | Bike) {
  if (vehicle instanceof Car) {
    vehicle.drive(); // ✅ narrowed to Car
  } else {
    vehicle.ride();  // ✅ narrowed to Bike
  }
}

const myCar = new Car();
move(myCar); // Output: Driving a car

// -------------------------------------
// 🔍 When to Use `instanceof`
// -------------------------------------
// - Use when checking if an object is an instance of a **class**
// - Doesn't work on plain object types or interfaces

// -------------------------------------
// 🧠 What is a Type Predicate?
// -------------------------------------
// A function that **tells the compiler** something is a specific type.
// Syntax: `function isX(arg): arg is X`

type Dog = { kind: "dog"; bark(): void };
type Cat = { kind: "cat"; meow(): void };

function isDog(pet: Dog | Cat): pet is Dog {
  return pet.kind === "dog"; // custom check
}

function makePetSound(pet: Dog | Cat) {
  if (isDog(pet)) {
    pet.bark(); // ✅ pet is Dog
  } else {
    pet.meow(); // ✅ pet is Cat
  }
}

// -------------------------------------
// ✅ Benefits of Type Predicate
// -------------------------------------
// - Can be reused across functions
// - Works on interfaces, object types, and unions

// -------------------------------------
// 🧩 Example: Array Type Predicate
// -------------------------------------

function isStringArray(val: any): val is string[] {
  return Array.isArray(val) && val.every(item => typeof item === "string");
}

function logInput(input: string | string[]) {
  if (isStringArray(input)) {
    input.forEach(str => console.log("List item:", str));
  } else {
    console.log("Single string:", input);
  }
}

// -------------------------------------
// 🔁 instance of vs Type Predicate
// -------------------------------------
/*
| Feature               | `instanceof`         | Type Predicate             |
|------------------------|----------------------|----------------------------|
| Use with classes       | ✅ Yes              | ✅ Yes                     |
| Use with interfaces    | ❌ No               | ✅ Yes                     |
| Use with unions        | ❌ Limited          | ✅ Ideal                   |
| Custom logic           | ❌ No               | ✅ Yes                     |
| Reusable check         | ❌ Not reusable     | ✅ Yes (as function)       |
*/

// -------------------------------------
// ✅ Combined Example
// -------------------------------------

class Admin {
  constructor(public role: string) {}
}

class Guest {
  constructor(public nickname: string) {}
}

type User = Admin | Guest;

function isAdmin(user: User): user is Admin {
  return user instanceof Admin;
}

function greetUser(user: User) {
  if (isAdmin(user)) {
    console.log("Welcome, admin:", user.role);
  } else {
    console.log("Hello guest:", user.nickname);
  }
}

// -------------------------------------
// 🧠 Summary
// -------------------------------------
/*
- Use `instanceof` when dealing with **class instances**
- Use **type predicates** when working with:
  - Union types
  - Interfaces
  - Custom logic
  - Reusable checks
*/

