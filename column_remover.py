import re
with open('lt-LT.dic.txt', 'r', encoding='utf-8') as file:
    data = file.read()
 # Remove slashes and numbers while preserving Lithuanian letters
clean_data = re.sub(r'[^a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ\s]', '', data)
with open('words2.txt', 'w', encoding='utf-8') as file:
    file.write(clean_data)
print("Cleaned data has been saved in words2.txt.")