from random import randint
from gen_func import input_digit, clear_console
import os
import time

def practice_sq():
    score = 0
    wrong = 0
    print("For exit enter 0.")
    start_table = input_digit("Enter start number to practice : ")
    end_table = input_digit("Enter last number to practice: ")
    active_selection = "Random Square Practice"
    clear_console(active_selection)
    no_of_rows = 0
    while True:
        no_of_rows += 1
        table = randint(start_table,end_table)
        #num = randint(2,9)
        ans = input_digit(f"   {table} x {table} = ")
        if ans==(table * table):
            score += 1
            print(f'  Good. Score: {score} ')
        else:
            wrong +=1
            print(f'   correct ans: {table * table}. Wrong ans: {wrong} ')

        if ans ==0 or wrong == 3:
            print(f"  Exited. Score: {score} ")
            print('   Exiting.....')
            time.sleep(5)
            break

        if no_of_rows > 10:
            no_of_rows = 0
            print('   screen clear activated') 
            time.sleep(1)
            
            clear_console(active_selection)

def practice_cube():
    score = 0
    wrong = 0
    print("For exit enter 0.")
    start_table = input_digit("Enter start number to practice : ")
    end_table = input_digit("Enter last number to practice: ")
    active_selection = "Random Cube Practice"
    clear_console(active_selection)
    no_of_rows = 0
    while True:
        no_of_rows += 1
        table = randint(start_table,end_table)
        #num = randint(2,9)
        ans = input_digit(f"   Cube of {table} = ")
        if ans==(table * table*table):
            score += 1
            print(f'  Good. Score: {score} ')
        else:
            wrong +=1
            print(f'   correct ans: {table*table * table}. Wrong ans: {wrong} ')

        if ans ==0 or wrong == 3:
            print(f"  Exited. Score: {score} ")
            print('   Exiting.....')
            time.sleep(5)
            break

        if no_of_rows > 10:
            no_of_rows = 0
            print('   screen clear activated') 
            time.sleep(1)
            
            clear_console(active_selection)
#practice_cube() 