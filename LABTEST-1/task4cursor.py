import csv

def read_student_data(csv_file):
    """
    Read student data from CSV file
    """
    students = []
    
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Extract student data
                student = {
                    'name': row['Name'],
                    'subject1': int(row['subject-1']),
                    'subject2': int(row['subject-2']),
                    'subject3': int(row['subject-3'])
                }
                students.append(student)
        return students
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def calculate_marks(students):
    """
    Calculate total and average marks for each student
    """
    results = []
    
    for student in students:
        # Calculate total and average
        total = student['subject1'] + student['subject2'] + student['subject3']
        average = total / 3
        
        # Store results
        result = {
            'name': student['name'],
            'subject1': student['subject1'],
            'subject2': student['subject2'],
            'subject3': student['subject3'],
            'total': total,
            'average': round(average, 2)
        }
        results.append(result)
    
    return results

def display_results(results):
    """
    Display results in a formatted table
    """
    print("\n" + "="*80)
    print(f"{'Name':<15} {'Subject-1':<12} {'Subject-2':<12} {'Subject-3':<12} {'Total':<10} {'Average':<10}")
    print("="*80)
    
    for student in results:
        print(f"{student['name']:<15} {student['subject1']:<12} {student['subject2']:<12} "
              f"{student['subject3']:<12} {student['total']:<10} {student['average']:<10}")
    
    print("="*80)

def display_summary(results):
    """
    Display summary statistics
    """
    print("\nSUMMARY STATISTICS:")
    print("-" * 30)
    
    total_students = len(results)
    class_total = sum(student['total'] for student in results)
    class_average = class_total / total_students
    
    print(f"Total Students: {total_students}")
    print(f"Class Average: {round(class_average, 2)}")
    
    # Find top performer
    top_student = max(results, key=lambda x: x['total'])
    print(f"Top Performer: {top_student['name']} (Total: {top_student['total']})")
    
    # Find lowest performer
    lowest_student = min(results, key=lambda x: x['total'])
    print(f"Lowest Performer: {lowest_student['name']} (Total: {lowest_student['total']})")

def main():
    """
    Main function
    """
    print("STUDENT MARKS CALCULATOR")
    print("=" * 50)
    
    # CSV file name
    csv_file = 'sample_students.csv'
    
    # Read student data
    print(f"Reading data from {csv_file}...")
    students = read_student_data(csv_file)
    
    if students is None:
        print("Could not read student data. Please check if the CSV file exists and has the correct format.")
        print("\nExpected CSV format:")
        print("Name,subject-1,subject-2,subject-3")
        print("john,23,67,89")
        print("peter,67,98,77")
        return
    
    if not students:
        print("No student data found in the file.")
        return
    
    print(f"Found {len(students)} students in the file.")
    
    # Calculate marks
    print("Calculating totals and averages...")
    results = calculate_marks(students)
    
    # Display results
    display_results(results)
    
    # Display summary
    display_summary(results)

if __name__ == "__main__":
    main()
