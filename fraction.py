import os
import random
import time

# Data extracted from the Percentage Fraction table (Up to 1/25)
FRACTION_PERCENT_DATA = {
    "1/2": "50.00%", "1/3": "33.33%", "1/4": "25.00%", "1/5": "20.00%",
    "1/6": "16.67%", "1/7": "14.29%", "1/8": "12.50%", "1/9": "11.11%",
    "1/10": "10.00%", "1/11": "9.09%", "1/12": "8.33%", "1/13": "7.69%",
    "1/14": "7.14%", "1/15": "6.67%", "1/16": "6.25%", "1/17": "5.88%",
    "1/18": "5.56%", "1/19": "5.26%", "1/20": "5.00%", "1/21": "4.76%",
    "1/22": "4.55%", "1/23": "4.35%", "1/24": "4.17%", "1/25": "4.00%"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
    score = 0
    total = 0
    questions = list(FRACTION_PERCENT_DATA.keys())

    print("--- Vedic Math: Fraction to Percentage Practice (1/2 to 1/25) ---")
    print("Goal: Memorize the base conversions for speed math.")
    time.sleep(2)

    try:
        while True:
            clear_screen()
            # Pick a random fraction
            q_fraction = random.choice(questions)
            correct_perc = FRACTION_PERCENT_DATA[q_fraction]
            
            # Create MCQ options
            wrong_pool = [v for v in FRACTION_PERCENT_DATA.values() if v != correct_perc]
            options = random.sample(wrong_pool, 3) + [correct_perc]
            random.shuffle(options)

            print(f"Progress: {score}/{total} correct")
            print("=" * 40)
            print(f"CONVERT TO PERCENTAGE:  {q_fraction}")
            print("=" * 40)

            for i, opt in enumerate(options, 1):
                print(f"{i}) {opt}")

            start_time = time.time()
            choice = input("\nSelect (1-4) or 'q' to quit: ").strip().lower()

            if choice == 'q':
                break
            
            if choice.isdigit() and 1 <= int(choice) <= 4:
                selected = options[int(choice) - 1]
                if selected == correct_perc:
                    elapsed = round(time.time() - start_time, 2)
                    print(f"\n✨ CORRECT! Fast work ({elapsed}s)")
                    score += 1
                else:
                    print(f"\n❌ NOT QUITE. {q_fraction} is actually {correct_perc}")
            else:
                print("\n⚠️ Invalid input.")

            total += 1
            time.sleep(1.8)

    except KeyboardInterrupt:
        pass

    clear_screen()
    print("--- Session Summary ---")
    if total > 0:
        print(f"Final Score: {score}/{total} ({round(score/total*100, 1)}%)")
    print("Keep mastering those reciprocals!")

if __name__ == "__main__":
    run_quiz()
    