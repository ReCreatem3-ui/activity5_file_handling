import os
import time
import sys

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

class FileWriter:
    def __init__(self, output_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.output_file = os.path.join(base, output_file)

    def write_lines(self):
        f = open(self.output_file, "w")
        more = "y"

        while more.lower() == "y":
            line = input("Enter a line: ")
            f.write(line + "\n")
            more = input("Add more lines? (y/n): ")

        f.close()
        print("Saved to", self.output_file)

    def display_contents(self):
        print(f"---{self.output_file}---")
        f = open(self.output_file, "r")
        print(f.read())
        f.close()

filename = input("Enter output filename: ")
writer = FileWriter(filename)
writer.write_lines()
writer.display_contents()

