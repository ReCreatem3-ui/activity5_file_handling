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

class IntroLoader:
    def __init__(self):
        self.spacer = Spacer()
        self.elements = Elements()

    def intro(self):
        self.spacer.clear_screen()
        print("""
                                                    ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    ██████╗ 
                                                    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    ╚════██╗
                                                    ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║     █████╔╝
                                                    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║     ╚═══██╗
                                                    ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    ██████╔╝
                                                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═════╝ 
            """)
        self.elements.slowtype("                                                                            Multi-line file writer", duration=2.5)
        self.spacer.light_space()
        time.sleep(2)

class FileWriter:
    def __init__(self, output_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.output_file = os.path.join(base, output_file)
        self.element = Elements()
        self.space = Spacer()
        self.lines_buffer = []

    def write_lines(self):
        self.lines_buffer = []
        more = "y"

        while more.lower() == "y":
            self.space.clear_screen()
            line = input("Enter a line: ")
            self.lines_buffer.append(line)
            self.space.one_space()
            more = input("Add more lines? (y/n): ")

    def append_lines(self):
        self.lines_buffer = []
        more = "y"

        while more.lower() == "y":
            self.space.clear_screen()
            line = input("Enter a line: ")
            self.lines_buffer.append(line)
            self.space.one_space()
            more = input("Add more lines? (y/n): ")

    def save_write(self):
        f = open(self.output_file, "w")
        for line in self.lines_buffer:
            f.write(line + "\n")
        f.close()
        print("Saved to", self.output_file)

    def save_append(self):
        f = open(self.output_file, "a")
        for line in self.lines_buffer:
            f.write(line + "\n")
        f.close()
        print("Appended to", self.output_file)

    def display_contents(self):
        self.space.clear_screen()
        f = open(self.output_file, "r")
        content = f.read()
        f.close()

        self.space.clear_screen()
        print(f"--- {self.output_file} ---")
        self.space.one_space()

        for line in content.splitlines():
            self.element.slowtype(" " * 60 + line.center(60), duration=max(0.5, len(line) / 10))

class SelectMenu:
    def __init__(self):
        self.space = Spacer()
        self.element = Elements()

    def post_action(self, writer, mode):
        while True:
            self.space.clear_screen()
            print("What do you want to do next?")
            if mode != "read":
                print("  [1] Save and display")
            print("  [2] Return to menu")
            print("  [3] Exit")
            choice = input("Enter choice: ")

            if choice == "1" and mode != "read":
                if mode == "write":
                    writer.save_write()
                elif mode == "append":
                    writer.save_append()
                self.element.loading_bar("Saving ")
                writer.display_contents()
                return "done"
            elif choice == "2":
                self.space.clear_screen()
                print("Returning to menu...")
                time.sleep(1)
                return "menu"
            elif choice == "3":
                self.space.clear_screen()
                self.element.loading_bar("Exiting ")
                exit()
            else:
                print("Invalid choice.")
                time.sleep(1)

    def run(self):
        while True:
            self.space.clear_screen()
            print("Select mode:")
            print("  [1] Create new file")
            print("  [2] Open existing file")
            print("  [3] Exit")
            mode = input("Enter choice: ")

            if mode == "1":
                self.space.clear_screen()
                filename = input("Enter new filename (e.g. mylife.txt): ")
                writer = FileWriter(filename)
                writer.write_lines()
                result = self.post_action(writer, "write")
                if result == "menu":
                    continue
                break

            elif mode == "2":
                self.space.clear_screen()
                filename = input("Enter existing filename (e.g. mylife.txt): ")
                writer = FileWriter(filename)

                if not os.path.exists(writer.output_file):
                    self.space.clear_screen()
                    self.element.slowtype(f"File '{filename}' not found. Try again.", duration=1)
                    time.sleep(2)
                    continue

                self.space.clear_screen()
                print("File found. What do you want to do?")
                print("  [1] Read only")
                print("  [2] Append new lines")
                action = input("Enter choice: ")

                if action == "1":
                    writer.display_contents()
                    result = self.post_action(writer, "read")
                    if result == "menu":
                        continue
                    break
                elif action == "2":
                    writer.append_lines()
                    result = self.post_action(writer, "append")
                    if result == "menu":
                        continue
                    break

            elif mode == "3":
                self.space.clear_screen()
                self.element.loading_bar("Exiting ")
                break
            else:
                self.space.clear_screen()
                print("Invalid choice. Enter 1, 2, or 3 only.")
                time.sleep(1.5)

introduction = IntroLoader()
introduction.intro()
menu = SelectMenu()
menu.run()