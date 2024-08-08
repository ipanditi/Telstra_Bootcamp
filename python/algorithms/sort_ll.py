class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap(ptr1, ptr2):
    tmp = ptr2.data
    ptr2.data = ptr1.data
    ptr1.data = tmp

def bubbleSort(head):
    swapped = True
    while swapped:
        swapped = False
        current = head

        while current.next:
            if current.data > current.next.data:
                swap(current, current.next)
                swapped = True
            current = current.next

def printList(n):
    while n:
        print(n.data, "->", end=" ")
        n = n.next
    print()

def insertAtTheBegin(start_ref, data):
    ptr1 = Node(data)
    ptr1.next = start_ref
    return ptr1

if __name__ == "__main__":
    arr = [0,1,0,1,0,1]
    list_size = len(arr)

    start = None

    # Create linked list from the array arr[]
    for i in range(list_size - 1, -1, -1):
        start = insertAtTheBegin(start, arr[i])

    print("Linked list before sorting")
    printList(start)

    bubbleSort(start)

    print("Linked list after sorting")
    printList(start)