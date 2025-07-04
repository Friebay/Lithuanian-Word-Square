import sqlite3
import os

def export_n_length_words(word_length=5):
    # Database path
    db_path = os.path.join(os.path.dirname(__file__), 'words.db')
    
    # Output file path
    output_file = os.path.join(os.path.dirname(__file__), f'{word_length}_length_words.txt')
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Query to get all words with length n
    cursor.execute('''
        SELECT DISTINCT word 
        FROM words 
        WHERE length = ?
        ORDER BY word
    ''', (word_length,))
    
    # Fetch all results
    words = cursor.fetchall()
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        for word_tuple in words:
            f.write(word_tuple[0].lower() + '\n')
    
    conn.close()

    print(f"Exported {len(words)} words of length {word_length} to {output_file}")

if __name__ == "__main__":
    # Change this value to export words of different lengths
    export_n_length_words(8)