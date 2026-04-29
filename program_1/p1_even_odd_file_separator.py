import os
import time
import random
import sys

def slowtype(text, duration):
    delay = duration / len(text) if len(text) > 0 else 0
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_bar(label="", total=26, duration=2):
    for i in range(total + 1):
        bar = '▄' * i + ' ' * (total - i)
        percent = int((i / total) * 100)
        sys.stdout.write(f'\r{label}{bar} {percent}%')
        sys.stdout.flush()
        time.sleep(duration / total)
    print()

class EvenOddSeparator:
    def __init__(self, source_file, even_file, odd_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.even_file = os.path.join(base, even_file)
        self.odd_file = os.path.join(base, odd_file)

    def generate_numbers(self):
        while True:
            try:
                range_start = int(input("Enter range start: "))
                range_end = int(input("Enter range end: "))
                num_count = int(input("How many numbers to generate?: "))

                if range_start > range_end:
                    print("Range start must be less than or equal to range end.")
                    continue
                if num_count < 1:
                    print("Number count must be at least 1.")
                    continue
                if num_count > (range_end - range_start + 1):
                    print(f"Count exceeds available numbers in range. Max is {range_end - range_start + 1}.")
                    continue
                break

            except ValueError:
                print("Invalid input! Please enter a numerical value.")

        numbers = random.sample(range(range_start, range_end + 1), num_count)

        f = open(self.source_file, "w")
        for num in numbers:
            f.write(str(num) + "\n")
        f.close()

        print("Generated:", ", ".join(str(n) for n in numbers))

    def manual_input(self):
        numbers = []
        more = "y"  # ← ADD THIS BACK

        while more.lower() == "y":
            while True:
                try:
                    num = int(input("Enter a number: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole value.")
            more = input("Add more? (y/n): ")

        f = open(self.source_file, "w")
        for num in numbers:
            f.write(str(num) + "\n")
        f.close()

        print("Entered:", ", ".join(str(n) for n in numbers))

        print("Entered:", ", ".join(str(n) for n in numbers))  # ← ADDED: Preview output
        

    def choose_mode(self):
        while True:
            print("Select input mode:")
            print("  [1] Generate random numbers")
            print("  [2] Manual input")
            print("  [3] View/Overwrite built-in numbers (numbers.txt)")
            print("  [4] Exit")
            mode = input("Enter choice: ")

            if mode == "1":
                loading_bar("Loading number generator ")
                self.generate_numbers()
            elif mode == "2":
                loading_bar("Loading manual input mode ")
                self.manual_input()
            elif mode == "3":
                print("\nUsing built-in numbers.txt as input.")
                print("Warning! If you proceed, the current numbers.txt will be used and results will be overwritten.")
                confirm = input("Are you sure you want to proceed? (y/n): ")
                if confirm.lower() == "y":
                    loading_bar("Loading built-in numbers ")
                    mode = "3"
                else:
                    continue
            elif mode == "4":
                loading_bar("Exiting ")
                exit()
            else:
                print("Invalid choice. Enter 1, 2, 3, or 4 only.")
                continue

            if mode in ("1", "2", "3"):
                print("\nWhat do you want to do next?")
                print("  [1] Try again")
                print("  [2] Back to input mode menu")
                print("  [3] Finalize and process results")
                after = input("Enter choice: ")

                if after == "1":
                    if mode == "1":
                        self.generate_numbers()
                    elif mode == "2":
                        self.manual_input()
                    loading_bar("Processing results ")
                    break
                elif after == "2":
                    continue
                elif after == "3":
                    loading_bar("Finalizing results ")
                    break

    def separate(self):
        src = open(self.source_file, "r")
        even = open(self.even_file, "w")
        odd = open(self.odd_file, "w")

        for line in src:
            num = int(line.strip())
            if num % 2 == 0:
                even.write(str(num) + "\n")
            else:
                odd.write(str(num) + "\n")

        src.close()
        even.close()
        odd.close()

    def display_results(self):
        f = open(self.even_file, "r")
        even_nums = sorted([int(line.strip()) for line in f])
        f.close()
        print("Even numbers:", ", ".join(str(n) for n in even_nums))

        f = open(self.odd_file, "r")
        odd_nums = sorted([int(line.strip()) for line in f])
        f.close()
        print("Odd numbers:", ", ".join(str(n) for n in odd_nums))


separator = EvenOddSeparator("numbers.txt", "even.txt", "odd.txt")
separator.choose_mode()
separator.separate()
separator.display_results()