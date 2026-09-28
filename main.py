import os
import time
import random
import json
import math
from datetime import datetime
import fraction

# Note: alternate_numbers import is commented out to ensure the script runs standalone. 
# Uncomment it if you have the 'alternate_numbers.py' file in the same folder.
# import alternate_numbers as an

RECORDS_FILE = "math_records.json"

# Enable ANSI escape sequences on Windows
if os.name == 'nt':
    os.system('')

class Colors:
    """ANSI color codes for beautiful terminal UI."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_console(title):
    """Clears the console and prints a beautifully formatted title."""
    os.system('cls' if os.name == 'nt' else 'clear')
    border = "=" * (len(title) + 8)
    print(f"{Colors.HEADER}{Colors.BOLD}{border}")
    print(f"   {title}   ")
    print(f"{border}{Colors.RESET}\n")

def input_digit(prompt):
    """
    Safely gets an integer input from the user. 
    Returns 'QUIT' if the user wants to exit.
    """
    while True:
        val = input(prompt).strip()
        
        if val.lower() == 'q': 
            return "QUIT"
            
        if val.lstrip('-').isdigit():
            return int(val)
            
        print(f"   {Colors.RED}❌ '{val}' is not a valid number. Enter a number or 'q' to quit.{Colors.RESET}")

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
        
    now = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    records[category].append({"date": now, "time": round(time_taken, 2)})
    records[category] = sorted(records[category], key=lambda x: x['time'])
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
    
    if category not in records or not records[category]:
        print(f"   {Colors.YELLOW}Difficulty: Baseline (10-99) - Unranked{Colors.RESET}")
        return 10, 99
    
    best_time = records[category][0]['time']
    tpq = best_time / count
    
    if tpq <= 3.0:
        print(f"   {Colors.RED}Difficulty: Expert (60-99) - Best Speed: {tpq:.1f}s/q{Colors.RESET}")
        return 60, 99
    elif tpq <= 5.0:
        print(f"   {Colors.YELLOW}Difficulty: Hard (40-99) - Best Speed: {tpq:.1f}s/q{Colors.RESET}")
        return 40, 99
    elif tpq <= 8.0:
        print(f"   {Colors.BLUE}Difficulty: Medium (20-79) - Best Speed: {tpq:.1f}s/q{Colors.RESET}")
        return 20, 79
    else:
        print(f"   {Colors.GREEN}Difficulty: Easy (10-49) - Best Speed: {tpq:.1f}s/q{Colors.RESET}")
        return 10, 49

def practice_logic(mode, start=None, end=None, count=None, reps=3, digits=None):
    """
    Unified logic for Tables, Squares, Cubes, Arithmetic, and Square Roots.
    Tracks time and saves performance upon successful completion.
    """
    score = 0
    wrong = 0
    practice_items = []
    counts = {}
    min_val, max_val = 10, 99 
    
    # 1. Setup specific configurations based on the chosen mode
    if mode == 1:
        category = f"Tables_{start}_to_{end}_{reps}reps"
        for n in range(start, end + 1):
            for m in range(2, 10):
                practice_items.append((n, m))
        counts = {item: 0 for item in practice_items}
        title = "Random Table Practice"
        
    elif mode == 2:
        category = f"Squares_{start}_to_{end}_{reps}reps"
        for n in range(start, end + 1):
            practice_items.append((n,))
        counts = {item: 0 for item in practice_items}
        title = "Random Square Practice"
        
    elif mode == 3:
        category = f"Cubes_{start}_to_{end}_{reps}reps"
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
        
    elif mode == 7:
        category = f"SquareRoot_{digits}Digits_{count}Qs"
        title = f"Square Root Practice ({digits}-Digit Perfect Squares)"
        # Calculate root boundaries for the specific number of digits of the perfect square
        min_sq = 10**(digits - 1) if digits > 1 else 0
        max_sq = (10**digits) - 1
        min_val = math.ceil(math.sqrt(min_sq))
        max_val = math.floor(math.sqrt(max_sq))
        # Edge case safeguard
        if min_val > max_val: min_val, max_val = 1, 3

    clear_console(title)
    
    # Load adaptive bounds for Arithmetic modes
    if mode in [4, 5, 6]:
        min_val, max_val = get_adaptive_bounds(category, count)
        
    print(f"   {Colors.BOLD}(Enter 'q' at any time to return to menu){Colors.RESET}\n")

    start_time = time.time()
    completed = False
    questions_done = 0

    # 2. Main Question Loop
    while True:
        if mode in [1, 2, 3]:
            available_items = [item for item, c in counts.items() if c < reps]
            if not available_items:
                completed = True
                break
                
            current_item = random.choice(available_items)
            num = current_item[0]
            
            if mode == 1:
                multiplier = current_item[1]
                correct_ans = num * multiplier
                prompt = f"   {Colors.CYAN}{num} x {multiplier} = {Colors.RESET}"
            elif mode == 2:
                correct_ans = num ** 2
                prompt = f"   {Colors.CYAN}{num}² = {Colors.RESET}"
            else:
                correct_ans = num ** 3
                prompt = f"   {Colors.CYAN}{num}³ = {Colors.RESET}"
        
        else: # Modes 4, 5, 6 (Arithmetic) and 7 (Roots)
            if questions_done >= count:
                completed = True
                break
            
            if mode == 7:
                correct_ans = random.randint(min_val, max_val)
                perfect_square = correct_ans ** 2
                prompt = f"   {Colors.CYAN}√{perfect_square} = {Colors.RESET}"
            else:
                n1 = random.randint(min_val, max_val)
                n2 = random.randint(min_val, max_val)
                
                if mode == 4:
                    correct_ans = n1 + n2
                    prompt = f"   {Colors.CYAN}{n1} + {n2} = {Colors.RESET}"
                elif mode == 5:
                    if n1 < n2: n1, n2 = n2, n1 
                    correct_ans = n1 - n2
                    prompt = f"   {Colors.CYAN}{n1} - {n2} = {Colors.RESET}"
                elif mode == 6:
                    correct_ans = n1 * n2
                    prompt = f"   {Colors.CYAN}{n1} x {n2} = {Colors.RESET}"

        # 3. Process User Input
        user_ans = input_digit(prompt)

        if user_ans == "QUIT":
            break

        if user_ans == correct_ans:
            score += 1
            if mode in [1, 2, 3]:
                counts[current_item] += 1
                print(f"   {Colors.GREEN}✅ Correct!{Colors.RESET} (Progress: {counts[current_item]}/{reps}) Score: {score}")
            else:
                questions_done += 1
                print(f"   {Colors.GREEN}✅ Correct!{Colors.RESET} (Progress: {questions_done}/{count}) Score: {score}")
        else:
            wrong += 1
            print(f"   {Colors.RED}❌ Wrong! Correct answer: {correct_ans}.{Colors.RESET} Mistakes: {wrong}/3")

        if wrong >= 3:
            print(f"\n   {Colors.RED}{Colors.BOLD}Too many mistakes! Let's review and try again.{Colors.RESET}")
            break

    # 4. Handle Session End & Record Keeping
    end_time = time.time()
    time_taken = end_time - start_time

    if completed:
        print(f"\n   {Colors.GREEN}{Colors.BOLD}🏆 Goal Reached! Set completed in {time_taken:.2f} seconds.{Colors.RESET}")
        
        top_records = save_record(category, time_taken)
        
        print(f"\n   {Colors.BLUE}--- Top 5 Records for '{category}' ---{Colors.RESET}")
        for i, rec in enumerate(top_records, 1):
            print(f"   {Colors.BOLD}{i}.{Colors.RESET} Date: {rec['date']} | Time: {Colors.YELLOW}{rec['time']}s{Colors.RESET}")
            
        input(f"\n   {Colors.BOLD}Press Enter to return to menu...{Colors.RESET}")
    else:
        print(f"\n   {Colors.YELLOW}Practice stopped. Final Score: {score}. Returning to menu...{Colors.RESET}")
        time.sleep(3)

def write_table():
    """Generates and prints a complete specific multiplication table."""
    num = input_digit(f"   {Colors.CYAN}Enter table number: {Colors.RESET}")
    if num == "QUIT": return
    clear_console(f"Table of {num}")
    for i in range(1, 11):
        print(f"   {Colors.BOLD}{num} x {i:<2}{Colors.RESET} = {Colors.GREEN}{num * i}{Colors.RESET}")
    input(f"\n   {Colors.BOLD}Press Enter to return to menu...{Colors.RESET}")

def main():
    while True:
        clear_console("Math Practice Main Menu")
        print(f"   {Colors.CYAN}1:{Colors.RESET} Practice Tables (2-9)")
        print(f"   {Colors.CYAN}2:{Colors.RESET} Write a Specific Table")
        print(f"   {Colors.CYAN}3:{Colors.RESET} Practice Squares")
        print(f"   {Colors.CYAN}4:{Colors.RESET} Practice Cubes")
        print(f"   {Colors.CYAN}5:{Colors.RESET} Practice 2-Digit Addition")
        print(f"   {Colors.CYAN}6:{Colors.RESET} Practice 2-Digit Subtraction")
        print(f"   {Colors.CYAN}7:{Colors.RESET} Practice 2-Digit Multiplication")
        print(f"   {Colors.CYAN}8:{Colors.RESET} Alternate Tables")
        print(f"   {Colors.CYAN}9:{Colors.RESET} Practice Fractions")
        print(f"  {Colors.CYAN}10:{Colors.RESET} Practice Square Roots")
        print(f"   {Colors.RED}0:{Colors.RESET} Quit")

        choice = input_digit(f"\n   {Colors.BOLD}Select option: {Colors.RESET}")

        if choice == "QUIT" or choice == 0:
            print(f"   {Colors.GREEN}Keep practicing! Goodbye.{Colors.RESET}")
            break
            
        elif choice == 8:
            try:
                import alternate_numbers as an
                an.multiplication_practice()
            except ImportError:
                print(f"   {Colors.RED}❌ 'alternate_numbers.py' not found. Please check your files.{Colors.RESET}")
                time.sleep(2)
                
        elif choice == 9:
            try:
                fraction.run_quiz()
            except NameError:
                print(f"   {Colors.RED}❌ 'fraction' module not loaded. Please check your files.{Colors.RESET}")
                time.sleep(2)
                
        elif choice == 2:
            write_table()
            
        elif choice in [1, 3, 4]:
            start = input_digit(f"   {Colors.YELLOW}Enter start of range: {Colors.RESET}")
            if start == "QUIT": continue
            end = input_digit(f"   {Colors.YELLOW}Enter end of range: {Colors.RESET}")
            if end == "QUIT": continue
                
            if start > end:
                print(f"   {Colors.RED}Error: Start number must be less than end number.{Colors.RESET}")
                time.sleep(2)
                continue
                
            reps = input_digit(f"   {Colors.YELLOW}How many times to practice each item? {Colors.RESET}")
            if reps == "QUIT": continue
            
            if reps <= 0:
                print(f"   {Colors.RED}Error: You must practice at least 1 time.{Colors.RESET}")
                time.sleep(2)
                continue
            
            # Map menu choice to logic mode
            mode = 1 if choice == 1 else (2 if choice == 3 else 3)
            practice_logic(mode, start=start, end=end, reps=reps)
            
        elif choice in [5, 6, 7]:
            count = input_digit(f"   {Colors.YELLOW}How many questions in this set? {Colors.RESET}")
            if count == "QUIT": continue
                
            if count <= 0:
                print(f"   {Colors.RED}Error: You must practice at least 1 question.{Colors.RESET}")
                time.sleep(2)
                continue
            
            # Map menu choice to logic mode
            mode = 4 if choice == 5 else (5 if choice == 6 else 6)
            practice_logic(mode, count=count)

        elif choice == 10:
            digits = input_digit(f"   {Colors.YELLOW}Digits in the perfect square (e.g., 2, 3, 4): {Colors.RESET}")
            if digits == "QUIT": continue
            
            if digits <= 0:
                print(f"   {Colors.RED}Error: Number of digits must be at least 1.{Colors.RESET}")
                time.sleep(2)
                continue
                
            count = input_digit(f"   {Colors.YELLOW}How many questions in this set? {Colors.RESET}")
            if count == "QUIT": continue
            
            if count <= 0:
                print(f"   {Colors.RED}Error: You must practice at least 1 question.{Colors.RESET}")
                time.sleep(2)
                continue
            
            practice_logic(mode=7, digits=digits, count=count)

        else:
            print(f"   {Colors.RED}Invalid selection.{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
    