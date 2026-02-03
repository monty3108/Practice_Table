# from random import randint
# from gen_func import input_digit, clear_console
# import os
# import time
#
# def practice_random():
#     score = 0
#     wrong = 0
#     print("For exit enter 0.")
#     start_table = input_digit("Enter start table number to practice : ")
#     end_table = input_digit("Enter last table number to practice: ")
#     active_selection = "Random Table Practice"
#     clear_console(active_selection)
#     no_of_rows = 0
#     while True:
#         no_of_rows += 1
#         table = randint(start_table,end_table)
#         num = randint(2,9)
#         ans = input_digit(f"   {table} x {num} = ")
#         if ans==(table * num):
#             score += 1
#             print(f'  Good. Score: {score} ')
#         else:
#             wrong +=1
#             print(f'   correct ans: {num * table}. Wrong ans: {wrong} ')
#
#         if ans ==0 or wrong == 3:
#             print(f"  Exited. Score: {score} ")
#             print('   Exiting.....')
#             time.sleep(5)
#             break
#
#         if no_of_rows > 10:
#             no_of_rows = 0
#             print('   screen clear activated')
#             time.sleep(1)
#
#             clear_console(active_selection)
# # practice_random()

from random import randint
from gen_func import input_digit, clear_console
import os
import time


def practice_random():
    score = 0
    wrong = 0
    last_table = None  # Track the previous table number

    print("For exit enter 0.")
    start_table = input_digit("Enter start table number to practice : ")
    end_table = input_digit("Enter last table number to practice: ")
    active_selection = "Random Table Practice"
    clear_console(active_selection)

    no_of_rows = 0
    while True:
        no_of_rows += 1

        # 1. Generate a new table number
        table = randint(start_table, end_table)

        # 2. If it's the same as the last one (and we have more than one option), try again
        # We check (end_table > start_table) to avoid an infinite loop if the range is only 1 number
        if end_table > start_table:
            while table == last_table:
                table = randint(start_table, end_table)

        # Update last_table for the next iteration
        last_table = table

        num = randint(2, 9)
        ans = input_digit(f"   {table} x {num} = ")

        # Exit condition: user enters 0
        if ans == 0:
            print(f"  Exited. Score: {score} ")
            break

        if ans == (table * num):
            score += 1
            print(f'  Good. Score: {score} ')
        else:
            wrong += 1
            print(f'   correct ans: {num * table}. Wrong ans: {wrong} ')

        # Game over condition: 3 mistakes
        if wrong == 3:
            print(f"  Exited. Score: {score} ")
            print('   Exiting.....')
            time.sleep(5)
            break

        if no_of_rows > 10:
            no_of_rows = 0
            print('   screen clear activated')
            time.sleep(1)
            clear_console(active_selection)

# practice_random()