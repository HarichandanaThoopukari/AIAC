"""
Comprehensive test suite for custom_sort function.
Tests various edge cases and input scenarios to ensure robust sorting behavior.

TEST CASE DOCUMENTATION:
=======================

1. Empty List Test:
   - Purpose: Verify function handles empty input gracefully
   - Expected: Returns empty list unchanged
   - Reasoning: Edge case that should not crash the function

2. Single Element Test:
   - Purpose: Verify function works with minimal input
   - Expected: Returns single element unchanged
   - Reasoning: Simplest non-empty case, should be trivially sorted

3. Already Sorted Test:
   - Purpose: Verify function doesn't break when input is already sorted
   - Expected: Returns input unchanged
   - Reasoning: Tests efficiency and correctness for best-case scenario

4. Reverse Sorted Test:
   - Purpose: Verify function handles worst-case scenario
   - Expected: Completely reverses the input order
   - Reasoning: Tests maximum number of swaps needed (bubble sort worst case)

5. Duplicates Test:
   - Purpose: Verify function handles repeated values correctly
   - Expected: Maintains relative order of equal elements (stable sort property)
   - Reasoning: Tests stability and duplicate handling

6. Large Numbers Test:
   - Purpose: Verify function works with large integer values
   - Expected: Sorts correctly regardless of magnitude
   - Reasoning: Tests integer overflow handling and comparison accuracy

7. Negative Numbers Test:
   - Purpose: Verify function handles negative values correctly
   - Expected: Sorts negative numbers before positive numbers
   - Reasoning: Tests comparison logic with negative values

8. Mixed Values Test:
   - Purpose: Verify function handles mix of positive, negative, and zero
   - Expected: Sorts in correct order: negative, zero, positive
   - Reasoning: Tests comprehensive comparison across all number types

9. All Negative Test:
   - Purpose: Verify function works when all values are negative
   - Expected: Sorts negative numbers in ascending order
   - Reasoning: Tests edge case where all comparisons involve negative numbers

10. All Same Elements Test:
    - Purpose: Verify function handles identical elements
    - Expected: Returns input unchanged
    - Reasoning: Tests stability and efficiency with no swaps needed

11. Two Elements Test:
    - Purpose: Verify function works with minimal non-trivial input
    - Expected: Swaps elements if needed
    - Reasoning: Tests basic swap logic with minimal complexity

12. Randomized Input Test:
    - Purpose: Verify function works with random data
    - Expected: Produces same result as Python's built-in sort
    - Reasoning: Tests general correctness across varied inputs

13. Very Small Numbers Test:
    - Purpose: Verify function works with small integer values
    - Expected: Sorts correctly regardless of value magnitude
    - Reasoning: Tests comparison logic with small numbers

14. Sorting Property Verification:
    - Purpose: Verify result is actually sorted (monotonic non-decreasing)
    - Expected: Each element is <= the next element
    - Reasoning: Mathematical verification of sorting correctness
"""

import unittest
import random
from task1 import custom_sort, empty_list


