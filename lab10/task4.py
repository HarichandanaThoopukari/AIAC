def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def find_highest(scores):
    return max(scores) if scores else None

def find_lowest(scores):
    return min(scores) if scores else None

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    return avg, highest, lowest

# Example usage
scores = [88, 92, 79, 93, 85]
process_scores(scores)