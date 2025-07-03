import sqlite3
import os
import sys
from datetime import datetime

def normalize_word(word):
    """Normalize Lithuanian word by removing diacritics and converting to lowercase."""
    # Lithuanian diacritic mappings
    diacritic_map = {
        'ą': 'a', 'č': 'c', 'ę': 'e', 'ė': 'e', 'į': 'i', 
        'š': 's', 'ų': 'u', 'ū': 'u', 'ž': 'z',
        'Ą': 'A', 'Č': 'C', 'Ę': 'E', 'Ė': 'E', 'Į': 'I',
        'Š': 'S', 'Ų': 'U', 'Ū': 'U', 'Ž': 'Z'
    }
    
    normalized = word.lower()
    for diacritic, replacement in diacritic_map.items():
        normalized = normalized.replace(diacritic.lower(), replacement)
    
    return normalized

def insert_words_from_file():
    """Insert words from SkolintuZodynas_cleaned.txt into the words database."""
    
    # Get paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    txt_file_path = os.path.join(script_dir, 'SkolintuZodynas_cleaned.txt')
    db_path = os.path.join(os.path.dirname(script_dir), 'words.db')
    
    # Check if files exist
    if not os.path.exists(txt_file_path):
        print(f"Error: Text file not found at {txt_file_path}")
        return False
        
    if not os.path.exists(db_path):
        print(f"Error: Database not found at {db_path}")
        print("Please run setup_database.py first to create the database.")
        return False
    
    print(f"Reading words from: {txt_file_path}")
    print(f"Inserting into database: {db_path}")
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Register source if not exists
        source_name = "VietovardziuZodynas"
        source_description = "https://data.gov.lt/datasets/2937/"
        
        cursor.execute('''
            INSERT OR IGNORE INTO sources (name, description, file_path) 
            VALUES (?, ?, ?)
        ''', (source_name, source_description, txt_file_path))
        
        # Read and process words
        words_processed = 0
        words_inserted = 0
        words_skipped = 0
        batch_size = 1000
        batch_words = []
        
        print("Processing words...")
        
        with open(txt_file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                word = line.strip()
                
                # Skip empty lines
                if not word:
                    continue
                
                words_processed += 1
                
                # Normalize the word
                normalized_word = normalize_word(word)
                word_length = len(word)
                
                # Add to batch
                batch_words.append((
                    word,                    # original word
                    word_length,             # length
                    source_name,             # source
                    'SkolintuZodynas_cleaned.txt', # source_file
                    word,                    # original_form
                    normalized_word          # normalized_form
                ))
                
                # Insert batch when it reaches batch_size
                if len(batch_words) >= batch_size:
                    inserted, skipped = insert_word_batch(cursor, batch_words)
                    words_inserted += inserted
                    words_skipped += skipped
                    batch_words = []
                    
                    if words_processed % 10000 == 0:
                        print(f"Processed {words_processed} words, inserted {words_inserted}, skipped {words_skipped}")
                        conn.commit()  # Commit every 10k words
        
        # Insert remaining words in the last batch
        if batch_words:
            inserted, skipped = insert_word_batch(cursor, batch_words)
            words_inserted += inserted
            words_skipped += skipped
        
        # Update source statistics
        cursor.execute('''
            UPDATE sources 
            SET total_words = ?, processed_at = CURRENT_TIMESTAMP 
            WHERE name = ?
        ''', (words_inserted, source_name))
        
        # Final commit
        conn.commit()
        conn.close()
        
        print(f"\nImport completed successfully!")
        print(f"Total words processed: {words_processed}")
        print(f"Words inserted: {words_inserted}")
        print(f"Words skipped (duplicates): {words_skipped}")
        
        return True
        
    except Exception as e:
        print(f"Error during import: {str(e)}")
        if 'conn' in locals():
            conn.rollback()
            conn.close()
        return False

def insert_word_batch(cursor, batch_words):
    """Insert a batch of words and return counts of inserted and skipped words."""
    inserted = 0
    skipped = 0
    
    for word_data in batch_words:
        try:
            cursor.execute('''
                INSERT INTO words (word, length, source, source_file, original_form, normalized_form)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', word_data)
            inserted += 1
        except sqlite3.IntegrityError:
            # Word already exists (duplicate)
            skipped += 1
        except Exception as e:
            print(f"Error inserting word '{word_data[0]}': {str(e)}")
            skipped += 1
    
    return inserted, skipped

def get_database_stats():
    """Display current database statistics."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(os.path.dirname(script_dir), 'words.db')
    
    if not os.path.exists(db_path):
        print("Database not found.")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get total words count
        cursor.execute('SELECT COUNT(*) FROM words')
        total_words = cursor.fetchone()[0]
        
        # Get words by source
        cursor.execute('''
            SELECT source, COUNT(*) 
            FROM words 
            GROUP BY source 
            ORDER BY COUNT(*) DESC
        ''')
        sources = cursor.fetchall()
        
        # Get words by length distribution
        cursor.execute('''
            SELECT length, COUNT(*) 
            FROM words 
            GROUP BY length 
            ORDER BY length
        ''')
        lengths = cursor.fetchall()
        
        conn.close()
        
        print(f"\nDatabase Statistics:")
        print(f"Total words: {total_words}")
        print(f"\nWords by source:")
        for source, count in sources:
            print(f"  {source}: {count}")
        
        print(f"\nWords by length:")
        for length, count in lengths:
            print(f"  {length} characters: {count}")
            
    except Exception as e:
        print(f"Error getting database stats: {str(e)}")

if __name__ == "__main__":
    print("Lithuanian Words Database Importer")
    print("=" * 40)
    
    # Show current stats before import
    print("Current database state:")
    get_database_stats()
    
    # Ask user for confirmation
    response = input("\nDo you want to proceed with importing words? (y/N): ")
    if response.lower() in ['y', 'yes']:
        success = insert_words_from_file()
        
        if success:
            print("\nUpdated database state:")
            get_database_stats()
        else:
            print("Import failed. Please check the error messages above.")
    else:
        print("Import cancelled.")
