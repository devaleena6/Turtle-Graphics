def count_occurrences(input_string):
   
    value_frequency = {}

    for char in input_string:
       
        value_frequency[char] = value_frequency.get(char, 0) + 1

    for value, count in value_frequency.items():
        print(f"{value}: {count}")

input_string = "Hello, World! 12345"
count_occurrences(input_string)
