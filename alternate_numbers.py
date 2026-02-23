import os
import time

def clear_screen():
    # Clears the terminal screen based on the Operating System
    # 'nt' is for Windows, 'posix' is for macOS and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def multiplication_practice():
    print("--- Welcome to Alternate Multiplication Practice ---")
    print("Instructions: Enter your answer, or type 'q' to quit at any time.\n")

    try:
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    question_count = 0
    
    # We use a step of 4 to get pairs like (2,3), then (6,7), then (10,11)
    # Or a custom logic to match your example: 2x3, 4x5, 8x9, 12x13
    # Let's use a flexible loop to generate these pairs:
    current = start
    while current <= end:
        num1 = current
        num2 = current + 1
        correct_ans = num1 * num2

        # Increment question counter
        question_count += 1

        # Logic to clear screen every 10 answers
        if question_count > 1 and (question_count - 1) % 10 == 0:
            print("\n10 questions reached! Clearing screen in 2 seconds...")
            time.sleep(2)
            clear_screen()

        # Prompt the user
        user_input = input(f"Q{question_count}: What is {num1} x {num2} = ")

        # Exit mechanism
        if user_input.lower() in ['q', 'exit', 'quit', '0']:
            print("Thanks for practicing! Goodbye.")
            break

        # Check answer
        try:
            if int(user_input) == correct_ans:
                print("Correct! ✅")
            else:
                print(f"Wrong! ❌ The correct answer was {correct_ans}")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

        # Update 'current' to get the next alternate pair
        # Adding 2 moves from (2,3) to (4,5).
        current += 1

    print("\nPractice session complete!")

if __name__ == "__main__":
    multiplication_practice()
    