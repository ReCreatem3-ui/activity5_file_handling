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

def slowtype(text, duration):
    delay = duration / len(text) if len(text) > 0 else 0
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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
        self.spacer = Spacer()

    def validate_gwa(self, value):
        try:
            gwa = float(value)
            if gwa < 1.00 or gwa > 5.00:
                print("GWA must be between 1.00 and 5.00 only.")
                return None
            return gwa
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
            return None
        
    def add_new_student(self):
        self.spacer.clear_screen()
        loading_bar("Loading input mode ")

        more = "y"
        while more.lower() == "y":
            name = input("Enter student name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            while True:
                gwa_input = input("Enter GWA (1.00 - 5.00): ")
                gwa = self.validate_gwa(gwa_input)
                if gwa is not None:
                    break

            self.students.append((name, gwa))
            self.spacer.light_space()
            print(f"Added: {name} | GWA: {gwa:.2f}")
            self.spacer.light_space()
            more = input("Add another student? (y/n): ")

        self.spacer.clear_screen()
        save = input("Save students to file? (y/n): ")
        if save.lower() == "y":
            loading_bar("Saving ")
            self._save_to_file()
            self.spacer.light_space()
            print("Students saved successfully.")
            time.sleep(2)

        self.find_highest()
        self._display_results()
        self._post_action_menu()

    def _save_to_file(self):
        f = open(self.source_file, "w")
        for name, gwa in self.students:
            f.write(f"{name},{gwa:.2f}\n")
        f.close()
        
    def load_from_file(self):
        self.spacer.clear_screen()
        loading_bar("Loading from file ")

        if not os.path.exists(self.source_file):
            self.spacer.light_space()
            print("File not found:", self.source_file)
            self.spacer.light_space()
            time.sleep(2)
            self._post_action_menu()
            return

        self.students = []
        f = open(self.source_file, "r")
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 2:
                name = parts[0]
                gwa = float(parts[1])
                self.students.append((name, gwa))
        f.close()

        self.spacer.light_space()
        print(f"Loaded {len(self.students)} student(s) from file.")
        time.sleep(2)

        self.find_highest()
        self._display_results()
        self._post_action_menu()

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
 
    def _display_results(self):
        self.spacer.clear_screen()
        self.spacer.equals_separator()
        print("Student List:")
        self.spacer.equals_separator()

        if not self.students:
            print("No students loaded.")
            self.spacer.equals_separator()
            return

        sorted_students = sorted(self.students, key=lambda x: x[1])
        for name, gwa in sorted_students:
            if name == self.top_name:
                print(f"  {name:<30} {gwa:.2f}  ← HIGHEST GWA")
            else:
                print(f"  {name:<30} {gwa:.2f}")

        self.spacer.equals_separator()
        self.spacer.light_space()
        print("Student with the Highest GWA:")
        slowtype(f"  Name : {self.top_name}", duration=2)
        slowtype(f"  GWA  : {self.top_gwa:.2f}", duration=2)
        self.spacer.equals_separator()

    def _post_action_menu(self):
        while True:
            self.spacer.light_space()
            self.spacer.line_separator()
            print("What do you want to do next?")
            print("  [1] Back to main menu")
            print("  [2] Save and exit")
            self.spacer.line_separator()
            choice = input("Enter choice: ")

            if choice == "1":
                return
            elif choice == "2":
                self.spacer.clear_screen()
                loading_bar("Saving ")
                self._save_to_file()
                self.spacer.light_space()
                print("Data saved. Goodbye!")
                self.spacer.light_space()
                exit()
            else:
                self.spacer.light_space()
                print("Invalid choice. Enter 1 or 2 only.")
                time.sleep(0.5)
    
    def run(self):
        while True:
            self.spacer.clear_screen()
            self.spacer.equals_separator()
            print("Select operation:")
            print("  [1] Add new student")
            print("  [2] Load from file")
            print("  [3] Exit")
            self.spacer.equals_separator()
            choice = input("Enter choice: ")

            if choice == "1":
                self.add_new_student()
            elif choice == "2":
                self.load_from_file()
            elif choice == "3":
                self.spacer.clear_screen()
                loading_bar("Exiting ")
                exit()
            else:
                self.spacer.light_space()
                print("Invalid choice. Enter 1, 2, or 3 only.")
                time.sleep(0.5)
 
 
finder = GWAFinder("students_with_gwa.txt")
finder.run()