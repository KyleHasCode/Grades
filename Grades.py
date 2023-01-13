"""Language: Python 2.7.18"""

"""Determines the grade based on the number provided by the user"""
def grade_converter(grade):
    if grade >= 90:
        return "A, Excellent"
    elif grade == 89 or grade >= 80:
        return "B, Great"
    elif grade == 79 or grade >= 70:
        return "C, Good"
    elif grade == 69 or grade >= 65:
        return "D, Passable"
    else:
        return "F, Failed"

"""Prints the grade"""
print grade_converter(int(input("Enter grade number: ")))

