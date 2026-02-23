# Table Practice 


import individual_table_practice as t1
import random_table as t2
import sq_cu as t3
import alternate_numbers as t4
from gen_func import input_digit, clear_console

while True:
    active_selection = 'Table practice Main Menu:'
    clear_console(active_selection)
    print("   Select Options....\n"
          "   1: Practice table\n"
          "   2: Write table\n"
          "   3: Practice random tables\n"
          "   4: Practice random squares\n"
          "   5: Practice random cubes\n"
          "   6: Alternate Multiplication \n"
          "   0: Quit table practice")

    select_option = input_digit('   Enter your option: ')
    if select_option == 1:
        t1.input_table_to_practice()
    elif select_option == 2:
        t1.write_table()
    elif select_option == 3:
        t2.practice_random()
    elif select_option == 4:
        t3.practice_sq() 
    elif select_option == 5:
        t3.practice_cube() 
    elif select_option == 6:
        t4.multiplication_practice() 
        
    else:
        break