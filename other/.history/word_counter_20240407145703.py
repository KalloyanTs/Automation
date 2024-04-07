file = input("Input file name: ")

def word_counter(file):
     try:
          with open(file, "r") as read_contents:
               content_var = read_contents.read()
               words = content_var.split()
               words_dict = {}
               for n in words:
                    words_dict[n] = words_dict.setdefault(n, 0) + 1
               return words_dict
     except FileNotFoundError:
          print("The file does not exist.")

word_occurrences = word_counter(file)


for i, f in word_occurrences.items():
    print(f"{i}: {f}")
