# Custom Sorting Program

A Python implementation of the bubble sort algorithm with comprehensive testing and user input functionality.

## Files

- `task1.py` - Main sorting program with user input functionality
- `test_task1.py` - Comprehensive test suite with 14+ test cases
- `demo.py` - Demonstration script showing various test cases
- `run_tests.py` - Script to run all tests and demos

## Features

### Sorting Function (`custom_sort`)
- Implements bubble sort algorithm
- Handles all data types (positive, negative, zero)
- Creates a copy of input to avoid modifying original list
- Well-documented with docstrings

### Empty List Function (`empty_list`)
- Empties a list by removing all elements
- Creates a copy of input to avoid modifying original list
- Returns an empty list regardless of input
- Well-documented with docstrings

### User Input Functionality
- Interactive command-line interface
- Supports both space and comma-separated input
- Input validation and error handling
- Option to perform multiple operations in one session
- Three operation modes: sort, empty, or both

### Comprehensive Testing
- 14+ automated test cases covering edge cases
- Tests for empty lists, single elements, duplicates, large numbers, negative numbers
- Randomized input testing
- Performance testing with larger datasets
- Detailed documentation for each test case

## Usage

### Interactive Mode
```bash
python task1.py
```

### Run Tests
```bash
python test_task1.py
```

### Run Demo
```bash
python demo.py
```

### Run All Tests and Demo
```bash
python run_tests.py
```

## Test Cases Covered

1. **Empty List** - Verifies function handles empty input gracefully
2. **Single Element** - Tests minimal non-empty input
3. **Already Sorted** - Tests best-case scenario efficiency
4. **Reverse Sorted** - Tests worst-case scenario (bubble sort)
5. **Duplicates** - Tests handling of repeated values
6. **Large Numbers** - Tests with large integer values
7. **Negative Numbers** - Tests negative value handling
8. **Mixed Values** - Tests combination of positive, negative, and zero
9. **All Negative** - Tests when all values are negative
10. **All Same Elements** - Tests identical element handling
11. **Two Elements** - Tests minimal non-trivial case
12. **Randomized Input** - Tests with random data
13. **Very Small Numbers** - Tests with small integer values
14. **Sorting Property Verification** - Mathematical verification of correctness

## Sample Input/Output

### Sorting Examples
```
Input: [5, 3, 1, 4, 2]
Output: [1, 2, 3, 4, 5]

Input: [10, -1, 0]
Output: [-1, 0, 10]

Input: [5, 5, 2, 2]
Output: [2, 2, 5, 5]

Input: []
Output: []

Input: [42]
Output: [42]
```

### Empty List Examples
```
Input: [1, 2, 3, 4, 5]
Output: []

Input: [42]
Output: []

Input: []
Output: []

Input: [5, 5, 2, 2]
Output: []
```

## Algorithm Details

The implementation uses bubble sort, which:
- Time Complexity: O(n²) in worst case, O(n) in best case
- Space Complexity: O(1) additional space
- Stable: Maintains relative order of equal elements
- In-place: Sorts by swapping elements

## Requirements

- Python 3.6+
- No external dependencies required

## Error Handling

- Input validation for non-numeric values
- Graceful handling of empty input
- Keyboard interrupt handling (Ctrl+C)
- Clear error messages for invalid input
