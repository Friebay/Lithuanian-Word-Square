import re
import os

def clean_dictionary_file():
    """
    Remove all numbers, forward slashes, periods, and lines starting with "-" from the lt-LT.dic file
    """
    # Define input and output file paths
    input_file = "Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika\\lt-LT.dic"
    output_file = "Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika\\lt-LT_cleaned.txt"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found in current directory")
        return
    
    try:
        # Read the original file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Filter out lines that start with "-"
        filtered_lines = [line for line in lines if not line.strip().startswith('-')]
        
        # Join the filtered lines back into content
        content = ''.join(filtered_lines)
        
        # Remove all numbers (0-9), forward slashes (/), and periods (.)
        # This regex pattern matches any digit, forward slash, or period
        cleaned_content = re.sub(r'[0-9/.]', '', content)
        
        # Alternative approach using string methods (commented out):
        # cleaned_content = content
        # for char in '0123456789/.':
        #     cleaned_content = cleaned_content.replace(char, '')
        
        # Write the cleaned content to a new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)
        
        print(f"Successfully cleaned the dictionary file!")
        print(f"Original file: {input_file}")
        print(f"Cleaned file: {output_file}")
        
        # Show some statistics
        original_size = len(content)
        cleaned_size = len(cleaned_content)
        removed_chars = original_size - cleaned_size
        
        print(f"\nStatistics:")
        print(f"Original file size: {original_size:,} characters")
        print(f"Cleaned file size: {cleaned_size:,} characters")
        print(f"Characters removed: {removed_chars:,}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    clean_dictionary_file()
