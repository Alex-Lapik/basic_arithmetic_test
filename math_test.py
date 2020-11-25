"""

Basic arithmetic test

"""

import random


def arithmetic_test(numberOfQuestions=10, studentName=input("Name: ")):
    correct_answers = 0  # Keep track of correct answers

    # Repeat x many times for number of questions
    for _ in range(0, numberOfQuestions):

        # Create an array with 2 random numbers for the equation
        numbers = sorted([random.randint(1, 10)
                          for _ in range(0, 2)], reverse=True)

        # Generate a random number, 0 == addition and 1 == subtraction
        operation = random.randint(0, 1)

        print(numbers[0], ''.join(
            ['-' if num == '1' else '+' for num in str(operation)]), numbers[1])  # Display question

        try:  # This will prevent the program from rasing an error.

            if operation == 0:  # Addition

                if int(input()) == numbers[0] + numbers[1]:
                    correct_answers += 1

            else:  # Subtraction

                if int(input()) == numbers[0] - numbers[1]:
                    correct_answers += 1

        except ValueError:
            continue

    print(''.join(studentName + ', ' + str(correct_answers) +
                  ' out of ' + str(numberOfQuestions)))  # Print test results

    return correct_answers


if __name__ == "__main__":
    arithmetic_test()
