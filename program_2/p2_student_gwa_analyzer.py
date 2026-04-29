import os
import time
import sys

class Spacer:
    def __init__(self):
        pass

    def light_space(self):
        for i in range(2):
            print()

    def medium_space(self):
        for i in range(3):
            print()

    def heavy_space(self):
        for i in range(5):
            print()

    def custom_space(self, lines=1):
        for i in range(lines):
            print()

    def line_separator(self):
        print("-" * 50)

    def equals_separator(self):
        print("=" * 50)

class loading_bar:
    def loading_bar(label="", total=26, duration=2):
        for i in range(total + 1):
            bar = '▄' * i + ' ' * (total - i)
            percent = int((i / total) * 100)
            sys.stdout.write(f'\r{label}{bar} {percent}%')
            sys.stdout.flush()
            time.sleep(duration / total)
        print()

class GWAFinder:
    def __init__(self, source_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.top_name = ""
        self.top_gwa = float("inf")

    def find_highest(self):
        f = open(self.source_file, "r")

        for line in f:
            parts = line.strip().split(",")
            name = parts[0]
            gwa = float(parts[1])
            if gwa < self.top_gwa:
                self.top_gwa = gwa
                self.top_name = name
        f.close()
 
    def display_result(self):
        print("Student with the Highest GWA:")
        print(f"  Name : {self.top_name}")
        print(f"  GWA  : {self.top_gwa}")
 
 
finder = GWAFinder("students_with_gwa.txt")
finder.find_highest()
finder.display_result()