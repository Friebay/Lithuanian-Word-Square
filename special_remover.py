# Open the file in read mode
with open("all_cleaned_cleaned.txt", "r", encoding="utf-8") as file:
    # Read all lines from the file
    lines = file.readlines()
# Create a list to store the filtered lines
filtered_lines = []
# Iterate over each line
for line in lines:
    # Check if the line contains any special characters, 'w', 'x', 'À', 'Ò', 'Í', or letters with a grave accent on the opposite side
    if not any(char in line for char in ['.', ',', '-', "'", '`', '*', 'ʼ','·']) and 'ʼ' not in line and 'Ù' not in line and 'Æ' not in line and 'Ç' not in line and 'Ê' not in line and 'Ć' not in line and 'Ş' not in line and 'Ī' not in line and 'Û' not in line and 'Ế' not in line and 'É' not in line and 'Ó' not in line and 'Q' not in line and 'Â' not in line and 'Ạ' not in line and 'Ä' not in line and 'Ü' not in line and 'Đ' not in line and 'Ý' not in line and 'Á' not in line and 'Ā' not in line and 'Ě' not in line and 'Ĩ' not in line and 'È' not in line and 'Ļ' not in line and 'Ö' not in line and 'Ú' not in line and 'W' not in line and 'X' not in line and 'À' not in line and 'Ò' not in line and 'Í' not in line and 'À'[::-1] not in line and 'Ò'[::-1] not in line and 'Í'[::-1] not in line:
        # If no special characters, add the line to the filtered list
        filtered_lines.append(line)
# Open the file in write mode and overwrite its contents with the filtered lines
with open("final.txt", "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)