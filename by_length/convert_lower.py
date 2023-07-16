# Open the input file
with open('8_length_words.txt', 'r', encoding='utf-8') as file:
    content = file.read()
 # Convert uppercase words to lowercase and save each word on a new line
converted_content = '\n'.join(word.lower() if word.isupper() else word for word in content.split())
 # Open the output file and write the converted content
with open('8_length_words.txt', 'w', encoding='utf-8') as file:
    file.write(converted_content)