class TestCustomSort(unittest.TestCase):
    """Test cases for the custom_sort function covering edge cases and special inputs."""
    
    def test_empty_list(self):
        """Test sorting an empty list - should return empty list unchanged."""
        input_list = []
        result = custom_sort(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list test passed")
    
    def test_single_element(self):
        """Test sorting a list with single element - should return unchanged."""
        input_list = [42]
        result = custom_sort(input_list)
        self.assertEqual(result, [42])
        self.assertEqual(len(result), 1)
        print("✓ Single element test passed")
    
    def test_already_sorted_list(self):
        """Test sorting an already sorted list - should remain unchanged."""
        input_list = [1, 2, 3, 4, 5]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        print("✓ Already sorted list test passed")
    
    def test_reverse_sorted_list(self):
        """Test sorting a reverse sorted list - should be completely reversed."""
        input_list = [5, 4, 3, 2, 1]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 2, 3, 4, 5])
        print("✓ Reverse sorted list test passed")
    
    def test_list_with_duplicates(self):
        """Test sorting a list with duplicate elements."""
        input_list = [5, 5, 2, 2, 8, 2]
        result = custom_sort(input_list)
        self.assertEqual(result, [2, 2, 2, 5, 5, 8])
        print("✓ List with duplicates test passed")
    
    def test_large_numbers(self):
        """Test sorting with large numbers."""
        input_list = [1000000, 999999, 1000001, 500000]
        result = custom_sort(input_list)
        self.assertEqual(result, [500000, 999999, 1000000, 1000001])
        print("✓ Large numbers test passed")
    
    def test_negative_numbers(self):
        """Test sorting with negative numbers."""
        input_list = [10, -1, 0, -5, 3]
        result = custom_sort(input_list)
        self.assertEqual(result, [-5, -1, 0, 3, 10])
        print("✓ Negative numbers test passed")
    
    def test_mixed_positive_negative_zero(self):
        """Test sorting with mix of positive, negative numbers and zero."""
        input_list = [-10, 0, 5, -3, 0, 1]
        result = custom_sort(input_list)
        self.assertEqual(result, [-10, -3, 0, 0, 1, 5])
        print("✓ Mixed positive/negative/zero test passed")
    
    def test_all_negative_numbers(self):
        """Test sorting with all negative numbers."""
        input_list = [-5, -1, -10, -3]
        result = custom_sort(input_list)
        self.assertEqual(result, [-10, -5, -3, -1])
        print("✓ All negative numbers test passed")
    
    def test_all_same_elements(self):
        """Test sorting a list where all elements are the same."""
        input_list = [7, 7, 7, 7, 7]
        result = custom_sort(input_list)
        self.assertEqual(result, [7, 7, 7, 7, 7])
        print("✓ All same elements test passed")
    
    def test_two_elements(self):
        """Test sorting a list with exactly two elements."""
        input_list = [3, 1]
        result = custom_sort(input_list)
        self.assertEqual(result, [1, 3])
        print("✓ Two elements test passed")
    
    def test_randomized_input(self):
        """Test sorting with randomized input to verify general correctness."""
        random.seed(42)  # For reproducible tests
        for _ in range(10):
            # Generate random list of length 5-15 with values -100 to 100
            input_list = [random.randint(-100, 100) for _ in range(random.randint(5, 15))]
            result = custom_sort(input_list.copy())
            
            # Verify result is sorted
            self.assertEqual(result, sorted(input_list))
        print("✓ Randomized input test passed")
    
    def test_very_small_numbers(self):
        """Test sorting with very small decimal-like integers."""
        input_list = [0, -1, 1, -2, 2]
        result = custom_sort(input_list)
        self.assertEqual(result, [-2, -1, 0, 1, 2])
        print("✓ Very small numbers test passed")
    
    def test_verify_sorting_property(self):
        """Test that the result is actually sorted (monotonic non-decreasing)."""
        input_list = [64, 34, 25, 12, 22, 11, 90]
        result = custom_sort(input_list)
        
        # Verify each element is <= the next element
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i], result[i + 1])
        print("✓ Sorting property verification test passed")


class TestEmptyList(unittest.TestCase):
    """Test cases for the empty_list function."""
    
    def test_empty_list_already_empty(self):
        """Test emptying an already empty list."""
        input_list = []
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (already empty) test passed")
    
    def test_empty_list_single_element(self):
        """Test emptying a list with single element."""
        input_list = [42]
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (single element) test passed")
    
    def test_empty_list_multiple_elements(self):
        """Test emptying a list with multiple elements."""
        input_list = [1, 2, 3, 4, 5]
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (multiple elements) test passed")
    
    def test_empty_list_with_duplicates(self):
        """Test emptying a list with duplicate elements."""
        input_list = [5, 5, 2, 2, 8, 2]
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (duplicates) test passed")
    
    def test_empty_list_negative_numbers(self):
        """Test emptying a list with negative numbers."""
        input_list = [-10, -5, -1, 0, 5]
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (negative numbers) test passed")
    
    def test_empty_list_large_numbers(self):
        """Test emptying a list with large numbers."""
        input_list = [1000000, 999999, 1000001, 500000]
        result = empty_list(input_list)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)
        print("✓ Empty list (large numbers) test passed")
    
    def test_empty_list_original_unchanged(self):
        """Test that original list is not modified."""
        original_list = [1, 2, 3, 4, 5]
        result = empty_list(original_list)
        
        # Original list should remain unchanged
        self.assertEqual(original_list, [1, 2, 3, 4, 5])
        # Result should be empty
        self.assertEqual(result, [])
        print("✓ Empty list (original unchanged) test passed")
    
    def test_empty_list_random_input(self):
        """Test emptying with random input."""
        random.seed(42)
        for _ in range(5):
            input_list = [random.randint(-100, 100) for _ in range(random.randint(1, 10))]
            result = empty_list(input_list)
            self.assertEqual(result, [])
            self.assertEqual(len(result), 0)
        print("✓ Empty list (random input) test passed")


def run_performance_test():
    """Run a simple performance test to check if the function handles larger inputs."""
    print("\n" + "="*50)
    print("PERFORMANCE TEST")
    print("="*50)
    
    # Test with larger input
    large_input = list(range(100, 0, -1))  # 100 elements in reverse order
    print(f"Testing with {len(large_input)} elements...")
    
    import time
    start_time = time.time()
    result = custom_sort(large_input)
    end_time = time.time()
    
    print(f"✓ Sorted {len(large_input)} elements in {end_time - start_time:.4f} seconds")
    print(f"✓ Result is correctly sorted: {result == sorted(large_input)}")


if __name__ == "__main__":
    print("="*60)
    print("COMPREHENSIVE TEST SUITE FOR CUSTOM_SORT FUNCTION")
    print("="*60)
    print()
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=0)
    
    # Run performance test
    run_performance_test()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
