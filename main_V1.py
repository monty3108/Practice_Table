import os
import time
import random
import fraction

# Note: alternate_numbers import is commented out to ensure the script runs standalone. 
# Uncomment it if you have the 'alternate_numbers.py' file in the same folder.
# import alternate_numbers as an

def clear_console(title):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- {title} ---\n")

def input_digit(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():
            return int(val)
        if val.lower() == 'q': # Quick exit option
            return 0
        print(f"   '{val}' is not a digit. Try again.")

def practice_logic(mode, start, end):
    """
    Unified logic for Tables, Squares, and Cubes.
    Tracks unique pairs/items to ensure each is answered correctly 3 times.
    """
    score = 0
    wrong = 0
    
    # 1. Generate the list of items to practice based on the mode
    practice_items = []
    if mode == 1: # Tables
        # Creates a list of tuples: (number, multiplier)
        for n in range(start, end + 1):
            for m in range(2, 10): # Standard practice: multipliers 2 to 9
                practice_items.append((n, m))
    else: # Squares or Cubes
        # Creates a list of single-item tuples: (number,)
        for n in range(start, end + 1):
            practice_items.append((n,))

    # 2. Initialize the frequency tracker for each item
    # This ensures every specific multiplication pair is tracked separately.
    counts = {item: 0 for item in practice_items}
    
    title_map = {1: "Random Table", 2: "Random Square", 3: "Random Cube"}
    clear_console(f"{title_map[mode]} Practice")
    print("   (Enter '0' or 'q' at any time to return to menu)\n")

    while True:
        # Filter items that haven't reached 3 correct answers yet
        available_items = [item for item, count in counts.items() if count < 3]

        if not available_items:
            print("\n   Goal Reached! All items practiced 3 times.")
            break

        # Select a random pair or number from the remaining list
        current_item = random.choice(available_items)
        num = current_item[0]

        # 3. Define question and answer based on the mode
        if mode == 1:
            multiplier = current_item[1]
            correct_ans = num * multiplier
            prompt = f"   {num} x {multiplier} = "
        elif mode == 2:
            correct_ans = num ** 2
            prompt = f"   {num}² = "
        else:
            correct_ans = num ** 3
            # Using superscript for the cube display
            prompt = f"   {num}³ = "

        user_ans = input_digit(prompt)

        if user_ans == 0:
            break

        if user_ans == correct_ans:
            score += 1
            counts[current_item] += 1
            print(f"   Correct! (Progress: {counts[current_item]}/3) Score: {score}")
        else:
            wrong += 1
            print(f"   Wrong! Correct answer: {correct_ans}. Mistakes: {wrong}/3")

        if wrong >= 3:
            print("\n   Too many mistakes! Let's review and try again.")
            break

    print(f"\n   Final Score: {score}. Returning to menu...")
    time.sleep(3)

def write_table():
    num = input_digit("   Enter table number: ")
    if num == 0: return
    clear_console(f"Table of {num}")
    for i in range(1, 11):
        print(f"   {num} x {i} = {num * i}")
    input("\n   Press Enter to return to menu...")

def main():
    while True:
        clear_console("Table Practice Main Menu")
        print("   1: Practice Tables (2-9)")
        print("   2: Write a Specific Table")
        print("   3: Practice Squares")
        print("   4: Practice Cubes")
        print("   5: Alternate Tables")
        print("   6: Practice Fractions")
        print("   0: Quit")

        choice = input_digit("\n   Select option: ")

        if choice == 0:
            print("   Keep practicing! Goodbye.")
            break
        elif choice == 5:
            try:
                import alternate_numbers as an
                an.multiplication_practice()
            except ImportError:
                print("   'alternate_numbers.py' not found. Please check your files.")
                time.sleep(2)
        elif choice == 2:
            write_table()
        elif choice in [1, 3, 4]:
            start = input_digit("   Enter start of range: ")
            end = input_digit("   Enter end of range: ")
            
            if start > end:
                print("   Error: Start number must be less than end number.")
                time.sleep(2)
                continue
            
            # Map menu choice to logic mode
            mode = 1 if choice == 1 else (2 if choice == 3 else 3)
            practice_logic(mode, start, end)
        elif choice == 6:
            fraction.run_quiz()

        else:
            print("   Invalid selection.")
            time.sleep(1)

if __name__ == "__main__":
    main()
    