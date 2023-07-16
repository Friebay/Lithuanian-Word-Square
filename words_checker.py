# Set of Lithuanian letters
lithuanian_letters = set('aąbcčdeęėfghiįyjklmnoprsštuųūvzž')
 # Read file contents
with open('modified_testing_cleaned_cleaned.txt', 'r', encoding='utf-8') as file:
    content = file.read()
 # Split content into words
words = content.split()
 # Remove words without Lithuanian letters and save them into a new list
filtered_words = [word for word in words if any(letter.lower() in lithuanian_letters for letter in word)]
 # Join filtered words with new lines
filtered_content = '\n'.join(filtered_words)
 # Save modified content into the new file "wiki_lithuanianletters.txt"
with open('wiki_lithuanianletters.txt', 'w', encoding='utf-8') as file:
    file.write(filtered_content)
print("Words containing Lithuanian letters have been saved in the 'wiki_lithuanianletters.txt' file.")