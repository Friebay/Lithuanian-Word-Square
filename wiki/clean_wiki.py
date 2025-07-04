import re
import os

def clean_wiki_text(input_file, output_file):
    """
    Clean Wikipedia text dump and extract words into one word per line format.
    
    Args:
        input_file (str): Path to input Wikipedia text file
        output_file (str): Path to output cleaned text file
    """
    
    # Set to store unique words
    unique_words = set()
    
    # Pattern to match words (Lithuanian characters included)
    # This pattern matches sequences of letters, including Lithuanian special characters
    word_pattern = re.compile(r'[a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ]+')
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            print(f"Processing {input_file}...")
            
            line_count = 0
            for line in infile:
                line_count += 1
                
                # Print progress every 10000 lines
                if line_count % 10000 == 0:
                    print(f"Processed {line_count} lines, found {len(unique_words)} unique words")
                
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Skip lines that look like titles (ending with colon)
                if line.strip().endswith(':'):
                    continue
                
                # Find all words in the line
                words = word_pattern.findall(line)
                
                # Add words to set (automatically handles duplicates)
                for word in words:
                    # Convert to lowercase for consistency
                    word_lower = word.lower()
                    
                    # Filter out very short words (less than 2 characters)
                    if len(word_lower) >= 2:
                        unique_words.add(word_lower)
        
        print(f"Found {len(unique_words)} unique words")
        
        # Write words to output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Sort words alphabetically
            sorted_words = sorted(unique_words)
            
            for word in sorted_words:
                outfile.write(word + '\n')
        
        print(f"Cleaned words saved to {output_file}")
        print(f"Total unique words: {len(unique_words)}")
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except Exception as e:
        print(f"Error processing file: {e}")

def clean_wiki_text_advanced(input_file, output_file, min_length=2, max_length=50):
    """
    Advanced cleaning with more options.
    
    Args:
        input_file (str): Path to input Wikipedia text file
        output_file (str): Path to output cleaned text file
        min_length (int): Minimum word length to include
        max_length (int): Maximum word length to include
    """
    
    unique_words = set()
    
    # More comprehensive pattern for Lithuanian words
    word_pattern = re.compile(r'[a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ]+')
    
    # Patterns to skip certain types of content
    skip_patterns = [
        re.compile(r'^\s*\d+\s*$'),  # Lines with only numbers
        re.compile(r'^\s*[IVX]+\s*$'),  # Roman numerals
        re.compile(r'^\s*[a-z]\)\s*'),  # List items like "a)", "b)"
        re.compile(r'^\s*\d+\.\s*'),  # Numbered lists
    ]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            print(f"Processing {input_file} with advanced cleaning...")
            
            line_count = 0
            for line in infile:
                line_count += 1
                
                if line_count % 10000 == 0:
                    print(f"Processed {line_count} lines, found {len(unique_words)} unique words")
                
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Skip lines matching skip patterns
                if any(pattern.match(line) for pattern in skip_patterns):
                    continue
                
                # Skip lines that look like titles (ending with colon)
                if line.strip().endswith(':'):
                    continue
                
                # Skip lines that are mostly punctuation or numbers
                if len(re.sub(r'[^a-zA-ZąčęėįšųūžĄČĘĖĮŠŲŪŽ]', '', line)) < len(line) * 0.5:
                    continue
                
                # Find all words in the line
                words = word_pattern.findall(line)
                
                for word in words:
                    word_lower = word.lower()
                    
                    # Filter by length
                    if min_length <= len(word_lower) <= max_length:
                        # Additional filtering: skip words that are mostly repeated characters
                        if len(set(word_lower)) >= 2:  # At least 2 different characters
                            unique_words.add(word_lower)
        
        print(f"Found {len(unique_words)} unique words")
        
        # Write words to output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            sorted_words = sorted(unique_words)
            
            for word in sorted_words:
                outfile.write(word + '\n')
        
        print(f"Cleaned words saved to {output_file}")
        print(f"Total unique words: {len(unique_words)}")
        
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    # Configuration
    input_file = "wiki\\wiki.txt"
    output_file = "wiki\\wiki_cleaned_2.txt"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Input file {input_file} not found in current directory")
        print("Please make sure the file exists and run the script again")
    else:
        # Choose cleaning method
        print("Choose cleaning method:")
        print("1. Basic cleaning (default)")
        print("2. Advanced cleaning with more filters")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "2":
            # Advanced cleaning
            min_len = input("Minimum word length (default: 2): ").strip()
            max_len = input("Maximum word length (default: 50): ").strip()
            
            min_len = int(min_len) if min_len else 2
            max_len = int(max_len) if max_len else 50
            
            clean_wiki_text_advanced(input_file, output_file, min_len, max_len)
        else:
            # Basic cleaning
            clean_wiki_text(input_file, output_file)