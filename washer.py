filemame = "1"

# Save to file "w" = read mode
def save_words_in_column(filename, words):
    with open(filename, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")
            
            
def count_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        words = file.read().split()
        return len(words)
    

 #Open the file "r" = read mode
with open(filemame + ".txt", "r", encoding="utf-8") as file:
    
    # Read the contents of the file
    words = file.read().split()

unique_words = set()

non_repeating_words = []

repeating_words = []

for word in words:
    # Check if the word is not already in the set
    if word not in unique_words:
        # Add the word to the set and list
        unique_words.add(word)
        non_repeating_words.append(word)
    else:
        repeating_words.append(word)

 # Call the function to save words in a column format
save_words_in_column(filemame + "_cleaned.txt", non_repeating_words)

    
    
count = count_words(filemame + ".txt")
cleaned_count = count_words(filemame + "_cleaned.txt")

print("Number of words in " + filemame + ".txt:", count)
print("Number of words in " + filemame + "_cleaned.txt:", cleaned_count)