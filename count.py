def count_occurrences(input_string):
    letter_frequency = {}
    for char in input_string:
    
        if char.isalpha():
          
            char = char.lower()

            letter_frequency[char] = letter_frequency.get(char, 0) + 1

    for letter, count in letter_frequency.items():
        print(f"{letter}: {count}")

input_string = "Hello, World!"
count_occurrences(input_string)
