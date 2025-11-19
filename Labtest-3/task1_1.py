def find_min_max(arr):
    if not arr:
        raise ValueError("Input array must not be empty")

    def helper(left, right):
        if left == right:
            return arr[left], arr[left]
        if right - left == 1:
            return (min(arr[left], arr[right]), max(arr[left], arr[right]))
        mid = (left + right) // 2
        left_min, left_max = helper(left, mid)
        right_min, right_max = helper(mid + 1, right)
        return min(left_min, right_min), max(left_max, right_max)

    return helper(0, len(arr) - 1)


if __name__ == "__main__":
    print("Enter 12 numbers separated by spaces:")
    user_input = input().strip()
    values = [float(num) for num in user_input.split()]
    if len(values) != 12:
        raise ValueError("Please enter exactly 12 numbers.")
    minimum, maximum = find_min_max(values)
    print(f"Values: {values}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

