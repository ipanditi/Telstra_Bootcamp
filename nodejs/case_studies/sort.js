function bubbleSort(arr) {
    let n = arr.length;
    // Traverse through all elements in the array
    for (let i = 0; i < n - 1; i++) {
        // Last i elements are already sorted
        for (let j = 0; j < n - i - 1; j++) {
            // Compare adjacent elements
            if (arr[j] > arr[j + 1]) {
                // Swap if the element found is greater than the next element
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
 
let arr = ["sam", "adams", "williams", "vivek"];
 
// Sort the array
bubbleSort(arr);
 
// Print the sorted array
console.log("Sorted array:", arr);  