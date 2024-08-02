// Define a base class
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

// Define a derived class
class Dog extends Animal {
    constructor(name, breed) {
        super(name); // Call the constructor of the base class
        this.breed = breed;
    }

    // Override the method from the base class
    speak() {
        console.log(`${this.name} barks.`);
    }

    // New method
    displayBreed() {
        console.log(`Breed: ${this.breed}`);
    }
}

// Create an instance of the derived class
const dog = new Dog('Rex', 'German Shepherd');

// Call methods on the instance
dog.speak(); // Output: Rex barks.
dog.displayBreed(); // Output: Breed: German Shepherd
