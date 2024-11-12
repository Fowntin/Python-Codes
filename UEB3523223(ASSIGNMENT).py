# Function to determine the student's division
def determine_division(gpa):
    if 3.60 <= gpa <= 4.00:
        return "First class"
    elif 3.00 <= gpa < 3.60:
        return "Second class (Upper)"
    elif 2.00 <= gpa < 3.00:
        return "Second class (Lower)"
    elif 1.50 <= gpa < 2.00:
        return "Third class"
    elif 1.00 <= gpa < 1.50:
        return "Pass"
    else:
        return "Fail"

# Main program
def main():
    # Get the student's name and GPA
    student_name = input("Enter the student's name: ")
    gpa = float(input("Enter the student's GPA: "))

    # Determine the division
    division = determine_division(gpa)

    # Print the result
    print(f"{student_name} is in {division}")

# Run the program
if __name__ == "__main__":
    main()
