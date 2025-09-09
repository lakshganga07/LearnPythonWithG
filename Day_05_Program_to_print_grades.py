import os
import sys

def main():
    # Variables
    math = 85
    science = 92
    english = 78

    # Addition using operators
    total = math + science + english
    # Division using operators
    average = total / 3

    print("Total Marks:", total)
    print("Average:", average)

    # Control statement for grading
    if average >= 90:
        print("Grade: A 🎯")
    elif average >= 75:
        print("Grade: B 👍")
    elif average >= 50:
        print("Grade: C 🙂")
    else:
        print("Grade: D ❌")
if __name__ == '__main__':
    main()