import os
import time
import sys
import subprocess

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

class IntroOutroLoader:
    def __init__(self):
        self.spacer = Spacer()
        self.elements = Elements()

    def intro(self):
        self.spacer.clear_screen()
        print("""
                                            ███████╗██╗██╗     ███████╗    ██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ██╗███╗   ██╗ ██████╗ 
                                            ██╔════╝██║██║     ██╔════╝    ██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██║████╗  ██║██╔════╝ 
                                            █████╗  ██║██║     █████╗      ███████║███████║██╔██╗ ██║██║  ██║██║     ██║██╔██╗ ██║██║  ███╗
                                            ██╔══╝  ██║██║     ██╔══╝      ██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██║██║╚██╗██║██║   ██║
                                            ██║     ██║███████╗███████╗    ██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗██║██║ ╚████║╚██████╔╝
                                            ╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝      
            """)
        self.elements.slowtype("                                                                     Welcome to ReCreatem3's file handling programs", duration=2.5)
        time.sleep(2)

    def outro(self):
        self.spacer.clear_screen()
        print("""
                                                        ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
                                                        ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
                                                           ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
                                                           ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
                                                           ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
                                                           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ 
                                                                                   ┏┓             ┓ •    
                                                                                   ┣ ┏┓┏┓  ┓┏┏┏┓╋┏┣┓┓┏┓┏┓
                                                                                   ┻ ┗┛┛   ┗┻┛┗┻┗┗┛┗┗┛┗┗┫
                                                                                                        ┛
            """)
        time.sleep(2)

class Launcher:
    def __init__(self):
        self.space = Spacer()
        self.element = Elements()
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.programs = {
            "1": {
                "label": "P1 - Even and Odd File Separator",
                "path": os.path.join(self.base, "program_1", "p1_even_odd_file_separator.py")
            },
            "2": {
                "label": "P2 - Student GWA Analyzer",
                "path": os.path.join(self.base, "program_2", "p2_student_gwa_analyzer.py")
            },
            "3": {
                "label": "P3 - Multiline File Writer",
                "path": os.path.join(self.base, "program_3", "p3_multiline_file_writer.py")
            },
            "4": {
                "label": "P4 - Even Square & Odd Cube Processor",
                "path": os.path.join(self.base, "program_4", "p4_even_square_odd_cube_processor.py")
            },
        }

    def launch(self, key):
        program = self.programs[key]
        path = program["path"]

        if not os.path.exists(path):
            self.space.clear_screen()
            print(f"File not found: {path}")
            print("Make sure your folder structure matches the expected layout.")
            time.sleep(3)
            return

        self.space.clear_screen()
        self.element.loading_bar(f"Launching {program['label']} ")
        self.space.clear_screen()
        subprocess.run([sys.executable, path])

    def run(self):
        while True:
            self.space.clear_screen()
            self.space.equals_separator()
            print("Select a program to launch:")
            self.space.equals_separator()
            for key, prog in self.programs.items():
                print(f"  [{key}] {prog['label']}")
            print("  [5] Exit")
            self.space.equals_separator()
            choice = input("Enter choice: ")

            if choice in self.programs:
                self.launch(choice)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Enter 1, 2, 3, 4, or 5 only.")
                time.sleep(1)


impression = IntroOutroLoader()
launcher = Launcher()

impression.intro()
launcher.run()
impression.outro()