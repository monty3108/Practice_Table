import os

def active(active_selection: str):
  print(f"   {active_selection} ")

def clear_console(active_selection: str):
  """Clears the console."""
  os.system('cls' if os.name == 'nt' else 'clear')
  active(active_selection)

def input_digit(display_text: str):
    enter_digit = input(display_text)
    if enter_digit.isdigit():
        return int(enter_digit)
    else:
        print(f"   {enter_digit} is not a digit. Try again")
        return input_digit(display_text)