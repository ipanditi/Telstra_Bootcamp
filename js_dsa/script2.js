class Rectangle {
    constructor(width, height) {
        this._width = width;  // Private variable (by convention)
        this._height = height; // Private variable (by convention)
    }

    // Getter for area
    get area() {
        return this._width * this._height;
    }

    // Setter for width
    set width(value) {
        if (value > 0) {
            this._width = value;
        } else {
            console.log('Width must be positive.');
        }
    }

    // Setter for height
    set height(value) {
        if (value > 0) {
            this._height = value;
        } else {
            console.log('Height must be positive.');
        }
    }
}

// Create an instance of Rectangle
const rect = new Rectangle(10, 5);

// Access the area using the getter
console.log(`Area: ${rect.area}`); // Output: Area: 50

// Modify dimensions using setters
rect.width = 20;
rect.height = 10;

console.log(`New Area: ${rect.area}`); // Output: New Area: 200

// Try to set invalid dimensions
rect.width = -5; // Output: Width must be positive.
rect.height = -10; // Output: Height must be positive.
