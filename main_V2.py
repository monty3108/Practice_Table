import os
import time
import random
import json
from datetime import datetime
import fraction

# Note: alternate_numbers import is commented out to ensure the script runs standalone. 
# Uncomment it if you have the 'alternate_numbers.py' file in the same folder.
# import alternate_numbers as an

RECORDS_FILE = "math_records.json"

def clear_console(title):
    """Clears the console and prints the current menu/practice title."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"--- {title} ---\n")

def input_digit(prompt):
    """
    Safely gets an integer input from the user. 
    Returns 'QUIT' if the user wants to exit.
    """
    while True:
        val = input(prompt).strip()
        
        if val.lower() == 'q': 
            return "QUIT"
            
        # lstrip('-') allows negative numbers to pass the isdigit() check just in case
        if val.lstrip('-').isdigit():
            return int(val)
            
        print(f"   '{val}' is not a valid number. Enter a number or 'q' to quit.")

def load_records():
    """Loads the performance records from a JSON file."""
    if os.path.exists(RECORDS_FILE):
        try:
            with open(RECORDS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_record(category, time_taken):
    """
    Saves a new performance record, sorts the category by fastest time, 
    and keeps only the top 5 records.
    """
    records = load_records()
    if category not in records:
        records[category] = []
        
    # Append the new record with the current date
    now = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    records[category].append({"date": now, "time": round(time_taken, 2)})
    
    # Sort the list so the lowest (fastest) time is at the top
    records[category] = sorted(records[category], key=lambda x: x['time'])
    
    # Slice to keep only the top 5 fastest records
    records[category] = records[category][:5]
    
    with open(RECORDS_FILE, 'w') as f:
        json.dump(records, f, indent=4)
        
    return records[category]

def get_adaptive_bounds(category, count):
    """
    Determines the difficulty range of 2-digit numbers based on the user's
    fastest completion time for the current category.
    """
    records = load_records()
    
    # If no records exist for this exact set, use the full 10-99 baseline
    if category not in records or not records[category]:
        print("   Difficulty: Baseline (10-99) - Unranked")
        return 10, 99
    
    # Grab the fastest time (index 0) and calculate Time Per Question (TPQ)
    best_time = records[category][0]['time']
    tpq = best_time / count
    
    if tpq <= 3.0:
        print(f"   Difficulty: Expert (60-99) - Best Speed: {tpq:.1f}s/q")
        return 60, 99
    elif tpq <= 5.0:
        print(f"   Difficulty: Hard (40-99) - Best Speed: {tpq:.1f}s/q")
        return 40, 99
    elif tpq <= 8.0:
        print(f"   Difficulty: Medium (20-79) - Best Speed: {tpq:.1f}s/q")
        return 20, 79
    else:
        print(f"   Difficulty: Easy (10-49) - Best Speed: {tpq:.1f}s/q")
        return 10, 49

def practice_logic(mode, start=None, end=None, count=None):
    """
    Unified logic for Tables, Squares, Cubes, and 2-Digit Arithmetic.
    Tracks time and saves performance upon successful completion.
    """
    score = 0
    wrong = 0
    practice_items = []
    counts = {}
    min_val, max_val = 10, 99 # Default bounds for arithmetic
    
    # 1. Setup specific configurations based on the chosen mode
    if mode == 1:
        category = f"Tables_{start}_to_{end}"
        for n in range(start, end + 1):
            for m in range(2, 10):
                practice_items.append((n, m))
        counts = {item: 0 for item in practice_items}
        title = "Random Table Practice"
        
    elif mode == 2:
        category = f"Squares_{start}_to_{end}"
        for n in range(start, end + 1):
            practice_items.append((n,))
        counts = {item: 0 for item in practice_items}
        title = "Random Square Practice"
        
    elif mode == 3:
        category = f"Cubes_{start}_to_{end}"
        for n in range(start, end + 1):
            practice_items.append((n,))
        counts = {item: 0 for item in practice_items}
        title = "Random Cube Practice"
        
    elif mode == 4:
        category = f"Addition_2Digit_{count}Qs"
        title = "2-Digit Addition Practice"
        
    elif mode == 5:
        category = f"Subtraction_2Digit_{count}Qs"
        title = "2-Digit Subtraction Practice"
        
    elif mode == 6:
        category = f"Multiplication_2Digit_{count}Qs"
        title = "2-Digit Multiplication Practice"

    clear_console(title)
    
    # Load adaptive bounds for Arithmetic modes and print the difficulty status
    if mode in [4, 5, 6]:
        min_val, max_val = get_adaptive_bounds(category, count)
        
    print("   (Enter 'q' at any time to return to menu)\n")

    start_time = time.time()
    completed = False
    questions_done = 0

    # 2. Main Question Loop
    while True:
        # Determine the next question based on range modes vs counting modes
        if mode in [1, 2, 3]:
            # Filter items that haven't reached 3 correct answers yet
            available_items = [item for item, c in counts.items() if c < 3]
            if not available_items:
                completed = True
                break
                
            current_item = random.choice(available_items)
            num = current_item[0]
            
            if mode == 1:
                multiplier = current_item[1]
                correct_ans = num * multiplier
                prompt = f"   {num} x {multiplier} = "
            elif mode == 2:
                correct_ans = num ** 2
                prompt = f"   {num}² = "
            else:
                correct_ans = num ** 3
                prompt = f"   {num}³ = "
        
        else: # Modes 4, 5, 6 (Arithmetic)
            if questions_done >= count:
                completed = True
                break
                
            # Generate numbers using the adaptive bounds
            n1 = random.randint(min_val, max_val)
            n2 = random.randint(min_val, max_val)
            
            if mode == 4:
                correct_ans = n1 + n2
                prompt = f"   {n1} + {n2} = "
            elif mode == 5:
                # Ensure the first number is larger to avoid negative answers for practice
                if n1 < n2: 
                    n1, n2 = n2, n1 
                correct_ans = n1 - n2
                prompt = f"   {n1} - {n2} = "
            elif mode == 6:
                correct_ans = n1 * n2
                prompt = f"   {n1} x {n2} = "

        # 3. Process User Input
        user_ans = input_digit(prompt)

        if user_ans == "QUIT":
            break

        if user_ans == correct_ans:
            score += 1
            if mode in [1, 2, 3]:
                counts[current_item] += 1
                print(f"   Correct! (Progress: {counts[current_item]}/3) Score: {score}")
            else:
                questions_done += 1
                print(f"   Correct! (Progress: {questions_done}/{count}) Score: {score}")
        else:
            wrong += 1
            print(f"   Wrong! Correct answer: {correct_ans}. Mistakes: {wrong}/3")

        if wrong >= 3:
            print("\n   Too many mistakes! Let's review and try again.")
            break

    # 4. Handle Session End & Record Keeping
    end_time = time.time()
    time_taken = end_time - start_time

    if completed:
        print(f"\n   Goal Reached! Set completed in {time_taken:.2f} seconds.")
        
        # Save and retrieve the top 5 records
        top_records = save_record(category, time_taken)
        
        print(f"\n   --- Top 5 Records for '{category}' ---")
        for i, rec in enumerate(top_records, 1):
            print(f"   {i}. Date: {rec['date']} | Time: {rec['time']}s")
            
        input("\n   Press Enter to return to menu...")
    else:
        print(f"\n   Practice stopped. Final Score: {score}. Returning to menu...")
        time.sleep(3)

def write_table():
    """Generates and prints a complete specific multiplication table."""
    num = input_digit("   Enter table number: ")
    if num == "QUIT": return
    clear_console(f"Table of {num}")
    for i in range(1, 11):
        print(f"   {num} x {i} = {num * i}")
    input("\n   Press Enter to return to menu...")

def main():
    while True:
        clear_console("Math Practice Main Menu")
        print("   1: Practice Tables (2-9)")
        print("   2: Write a Specific Table")
        print("   3: Practice Squares")
        print("   4: Practice Cubes")
        print("   5: Practice 2-Digit Addition")
        print("   6: Practice 2-Digit Subtraction")
        print("   7: Practice 2-Digit Multiplication")
        print("   8: Alternate Tables")
        print("   9: Practice Fractions")
        print("   0: Quit")

        choice = input_digit("\n   Select option: ")

        if choice == "QUIT" or choice == 0:
            print("   Keep practicing! Goodbye.")
            break
            
        elif choice == 8:
            try:
                import alternate_numbers as an
                an.multiplication_practice()
            except ImportError:
                print("   'alternate_numbers.py' not found. Please check your files.")
                time.sleep(2)
                
        elif choice == 9:
            try:
                fraction.run_quiz()
            except NameError:
                print("   'fraction' module not loaded. Please check your files.")
                time.sleep(2)
                
        elif choice == 2:
            write_table()
            
        elif choice in [1, 3, 4]:
            start = input_digit("   Enter start of range: ")
            end = input_digit("   Enter end of range: ")
            
            if start == "QUIT" or end == "QUIT":
                continue
                
            if start > end:
                print("   Error: Start number must be less than end number.")
                time.sleep(2)
                continue
            
            # Map menu choice to logic mode
            mode = 1 if choice == 1 else (2 if choice == 3 else 3)
            practice_logic(mode, start=start, end=end)
            
        elif choice in [5, 6, 7]:
            count = input_digit("   How many questions in this set? ")
            if count == "QUIT":
                continue
                
            if count <= 0:
                print("   Error: You must practice at least 1 question.")
                time.sleep(2)
                continue
            
            # Map menu choice to logic mode
            mode = 4 if choice == 5 else (5 if choice == 6 else 6)
            practice_logic(mode, count=count)

        else:
            print("   Invalid selection.")
            time.sleep(1)

if __name__ == "__main__":
    main()
    