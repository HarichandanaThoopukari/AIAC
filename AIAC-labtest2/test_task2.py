"""
Comprehensive test suite for the agritech feedback sentiment analyzer.
Tests tokenization, sentiment scoring, and edge cases.
"""

import unittest
from task2 import simple_tokenizer, compute_sentiment, analyze_feedback_detailed


class TestSimpleTokenizer(unittest.TestCase):
    """Test cases for the simple_tokenizer function."""
    
    def test_basic_tokenization(self):
        """Test basic tokenization with spaces."""
        text = "good product with bad packaging"
        result = simple_tokenizer(text)
        expected = ["good", "product", "with", "bad", "packaging"]
        self.assertEqual(result, expected)
        print("✓ Basic tokenization test passed")
    
    def test_punctuation_stripping(self):
        """Test that punctuation is stripped from tokens."""
        text = "good! product, with. bad? packaging;"
        result = simple_tokenizer(text)
        expected = ["good", "product", "with", "bad", "packaging"]
        self.assertEqual(result, expected)
        print("✓ Punctuation stripping test passed")
    
    def test_case_insensitive(self):
        """Test that tokens are converted to lowercase."""
        text = "GOOD Product With BAD Packaging"
        result = simple_tokenizer(text)
        expected = ["good", "product", "with", "bad", "packaging"]
        self.assertEqual(result, expected)
        print("✓ Case insensitive test passed")
    
    def test_empty_string(self):
        """Test tokenization of empty string."""
        result = simple_tokenizer("")
        self.assertEqual(result, [])
        print("✓ Empty string test passed")
    
    def test_whitespace_only(self):
        """Test tokenization of whitespace-only string."""
        result = simple_tokenizer("   \t\n  ")
        self.assertEqual(result, [])
        print("✓ Whitespace only test passed")
    
    def test_single_word(self):
        """Test tokenization of single word."""
        result = simple_tokenizer("good")
        self.assertEqual(result, ["good"])
        print("✓ Single word test passed")
    
    def test_multiple_spaces(self):
        """Test tokenization with multiple spaces."""
        text = "good    product   with   bad   packaging"
        result = simple_tokenizer(text)
        expected = ["good", "product", "with", "bad", "packaging"]
        self.assertEqual(result, expected)
        print("✓ Multiple spaces test passed")
    
    def test_punctuation_only_tokens(self):
        """Test handling of punctuation-only tokens."""
        text = "good !!! product ??? bad"
        result = simple_tokenizer(text)
        expected = ["good", "product", "bad"]
        self.assertEqual(result, expected)
        print("✓ Punctuation only tokens test passed")
    
    def test_mixed_punctuation(self):
        """Test with various punctuation marks."""
        text = "good!@# product$%^ with&*() bad-=+"
        result = simple_tokenizer(text)
        expected = ["good", "product", "with", "bad"]
        self.assertEqual(result, expected)
        print("✓ Mixed punctuation test passed")
    
    def test_non_string_input(self):
        """Test handling of non-string input."""
        result = simple_tokenizer(None)
        self.assertEqual(result, [])
        print("✓ Non-string input test passed")


class TestComputeSentiment(unittest.TestCase):
    """Test cases for the compute_sentiment function."""
    
    def test_sample_input(self):
        """Test the provided sample input."""
        text = "good product with bad packaging but great value"
        result = compute_sentiment(text)
        expected = 2  # good(+1) + bad(-1) + great(+2) = 2
        self.assertEqual(result, expected)
        print("✓ Sample input test passed")
    
    def test_only_positive_words(self):
        """Test with only positive sentiment words."""
        text = "good great product"
        result = compute_sentiment(text)
        expected = 3  # good(+1) + great(+2) = 3
        self.assertEqual(result, expected)
        print("✓ Only positive words test passed")
    
    def test_only_negative_words(self):
        """Test with only negative sentiment words."""
        text = "bad product bad quality"
        result = compute_sentiment(text)
        expected = -2  # bad(-1) + bad(-1) = -2
        self.assertEqual(result, expected)
        print("✓ Only negative words test passed")
    
    def test_mixed_sentiment(self):
        """Test with mixed positive and negative words."""
        text = "great product but bad service"
        result = compute_sentiment(text)
        expected = 1  # great(+2) + bad(-1) = 1
        self.assertEqual(result, expected)
        print("✓ Mixed sentiment test passed")
    
    def test_no_sentiment_words(self):
        """Test with no sentiment words."""
        text = "product service quality"
        result = compute_sentiment(text)
        expected = 0
        self.assertEqual(result, expected)
        print("✓ No sentiment words test passed")
    
    def test_empty_string(self):
        """Test with empty string."""
        result = compute_sentiment("")
        expected = 0
        self.assertEqual(result, expected)
        print("✓ Empty string test passed")
    
    def test_case_insensitive_sentiment(self):
        """Test that sentiment scoring is case insensitive."""
        text = "GOOD product with BAD packaging but GREAT value"
        result = compute_sentiment(text)
        expected = 2  # good(+1) + bad(-1) + great(+2) = 2
        self.assertEqual(result, expected)
        print("✓ Case insensitive sentiment test passed")
    
    def test_punctuation_with_sentiment(self):
        """Test sentiment scoring with punctuation."""
        text = "good! product, with. bad? packaging; but great! value."
        result = compute_sentiment(text)
        expected = 2  # good(+1) + bad(-1) + great(+2) = 2
        self.assertEqual(result, expected)
        print("✓ Punctuation with sentiment test passed")
    
    def test_repeated_sentiment_words(self):
        """Test with repeated sentiment words."""
        text = "good good great bad bad"
        result = compute_sentiment(text)
        expected = 1  # good(+1) + good(+1) + great(+2) + bad(-1) + bad(-1) = 2
        self.assertEqual(result, expected)
        print("✓ Repeated sentiment words test passed")
    
    def test_zero_score(self):
        """Test that results in zero score."""
        text = "good bad"  # +1 -1 = 0
        result = compute_sentiment(text)
        expected = 0
        self.assertEqual(result, expected)
        print("✓ Zero score test passed")
    
    def test_negative_score(self):
        """Test negative total score."""
        text = "bad bad product"  # -1 -1 = -2
        result = compute_sentiment(text)
        expected = -2
        self.assertEqual(result, expected)
        print("✓ Negative score test passed")
    
    def test_positive_score(self):
        """Test positive total score."""
        text = "great great product"  # +2 +2 = +4
        result = compute_sentiment(text)
        expected = 4
        self.assertEqual(result, expected)
        print("✓ Positive score test passed")
    
    def test_whitespace_handling(self):
        """Test with various whitespace patterns."""
        text = "  good   product   with   bad   packaging  "
        result = compute_sentiment(text)
        expected = 0  # good(+1) + bad(-1) = 0
        self.assertEqual(result, expected)
        print("✓ Whitespace handling test passed")
    
    def test_single_sentiment_word(self):
        """Test with single sentiment word."""
        text = "good"
        result = compute_sentiment(text)
        expected = 1
        self.assertEqual(result, expected)
        print("✓ Single sentiment word test passed")
    
    def test_complex_sentence(self):
        """Test with complex sentence structure."""
        text = "This is a good product with great features but bad customer service"
        result = compute_sentiment(text)
        expected = 2  # good(+1) + great(+2) + bad(-1) = 2
        self.assertEqual(result, expected)
        print("✓ Complex sentence test passed")


