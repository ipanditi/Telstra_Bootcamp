function binarySearch(arr,target){
    let low=0;
    let high = arr.length-1;
    while(low<high){
        const mid = Math.floor((low+high)/2);
        if(arr[mid]===target) return mid;
        else if(arr[mid]<target) low=mid+1;
        else high=mid+1;
    }
    return -1;
}
let arr = [1,2,3,4]
let r = binarySearch(arr,2);
console.log(r);