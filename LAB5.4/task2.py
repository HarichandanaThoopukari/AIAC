import re
from collections import Counter

def preprocess_text(text):
    # Remove offensive terms (example list, expand as needed)
    offensive_terms = ['offensiveword1', 'offensiveword2']
    pattern = re.compile('|'.join(map(re.escape, offensive_terms)), re.IGNORECASE)
    text = pattern.sub('[REMOVED]', text)
    # Basic cleaning
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

def balance_dataset(data):
    # Simple balancing: equalize positive and negative samples
    pos = [d for d in data if d[1] == 'positive']
    neg = [d for d in data if d[1] == 'negative']
    min_len = min(len(pos), len(neg))
    balanced = pos[:min_len] + neg[:min_len]
    return balanced

def sentiment_analysis(data):
    # Very basic sentiment analysis using word lists
    positive_words = {'good', 'happy', 'excellent', 'great', 'love', 'wonderful'}
    negative_words = {'bad', 'sad', 'terrible', 'hate', 'awful', 'poor'}
    results = []
    for text in data:
        text_clean = preprocess_text(text)
        words = set(text_clean.split())
        pos_score = len(words & positive_words)
        neg_score = len(words & negative_words)
        if pos_score > neg_score:
            results.append((text, 'positive'))
        elif neg_score > pos_score:
            results.append((text, 'negative'))
        else:
            results.append((text, 'neutral'))
    return results

def main():
    print("Enter your data (one sentence per line, empty line to finish):")
    user_data = []
    while True:
        line = input()
        if not line.strip():
            break
        user_data.append(line)
    # Preprocess and analyze
    analyzed = sentiment_analysis(user_data)
    # Count classes for bias check
    counts = Counter([label for _, label in analyzed])
    print("Sentiment counts:", counts)
    # Example: balance dataset if needed
    balanced = balance_dataset([(text, label) for text, label in analyzed if label in ('positive', 'negative')])
    print("Balanced dataset size:", len(balanced))
    print("Results:")
    for text, label in analyzed:
        print(f"'{text}' => {label}")

if __name__ == "__main__":
    main()

# Bias Mitigation Strategies:
# - Offensive terms are removed during preprocessing.
# - Dataset is balanced to avoid bias toward majority sentiment.
# - Expand offensive_terms and sentiment word lists for better coverage.
# - Consider using more advanced models and fairness metrics for production use.