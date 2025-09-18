"""
Demo script for the agritech feedback sentiment analyzer.
Shows various test cases and usage patterns.
"""

from task2 import simple_tokenizer, compute_sentiment, analyze_feedback_detailed


def demo_tokenizer():
    """Demonstrate the tokenizer functionality."""
    print("=" * 60)
    print("TOKENIZER DEMONSTRATION")
    print("=" * 60)
    
    test_cases = [
        "good product with bad packaging",
        "good! product, with. bad? packaging;",
        "GOOD Product With BAD Packaging",
        "good    product   with   bad   packaging",
        "good!@# product$%^ with&*() bad-=+",
        "This is a good product with great features but bad customer service",
        "",
        "   ",
        "good",
        "No sentiment words here"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\n{i}. Input: '{text}'")
        tokens = simple_tokenizer(text)
        print(f"   Tokens: {tokens}")
        print(f"   Count: {len(tokens)}")


def demo_sentiment_scoring():
    """Demonstrate the sentiment scoring functionality."""
    print("\n" + "=" * 60)
    print("SENTIMENT SCORING DEMONSTRATION")
    print("=" * 60)
    
    test_cases = [
        ("good product with bad packaging but great value", 2, "Sample case"),
        ("good great product", 3, "Only positive"),
        ("bad product bad quality", -2, "Only negative"),
        ("great product but bad service", 1, "Mixed sentiment"),
        ("product service quality", 0, "No sentiment words"),
        ("GOOD product with BAD packaging but GREAT value", 2, "Case insensitive"),
        ("good! product, with. bad? packaging; but great! value.", 2, "With punctuation"),
        ("good good great bad bad", 1, "Repeated words"),
        ("bad bad product", -2, "Negative score"),
        ("great great product", 4, "Positive score"),
        ("good bad", 0, "Zero score"),
        ("", 0, "Empty string")
    ]
    
    for text, expected, description in test_cases:
        result = compute_sentiment(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}: '{text}' -> {result}")


def demo_detailed_analysis():
    """Demonstrate the detailed analysis functionality."""
    print("\n" + "=" * 60)
    print("DETAILED ANALYSIS DEMONSTRATION")
    print("=" * 60)
    
    test_cases = [
        "good product with bad packaging but great value",
        "This is a great product with good features but bad customer service",
        "No sentiment words in this text",
        "bad bad bad product",
        "great great great product"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\n{i}. Text: '{text}'")
        result = analyze_feedback_detailed(text)
        
        print(f"   Total Score: {result['total_score']}")
        print(f"   Word Count: {result['word_count']}")
        print(f"   Sentiment Words: {result['sentiment_word_count']}")
        
        if result['sentiment_words']:
            print("   Sentiment Words Found:")
            for word_info in result['sentiment_words']:
                print(f"     - '{word_info['word']}' (score: {word_info['score']}, position: {word_info['position']})")
        else:
            print("   No sentiment words found.")


def interactive_demo():
    """Run an interactive demo where user can test their own inputs."""
    print("\n" + "=" * 60)
    print("INTERACTIVE DEMO")
    print("=" * 60)
    print("Test the sentiment analyzer with your own feedback!")
    print("Enter 'quit' to exit the demo.")
    print()
    
    while True:
        try:
            user_input = input("Enter feedback text: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                print("Please enter some feedback text!")
                continue
            
            # Show just the score
            result = compute_sentiment(user_input)
            print(f"\n{result}")
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


def run_performance_test():
    """Run a simple performance test."""
    print("\n" + "=" * 60)
    print("PERFORMANCE TEST")
    print("=" * 60)
    
    # Test with longer text
    long_text = "good product with great features but bad customer service " * 10
    print(f"Testing with {len(long_text)} characters...")
    
    import time
    start_time = time.time()
    
    # Run multiple iterations
    for _ in range(1000):
        compute_sentiment(long_text)
    
    end_time = time.time()
    
    print(f"✓ Processed 1000 iterations in {end_time - start_time:.4f} seconds")
    print(f"✓ Average time per analysis: {(end_time - start_time) / 1000 * 1000:.2f} ms")


if __name__ == "__main__":
    # Run demonstrations
    demo_tokenizer()
    demo_sentiment_scoring()
    demo_detailed_analysis()
    
    # Run performance test
    run_performance_test()
    
    # Ask if user wants interactive demo
    print("\nWould you like to try the interactive demo? (y/n): ", end="")
    try:
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            interactive_demo()
    except KeyboardInterrupt:
        print("\nGoodbye!")
