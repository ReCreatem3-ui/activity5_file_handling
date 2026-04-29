import os
import time
import random

def slowtype(text, duration):
    delay = duration / len(text) if len(text) > 0 else 0
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class EvenOddSeparator:
    def __init__(self, source_file, even_file, odd_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.even_file = os.path.join(base, even_file)
        self.odd_file = os.path.join(base, odd_file)
    
    def generate_numbers(self):
        range_start = int(input("Enter range start: "))
        range_end = int(input("Enter range end: "))
        num_count = int(input("How many numbers to generate?: "))

        numbers = random.sample(range(range_start, range_end + 1), num_count)

        f = open(self.source_file, "w")
        for num in numbers:
            f.write(str(num) + "\n")
        f.close()

        print("Generated:", ", ".join(str(n) for n in numbers))

    def manual_input(self):
        f = open(self.source_file, "w")
        more = "y"

        while more.lower() == "y":
            num = input("Enter a number: ")
            f.write(num + "\n")
            more = input("Add more? (y/n)")
        
        f.close()

    def choose_mode(self):
        print("Select input mode:")
        print("  [1] Generate random numbers")
        print("  [2] Manual input")
        mode = input("Enter choice: ")

        if mode == "1":
            self.generate_numbers()
        elif mode == "2":
            self.manual_input()
        else:
            print("Invalid choice.")
    
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