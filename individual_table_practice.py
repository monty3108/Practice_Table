# Individual Table Practice
from gen_func import input_digit, clear_console
import time

def write_table():
    i = 1
    j = 10

    table = input_digit("   Enter table number:")
    clear_console(f'Table of {table} :- \n')
    for x in range(1, 11):
        print(f"   {table} x {x} = {(table) * x} ")

    exit = input('   enter anything to exit: ')


def practice_table(table: int):

    i = 1
    while i < 11:
        ans = i * table
        product = input_digit(f"   {table} x {i} = ")

        if ans == int(product):
            print("   Correct answer ")
        else:
            print(f"   Correct answer is {ans}")
        i += 1
    print('   Exiting...')
    time.sleep(3)

def input_table_to_practice():
    active_selection = "Individual Table Practice"
    clear_console(active_selection)
    table_to_practice = input_digit("Enter Table to practice: ")
    practice_table(table_to_practice)

