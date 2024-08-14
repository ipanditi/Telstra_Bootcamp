// Shape class

class Shape {

  constructor() {

    this.id = null;

    this.type = null;

  }
 
  getType() {

    return this.type;

  }
 
  getId() {

    return this.id;

  }
 
  setId(id) {

    this.id = id;

  }
 
  clone() {

    throw new Error("This method should be overridden!");

  }

}
 
// Circle class extending Shape

class Circle extends Shape {

  constructor() {

    super();

    this.type = "Circle";

  }
 
  clone() {

    return Object.assign(Object.create(Object.getPrototypeOf(this)), this);

  }

}
 
// Rectangle class extending Shape

class Rectangle extends Shape {

  constructor() {

    super();

    this.type = "Rectangle";

  }
 
  clone() {

    return Object.assign(Object.create(Object.getPrototypeOf(this)), this);

  }

}
 
// Square class extending Shape

class Square extends Shape {

  constructor() {

    super();

    this.type = "Square";

  }
 
  clone() {

    return Object.assign(Object.create(Object.getPrototypeOf(this)), this);

  }

}
 
// ShapeCache class

class ShapeCache {

  constructor() {

    this.shapeMap = new Map();

  }
 
  loadCache() {

    const circle = new Circle();

    circle.setId("1");

    this.shapeMap.set(circle.getId(), circle);
 
    const rectangle = new Rectangle();

    rectangle.setId("2");

    this.shapeMap.set(rectangle.getId(), rectangle);
 
    const square = new Square();

    square.setId("3");

    this.shapeMap.set(square.getId(), square);

  }
 
  getShape(shapeId) {

    const cachedShape = this.shapeMap.get(shapeId);

    return cachedShape.clone();

  }

}
 
// PrototypePatternDemo function

function prototypePatternDemo() {

  const shapeCache = new ShapeCache();

  shapeCache.loadCache();
 
  const clonedShape1 = shapeCache.getShape("1");

  console.log("Shape: " + clonedShape1.getType());
 
  const clonedShape2 = shapeCache.getShape("2");

  console.log("Shape: " + clonedShape2.getType());
 
  const clonedShape3 = shapeCache.getShape("3");

  console.log("Shape: " + clonedShape3.getType());

}
 
// Run demo

prototypePatternDemo();

 