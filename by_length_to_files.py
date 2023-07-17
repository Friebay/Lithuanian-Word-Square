import os
 # Path to the text file
file_path = r"C:\Users\zabit\Documents\GitHub\Lithuanian-Word-Square\all_cleaned_length.txt"
 # Path to the folder where the combined files will be created
folder_path = r"C:\Users\zabit\Documents\GitHub\Lithuanian-Word-Square"
 # Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
 # Read the words from the text file
with open(file_path, 'r', encoding='utf-8') as file:
    words = file.read().splitlines()
 # Separate the words into files based on their length
length_files = {}
for word in words:
    length = len(word)
    if length not in length_files:
        length_files[length] = []
    length_files[length].append(word)
 # Write the words of the same length into one file
for length, words_list in length_files.items():
    words_file = os.path.join(folder_path, f"{length}_length_words.txt")
    with open(words_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(words_list))