import random

correct_answer = 0
for count in range(1, 3):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print('How much is', number1 , 'times', number2, '?')
    answer = input()
    answer_int = int(answer) 
    calculate = number1 * number2
    if answer_int == calculate:
        correct_answer = correct_answer + 1
print('your correct answers are:', correct_answer)


