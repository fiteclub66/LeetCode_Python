def bubbleSort(nums):
    # First outside loop needs to decrement down to 0.
    # This is because every iteration moves the largest number to the end of the list.
    # So once the largest number is at the end, no need to use it again in the comparison list.
    # So decrement down.
    # So the outside list works by saying for passnum in the range (creates an array: starting point, ending point,
    # how it will operate in the array).  So for passum in range of length of our unsorted list/array minus 1 (because
    # it returns the size of the list, and we need it to start at 0, not 1).  So starting at 5-1 (so 4), decrement
    # by 1 until 0.
    # Inner loop simply starts at 0 and increases up to the current size of passnum for each iteration, getting
    # smaller by 1 each time until it's done sorting.
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

    return nums

def main():
    nums = [14,46,43,27,57,41,45,21,70]
    bubbleSort(nums)
    print(nums)

if __name__ == "__main__":
    main()