class TestAnalyzeFeedbackDetailed(unittest.TestCase):
    """Test cases for the analyze_feedback_detailed function."""
    
    def test_detailed_analysis_sample(self):
        """Test detailed analysis with sample input."""
        text = "good product with bad packaging but great value"
        result = analyze_feedback_detailed(text)
        
        # Check basic structure
        self.assertEqual(result['original_text'], text)
        self.assertEqual(result['total_score'], 2)
        self.assertEqual(result['word_count'], 8)
        self.assertEqual(result['sentiment_word_count'], 3)
        
        # Check sentiment words
        sentiment_words = result['sentiment_words']
        self.assertEqual(len(sentiment_words), 3)
        
        # Check specific sentiment words
        word_scores = {word['word']: word['score'] for word in sentiment_words}
        self.assertEqual(word_scores['good'], 1)
        self.assertEqual(word_scores['bad'], -1)
        self.assertEqual(word_scores['great'], 2)
        
        print("✓ Detailed analysis sample test passed")
    
    def test_detailed_analysis_no_sentiment(self):
        """Test detailed analysis with no sentiment words."""
        text = "product service quality"
        result = analyze_feedback_detailed(text)
        
        self.assertEqual(result['total_score'], 0)
        self.assertEqual(result['sentiment_word_count'], 0)
        self.assertEqual(result['sentiment_words'], [])
        print("✓ Detailed analysis no sentiment test passed")
    
    def test_detailed_analysis_empty(self):
        """Test detailed analysis with empty string."""
        text = ""
        result = analyze_feedback_detailed(text)
        
        self.assertEqual(result['total_score'], 0)
        self.assertEqual(result['word_count'], 0)
        self.assertEqual(result['sentiment_word_count'], 0)
        self.assertEqual(result['sentiment_words'], [])
        print("✓ Detailed analysis empty test passed")


def run_edge_case_tests():
    """Run additional edge case tests."""
    print("\n" + "="*50)
    print("EDGE CASE TESTS")
    print("="*50)
    
    # Test cases for edge scenarios
    edge_cases = [
        ("", 0, "Empty string"),
        ("   ", 0, "Whitespace only"),
        ("good", 1, "Single positive word"),
        ("bad", -1, "Single negative word"),
        ("great", 2, "Single great word"),
        ("good bad", 0, "Equal positive and negative"),
        ("great great", 4, "Multiple great words"),
        ("bad bad bad", -3, "Multiple bad words"),
        ("good!@# bad??? great!!!", 2, "Punctuation mixed"),
        ("GOOD BAD GREAT", 2, "All caps"),
        ("good product with bad packaging but great value", 2, "Sample case"),
        ("This product is good but the service is bad", 0, "Mixed with neutral words"),
        ("No sentiment words here", 0, "No sentiment words"),
        ("good good good", 3, "Repeated positive"),
        ("bad bad bad bad", -4, "Repeated negative")
    ]
    
    all_passed = True
    for text, expected, description in edge_cases:
        result = compute_sentiment(text)
        if result == expected:
            print(f"✓ {description}: '{text}' -> {result}")
        else:
            print(f"✗ {description}: '{text}' -> {result} (expected {expected})")
            all_passed = False
    
    if all_passed:
        print("\n✓ All edge case tests passed!")
    else:
        print("\n✗ Some edge case tests failed!")
    
    return all_passed


if __name__ == "__main__":
    print("="*60)
    print("COMPREHENSIVE TEST SUITE FOR SENTIMENT ANALYZER")
    print("="*60)
    print()
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=0)
    
    # Run edge case tests
    run_edge_case_tests()
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
