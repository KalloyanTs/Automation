file = input("Input file name: ")

try:
     read_contents = open(file, 'r')
     content_var = read_contents.read()
     words = content_var.split()
     number_of_words = len(words)
     print(number_of_words)
except FileNotFoundError:
    print("The file does not exist.")