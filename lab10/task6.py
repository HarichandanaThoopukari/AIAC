def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def process_scores(scores):
    grades = [grade(score) for score in scores]
    print("Scores:", scores)
    print("Grades:", grades)
    return grades

# Example usage
scores = [95, 82, 67, 74, 58, 88]
process_scores(scores)