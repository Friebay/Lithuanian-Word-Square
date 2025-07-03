import csv
import os

def read_vietovardis_from_csv(csv_file_path):
    """
    Read terminas column from the CSV file.
    
    Args:
        csv_file_path (str): Path to the SkolintuZodynas.csv file
    
    Returns:
        list: List of terminas values
    """
    vietovardis_list = []
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            
            for row in csv_reader:
                vietovardis = row.get('terminas', '').strip()
                if vietovardis:  # Only add non-empty values
                    vietovardis_list.append(vietovardis)
                    
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []
    
    return vietovardis_list

def main():
    # Path to the CSV file
    csv_file_path = "SkolintuZodynas/SkolintuZodynas.csv"
    output_file_path = "SkolintuZodynas/SkolintuZodynas_cleaned.txt"
    
    # Check if file exists in current directory
    if not os.path.exists(csv_file_path):
        print(f"CSV file '{csv_file_path}' not found in current directory.")
        return
    
    # Read terminas from CSV
    vietovardis_data = read_vietovardis_from_csv(csv_file_path)
    
    if vietovardis_data:
        print(f"Successfully read {len(vietovardis_data)} place names from CSV.")
        
        # Extract first words and save to file
        first_words = []
        for vietovardis in vietovardis_data:
            first_word = vietovardis.split()[0] if vietovardis.split() else vietovardis
            first_words.append(first_word)
        
        try:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for word in first_words:
                    output_file.write(word + '\n')
            
            print(f"Successfully saved {len(first_words)} first words to '{output_file_path}'")
            
            # Display first 100 words as preview
            print("\nFirst 100 words saved:")
            for i, word in enumerate(first_words[:100], 1):
                print(f"{i:2d}. {word}")
            
            if len(first_words) > 100:
                print(f"... and {len(first_words) - 100} more")
                
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print("No data found or error occurred while reading the file.")

if __name__ == "__main__":
    main()
