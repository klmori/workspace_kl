// 📘 TypeScript Abstract Classes - Full Guide

// -------------------------------------
// 🧠 What is an Abstract Class?
// -------------------------------------
// - An abstract class cannot be instantiated directly.
// - It can include abstract methods (no implementation) and regular methods (with implementation).
// - Used as a **blueprint** for other classes.

abstract class Animal {
  abstract makeSound(): void; // abstract method (must be implemented by subclasses)

  move(): void {
    console.log("Animal is moving");
  }
}

// -------------------------------------
// ✅ Concrete Subclass (extends abstract)
// -------------------------------------
class Dog extends Animal {
  makeSound(): void {
    console.log("Woof!");
  }
}

const myDog = new Dog();
myDog.makeSound(); // Woof!
myDog.move();      // Animal is moving

// -------------------------------------
// ❌ Error: Cannot create instance of abstract class
// const someAnimal = new Animal(); // ❌ Compilation Error

// -------------------------------------
// 📦 Abstract Class with Properties
// -------------------------------------
abstract class Vehicle {
  constructor(public brand: string) {}

  abstract drive(): void;

  honk(): void {
    console.log(`${this.brand} says: Beep beep!`);
  }
}

class Car extends Vehicle {
  drive(): void {
    console.log(`${this.brand} is driving.`);
  }
}

const c = new Car("Toyota");
c.drive(); // Toyota is driving.
c.honk();  // Toyota says: Beep beep!

// -------------------------------------
// 🧱 Abstract Class with Getters/Setters
// -------------------------------------
abstract class Shape {
  abstract get area(): number;
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }

  get area(): number {
    return Math.PI * this.radius * this.radius;
  }
}

const circle = new Circle(10);
console.log(circle.area); // 314.159...

// -------------------------------------
// 🔄 Abstract Class as Interface
// -------------------------------------
abstract class Logger {
  abstract log(message: string): void;
}

class ConsoleLogger extends Logger {
  log(message: string): void {
    console.log(`[Log]: ${message}`);
  }
}

const logger = new ConsoleLogger();
logger.log("Hello from logger!"); // [Log]: Hello from logger!

// -------------------------------------
// ✅ Summary Table
// -------------------------------------
/*
| Feature               | Support in Abstract Class |
|------------------------|--------------------------|
| Constructors           | ✅ Yes                    |
| Concrete Methods       | ✅ Yes                    |
| Abstract Methods       | ✅ Yes (must override)    |
| Properties             | ✅ Yes                    |
| Inheritance            | ✅ Yes                    |
| Instantiation Allowed? | ❌ No                     |
*/

