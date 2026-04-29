import os
import time
import sys
import random

class Spacer:
    def __init__(self):
        pass

    def one_space(self):
        print()

    def light_space(self):
        for i in range(2):
            print()

    def medium_space(self):
        for i in range(3):
            print()

    def heavy_space(self):
        for i in range(5):
            print()

    def clear_screen(self):
        for i in range(35):
            print()

    def custom_space(self, lines=1):
        for i in range(lines):
            print()

    def line_separator(self):
        print("-" * 50)

    def equals_separator(self):
        print("=" * 50)

class Elements:
    def loading_bar(self, label="", total=26, duration=2):
        for i in range(total + 1):
            bar = '▄' * i + ' ' * (total - i)
            percent = int((i / total) * 100)
            sys.stdout.write(f'\r{label}{bar} {percent}%')
            sys.stdout.flush()
            time.sleep(duration / total)
        print()

    def slowtype(self, text, duration):
        delay = duration / len(text) if len(text) > 0 else 0
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class IntroLoader:
    def __init__(self):
        self.spacer = Spacer()
        self.elements = Elements()

    def intro(self):
        self.spacer.clear_screen()
        print("""
                                                    ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    ██╗  ██╗
                                                    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ██║  ██║
                                                    ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║    ███████║
                                                    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    ╚════██║
                                                    ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║         ██║
                                                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝         ╚═╝
            """)
        self.elements.slowtype("                                                                 Even Square & Odd Cube Processor", duration=2.5)
        self.spacer.light_space()
        time.sleep(2)

class PowerSeparator:
    def __init__(self, source_file, double_file, triple_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.double_file = os.path.join(base, double_file)
        self.triple_file = os.path.join(base, triple_file)
        self.space = Spacer()
        self.element = Elements()

    def generate_numbers(self):
            while True:
                try:
                    self.space.clear_screen()
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
                        print(f"Count exceeds available numbers. Max is {range_end - range_start + 1}.")
                        continue
                    break

                except ValueError:
                    print("Invalid input! Please enter a numerical value.")

            numbers = random.sample(range(range_start, range_end + 1), num_count)

            f = open(self.source_file, "w")
            for num in numbers:
                f.write(str(num) + "\n")
            f.close()

            self.space.clear_screen()
            print("Generated:")
            self.element.slowtype(", ".join(str(n) for n in numbers), duration=3)
            self.space.light_space()
            time.sleep(2)

    def manual_input(self):
        numbers = []
        more = "y"

        self.space.clear_screen()
        while more.lower() == "y":
            while True:
                try:
                    num = int(input("Enter a number: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a whole number.")
            more = input("Add more? (y/n): ")

        f = open(self.source_file, "w")
        for num in numbers:
            f.write(str(num) + "\n")
        f.close()

        self.space.clear_screen()
        print("You entered:")
        print(", ".join(str(n) for n in numbers))
        self.space.light_space()
        time.sleep(2)

    def process(self):
        src = open(self.source_file, "r")
        square = open(self.double_file, "w")
        cube = open(self.triple_file, "w")

        for line in src:
            num = int(line.strip())
            if num % 2 == 0:
                square.write(str(num ** 2) + "\n")
            else:
                cube.write(str(num ** 3) + "\n")
        
        src.close()
        square.close()
        cube.close()
    
    def display_results(self):
        f = open(self.double_file, "r")
        even_results = sorted([int(line.strip()) for line in f])
        f.close()

        f = open(self.source_file, "r")
        all_nums = [int(line.strip()) for line in f]
        f.close()
        even_nums = sorted([n for n in all_nums if n % 2 == 0])
        odd_nums = sorted([n for n in all_nums if n % 2 != 0])

        f = open(self.triple_file, "r")
        odd_results = sorted([int(line.strip()) for line in f])
        f.close()

        print("--- Square of Even Numbers ---")
        print("Numbers used: ", ", ".join(str(n) for n in even_nums))
        print("Results:      ", ", ".join(str(n) for n in even_results))

        print()

        print("--- Cube of Odd Numbers ---")
        print("Numbers used: ", ", ".join(str(n) for n in odd_nums))
        print("Results:      ", ", ".join(str(n) for n in odd_results))

class SelectMenu:
    def __init__(self):
        self.space = Spacer()
        self.element = Elements()
        self.processor = PowerSeparator("integers.txt", "double.txt", "triple.txt")

    def post_action(self):
        while True:
            self.space.clear_screen()
            print("What do you want to do next?")
            print("  [1] Try again")
            print("  [2] Return to menu")
            print("  [3] Proceed to results")
            print("  [4] Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                return "retry"
            elif choice == "2":
                return "menu"
            elif choice == "3":
                self.element.loading_bar("Processing results ")
                return "proceed"
            elif choice == "4":
                self.space.clear_screen()
                self.element.loading_bar("Exiting ")
                exit()
            else:
                print("Invalid choice. Enter 1, 2, 3, or 4 only.")
                time.sleep(1)

processor = PowerSeparator("integers.txt", "double.txt", "triple.txt")
processor.process()
processor.display_results()