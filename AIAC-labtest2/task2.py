"""
Lightweight Agritech Feedback Analyzer
Computes sentiment scores using a simple lexicon: good=+1, great=+2, bad=-1
"""

import re
import string


def simple_tokenizer(text):
    """
    Tokenize text by spaces and strip simple punctuation.
    
    Args:
        text (str): Input text to tokenize
        
    Returns:
        list: List of cleaned tokens
    """
    if not text or not isinstance(text, str):
        return []
    
    # Split by whitespace
    tokens = text.split()
    
    # Strip punctuation from each token
    cleaned_tokens = []
    for token in tokens:
        # Remove punctuation from start and end of token
        cleaned_token = token.strip(string.punctuation)
        if cleaned_token:  # Only add non-empty tokens
            cleaned_tokens.append(cleaned_token.lower())
    
    return cleaned_tokens


def compute_sentiment(text):
    """
    Compute total sentiment score using lexicon: good=+1, great=+2, bad=-1
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        int: Total sentiment score
    """
    # Tokenize the input text
    tokens = simple_tokenizer(text)
    
    # Define sentiment lexicon
    sentiment_scores = {
        'good': 1,
        'great': 2,
        'bad': -1
    }
    
    # Calculate total sentiment score
    total_score = 0
    for token in tokens:
        if token in sentiment_scores:
            total_score += sentiment_scores[token]
    
    return total_score


def get_user_feedback():
    """
    Get feedback text from user with validation.
    
    Returns:
        str: User input text or None if user wants to exit
    """
    print("Enter agritech feedback text to analyze:")
    print("(Type 'quit' to exit)")
    print()
    
    while True:
        try:
            user_input = input("Feedback: ").strip()
            
            if not user_input:
                print("Please enter some feedback text!")
                continue
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                return None
                
            return user_input
            
        except KeyboardInterrupt:
            print("\nExiting...")
            return None


def analyze_feedback_detailed(text):
    """
    Provide detailed analysis of feedback text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Detailed analysis results
    """
    tokens = simple_tokenizer(text)
    sentiment_scores = {'good': 1, 'great': 2, 'bad': -1}
    
    # Find sentiment words and their positions
    sentiment_words = []
    for i, token in enumerate(tokens):
        if token in sentiment_scores:
            sentiment_words.append({
                'word': token,
                'score': sentiment_scores[token],
                'position': i
            })
    
    total_score = sum(word['score'] for word in sentiment_words)
    
    return {
        'original_text': text,
        'tokens': tokens,
        'sentiment_words': sentiment_words,
        'total_score': total_score,
        'word_count': len(tokens),
        'sentiment_word_count': len(sentiment_words)
    }


def main():
    """Main function to run the sentiment analyzer with user input."""
    print("=" * 50)
    print("AGRITECH FEEDBACK SENTIMENT ANALYZER")
    print("=" * 50)
    print("Lexicon: good=+1, great=+2, bad=-1")
    print("Enter feedback text to get sentiment score.")
    print()
    
    while True:
        # Get feedback from user
        feedback = get_user_feedback()
        
        if feedback is None:  # User wants to exit
            break
        
        # Analyze the feedback
        result = analyze_feedback_detailed(feedback)
        
        # Display results - just the score
        print(f"\n{result['total_score']}")
        
        # Ask if user wants to continue
        print("\n" + "-" * 40)
        while True:
            continue_choice = input("Analyze another feedback? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes']:
                print()
                break
            elif continue_choice in ['n', 'no']:
                print("Thank you for using the sentiment analyzer!")
                return
            else:
                print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
