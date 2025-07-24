// 📘 TypeScript Access Modifiers - Full Guide

// -------------------------------------
// ✅ public (default)
// -------------------------------------
// - Accessible from anywhere (inside class, subclass, outside)

class Person {
  public name: string; // optional: 'public' is the default

  constructor(name: string) {
    this.name = name;
  }

  public greet(): void {
    console.log(`Hello, I’m ${this.name}`);
  }
}

const p1 = new Person("Alice");
console.log(p1.name); // ✅ Accessible
p1.greet();           // ✅ Accessible

// -------------------------------------
// 🔐 private
// -------------------------------------
// - Accessible **only inside the class**
// - ❌ Not accessible in subclasses or outside

class BankAccount {
  private balance: number;

  constructor(initialAmount: number) {
    this.balance = initialAmount;
  }

  public deposit(amount: number) {
    this.balance += amount;
  }

  public getBalance(): number {
    return this.balance;
  }
}

const acc = new BankAccount(1000);
acc.deposit(500);
console.log(acc.getBalance()); // ✅ OK
// console.log(acc.balance);   // ❌ Error: 'balance' is private

// -------------------------------------
// 🛡️ protected
// -------------------------------------
// - Accessible inside the class and subclasses
// - ❌ Not accessible from outside the class hierarchy

class Employee {
  protected salary: number;

  constructor(salary: number) {
    this.salary = salary;
  }
}

class Manager extends Employee {
  showSalary(): void {
    console.log(`Salary is ${this.salary}`); // ✅ Allowed (subclass)
  }
}

const mgr = new Manager(80000);
mgr.showSalary();           // ✅ OK
// console.log(mgr.salary); // ❌ Error: 'salary' is protected

// -------------------------------------
// 🧠 Modifier Rules Summary
// -------------------------------------
/*
| Modifier   | Inside Class | Subclass | Outside Class |
|------------|--------------|----------|----------------|
| public     | ✅ Yes       | ✅ Yes   | ✅ Yes         |
| private    | ✅ Yes       | ❌ No    | ❌ No          |
| protected  | ✅ Yes       | ✅ Yes   | ❌ No          |
*/

// -------------------------------------
// ✅ Combined Example
// -------------------------------------
class User {
  public username: string;
  private password: string;
  protected email: string;

  constructor(username: string, password: string, email: string) {
    this.username = username;
    this.password = password;
    this.email = email;
  }

  public login(pass: string): boolean {
    return this.password === pass;
  }
}

class Admin extends User {
  resetEmail(newEmail: string): void {
    this.email = newEmail; // ✅ OK
    // this.password = "123"; // ❌ Error: password is private
  }
}

const u = new User("john_doe", "pass123", "john@example.com");
console.log(u.username);      // ✅ public
console.log(u.login("pass123")); // ✅ method works
// console.log(u.password);   // ❌ Error: private
// console.log(u.email);      // ❌ Error: protected

