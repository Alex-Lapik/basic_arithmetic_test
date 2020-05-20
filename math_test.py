"""

Basic arithmetic test

"""

import random


def main(numberOfQuestions=10, student_name=input()):
    correct_answers = 0  # Keep track of correct answers

    for question_number in range(0, numberOfQuestions):  # Repeat x many times for number of questions

        numbers = sorted([random.randint(1, 10) for _ in range(0, 2)],
                         reverse=True)  # Create an array with 2 random numbers for the equation

        operation = random.randint(0, 1)  # Create a random number, 0 == addition and 1 == subtraction

        print(numbers[0], ''.join(['-' if num == '1' else '+' for num in str(operation)]), numbers[1])  # Display question

        if operation == 0:  # Addition

            if int(input()) == numbers[0] + numbers[1]:
                correct_answers += 1

        else:  # Subtraction

            if int(input()) == numbers[0] - numbers[1]:
                correct_answers += 1

    print(
        ''.join(student_name + ', ' + str(correct_answers) + ' out of ' + str(numberOfQuestions)))  # Print test results

    return correct_answers


if __name__ == "__main__":
    main()
