def find_min_max(arr):
    """
    Return (min_value, max_value) using divide and conquer.
    """
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
    data = [42, 17, 58, 3, 91, 26, 11, 39, 74, 5, 63, 28]
    minimum, maximum = find_min_max(data)
    print(f"Input: {data}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

