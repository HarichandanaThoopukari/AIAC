"""
Simple test script to verify the sample input works correctly.
"""

from task2 import compute_sentiment

def test_sample():
    """Test the provided sample input."""
    sample_input = "good product with bad packaging but great value"
    expected_output = 2
    
    result = compute_sentiment(sample_input)
    
    print(f"Input: '{sample_input}'")
    print(f"Expected: {expected_output}")
    print(f"Actual: {result}")
    print(f"Test: {'PASS' if result == expected_output else 'FAIL'}")
    
    return result == expected_output

if __name__ == "__main__":
    print("Testing sample input...")
    test_sample()
