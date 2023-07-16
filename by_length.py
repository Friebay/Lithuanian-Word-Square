# Open the input file
with open("final.txt", "r", encoding="utf-8") as input_file:
    # Read the words from the input file
    words = input_file.read().split()
 # Sort the words by length
sorted_words = sorted(words, key=len)
 # Open the output file
with open("final_length.txt", "w", encoding="utf-8") as output_file:
    # Write the sorted words to the output file
    for word in sorted_words:
        output_file.write(word + "\n")