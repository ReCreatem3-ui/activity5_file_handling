import os

class EvenOddSeparator:
    def __init__(self, source_file, even_file, odd_file):
        base = os.path.dirname(os.path.abspath(__file__))
        self.source_file = os.path.join(base, source_file)
        self.even_file = os.path.join(base, even_file)
        self.odd_file = os.path.join(base, odd_file)
 
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
separator.separate()
separator.display_results()