class Vehicle {
    start() {
        console.log('Vehicle is starting.');
    }
}

class Car extends Vehicle {
    start() {
        console.log('Car is starting with a roar.');
    }
}

class Bike extends Vehicle {
    start() {
        console.log('Bike is starting with a hum.');
    }
}

// Create instances of derived classes
const car = new Car();
const bike = new Bike();

// Call the start method on different instances
car.start(); // Output: Car is starting with a roar.
bike.start(); // Output: Bike is starting with a hum.
