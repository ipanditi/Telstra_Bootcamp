//result = (x,y) => x+y
function callfunc(f,a,b){
    return f(a,b)
}
//console.log(callfunc(result,12,23))
let arr=[12,23,11,19,55,27]
//arr.map((a)=>console.log(a));
const res=arr.filter((a)=>a%2==0);
//console.log(res);
const res1=arr.reduce((a,b)=>a+b);
//console.log(res1);

function calculateCircleArea(radius) {
    if (radius < 0) {

        throw new Error("Radius cannot be negative");
    }
    const pi = Math.PI;
    return pi * radius * radius;
}
let area = calculateCircleArea(12)
//console.log(area)

let a = [12,23,11,19,55,67,32,17]
const max =a.reduce((a, b) => Math.max(a, b), -Infinity);
const min =a.reduce((a, b) => Math.min(a, b), Infinity);
console.log(min)