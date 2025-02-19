def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = [12, 11, 13, 5, 6]
    print(f"Original array: {arr}")
    insertion_sort(arr)
    print(f"Sorted array: {arr}")

if __name__ == "__main__":
    main()
