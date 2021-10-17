def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print('Please, remind me your name.')
    your_name = input()
    print(f"What a great name you have, {your_name}!")


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder3, remainder5, remainder7 = int(input()), int(input()), int(input())
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {your_age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    number_to_count = int(input())
    counter = 0
    while counter <= number_to_count:
        print(f"{counter}!")
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    # method_test = "Why do we use methods?"
    # method_question_one = "1. To repeat a statement multiple times."
    # method_question_two = "2. To decompose a program into several small subroutines."
    # method_question_three = "3. To determine the execution time of a program."
    # method_question_four = "4. To interrupt the execution of a program."
    # print(method_test)
    # print(method_question_one)
    # print(method_question_two)
    # print(method_question_three)
    # print(method_question_four)
    # was thinking on to include and mix questions later,
    # that is why the variables, but a simpler solution is below:
    print("Let's test your programming knowledge.",
          "Why do we use methods?",
          "1. To repeat a statement multiple times.",
          "2. To decompose a program into several small subroutines.",
          "3. To determine the execution time of a program.",
          "4. To interrupt the execution of a program.", sep='\n')
    method_answer = int(input())
    correct_method_answer = 2
    # while True:
    #     if method_answer == correct_method_answer:
    #         print("Completed, have a nice day!")
    #         break
    #     else:
    #         print("Please, try again.")
    #         method_answer = int(input())
# OORRRRRRRR (adopted it from another student's solution)
    while method_answer != correct_method_answer:
        print("Please, try again.")
        method_answer = int(input())

    print("Completed, have a nice day!")


def end():
    print('Congratulations, have a nice day!')

greet('BotPal', '2021')
remind_name()
guess_age()
count()
test()
end()