import os

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

