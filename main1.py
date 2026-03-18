import os
import time
import random
import alternate_numbers as an

def clear_console(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- {title} ---\n")


def input_digit(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        print(f"   '{val}' is not a digit. Try again.")


def practice_logic(mode, start, end):
    """
    Unified logic for Tables, Squares, and Cubes.
    mode: 1 (Table), 2 (Square), 3 (Cube)
    """
    score = 0
    wrong = 0
    # Track how many times each number in the range has appeared
    counts = {num: 0 for num in range(start, end + 1)}
    title = ["Random Table", "Random Square", "Random Cube"][mode - 1]
    clear_console(f"{title} Practice")

    while True:
        # Filter numbers that haven't appeared 3 times yet
        available_nums = [n for n, count in counts.items() if count < 3]

        if not available_nums:
            print("\n   All numbers occurred 3 times. Maximum reached!")
            break

        current_num = random.choice(available_nums)
        counts[current_num] += 1

        # Determine the question and answer based on mode
        if mode == 1:  # Table
            multiplier = random.randint(2, 9)
            correct_ans = current_num * multiplier
            prompt = f"   {current_num} x {multiplier} = "
        elif mode == 2:  # Square
            correct_ans = current_num ** 2
            prompt = f"   {current_num}² = "
        else:  # Cube
            correct_ans = current_num ** 3
            prompt = f"   Cube of {current_num} = "

        user_ans = input_digit(prompt)

        if user_ans == 0:
            break

        if user_ans == correct_ans:
            score += 1
            print(f"   Correct! Score: {score}")
        else:
            wrong += 1
            print(f"   Wrong! Correct answer: {correct_ans}. Mistakes: {wrong}/3")

        if wrong >= 3:
            print("\n   Too many mistakes!")
            break

    print(f"   Final Score: {score}. Returning to menu...")
    time.sleep(3)


def write_table():
    num = input_digit("   Enter table number: ")
    clear_console(f"Table of {num}")
    for i in range(1, 11):
        print(f"   {num} x {i} = {num * i}")
    input("\n   Press Enter to return to menu...")


def main():
    while True:
        clear_console("Table Practice Main Menu")
        print("   1: Practice Tables\n   2: Write a Table\n   3: Practice Squares\n   4: Practice Cubes\n"
              "   5: Alternate Tables\n   0: Quit")

        choice = input_digit("\n   Select option: ")

        if choice == 0:
            print("   Goodbye!")
            break
        elif choice == 5:
            an.multiplication_practice()


        elif choice == 2:
            write_table()
            continue
        elif choice in [1, 3, 4]:
            start = input_digit("   Enter start number: ")
            end = input_digit("   Enter end number: ")
            # Map choice to mode (1=Table, 3=Square->mode 2, 4=Cube->mode 3)
            mode = 1 if choice == 1 else (2 if choice == 3 else 3)
            practice_logic(mode, start, end)
        else:
            print("   Invalid selection.")
            time.sleep(1)


if __name__ == "__main__":
    main()