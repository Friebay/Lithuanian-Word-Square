import csv
import os
import re

def remove_punctuation(text):
    """
    Remove punctuation symbols from text.
    
    Args:
        text (str): Input text with punctuation
    
    Returns:
        str: Text with punctuation removed
    """
    # First, replace em dashes and dashes with spaces
    text = re.sub(r'[—–\-]', ' ', text)
    
    # Then remove other punctuation patterns including Lithuanian quotation marks and “
    punctuation_pattern = r'[,.\!?;:()\„\“"\'`]'
    # Remove punctuation and extra spaces
    cleaned_text = re.sub(punctuation_pattern, '', text)
    
    # Remove extra whitespace and strip
    cleaned_text = ' '.join(cleaned_text.split())
    
    return cleaned_text

def read_sentences_from_tsv(tsv_file_path):
    """
    Read sentence column from the TSV file.
    
    Args:
        tsv_file_path (str): Path to the validated.tsv file
    
    Returns:
        list: List of sentence values
    """
    sentences_list = []
    
    try:
        with open(tsv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter='\t')
            
            for row in csv_reader:
                sentence = row.get('sentence', '').strip()
                if sentence:  # Only add non-empty values
                    sentences_list.append(sentence)
                    
    except FileNotFoundError:
        print(f"Error: File '{tsv_file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading TSV file: {e}")
        return []
    
    return sentences_list

def main():
    # Path to the TSV file
    tsv_file_path = "common_voice_17\\validated.tsv"
    output_sentences_file = "common_voice_17\\sentences_cleaned.txt"
    output_words_file = "common_voice_17\\words_cleaned.txt"
    
    # Check if file exists in current directory
    if not os.path.exists(tsv_file_path):
        print(f"TSV file '{tsv_file_path}' not found in current directory.")
        return
    
    # Read sentences from TSV
    sentences_data = read_sentences_from_tsv(tsv_file_path)
    
    if sentences_data:
        print(f"Successfully read {len(sentences_data)} sentences from TSV.")
        
        # Clean sentences by removing punctuation
        cleaned_sentences = []
        all_words = []
        
        for sentence in sentences_data:
            cleaned_sentence = remove_punctuation(sentence)
            if cleaned_sentence:  # Only add non-empty sentences after cleaning
                cleaned_sentences.append(cleaned_sentence)
                # Extract individual words from the sentence
                words = cleaned_sentence.split()
                all_words.extend(words)
        
        print(f"Successfully cleaned {len(cleaned_sentences)} sentences (removed punctuation).")
        print(f"Extracted {len(all_words)} individual words.")
        
        # Save cleaned sentences to file
        try:
            with open(output_sentences_file, 'w', encoding='utf-8') as output_file:
                for sentence in cleaned_sentences:
                    output_file.write(sentence + '\n')
            
            print(f"Successfully saved {len(cleaned_sentences)} cleaned sentences to '{output_sentences_file}'")
            
            # Save individual words to file
            with open(output_words_file, 'w', encoding='utf-8') as output_file:
                for word in all_words:
                    output_file.write(word + '\n')
            
            print(f"Successfully saved {len(all_words)} words to '{output_words_file}'")
            
            # Display first 10 sentences as preview
            print("\nFirst 10 cleaned sentences saved:")
            for i, sentence in enumerate(cleaned_sentences[:10], 1):
                print(f"{i:2d}. {sentence}")
            
            if len(cleaned_sentences) > 10:
                print(f"... and {len(cleaned_sentences) - 10} more")
            
            # Display first 10 words as preview
            print("\nFirst 10 words saved:")
            for i, word in enumerate(all_words[:10], 1):
                print(f"{i:2d}. {word}")
            
            if len(all_words) > 10:
                print(f"... and {len(all_words) - 10} more")
                
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print("No data found or error occurred while reading the file.")

if __name__ == "__main__":
    main()
