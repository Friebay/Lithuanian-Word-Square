import sqlite3
import os

def create_database():
    # Create database in your project directory
    db_path = os.path.join(os.path.dirname(__file__), 'words.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            length INTEGER NOT NULL,
            source TEXT NOT NULL,
            source_file TEXT,
            original_form TEXT,
            normalized_form TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            file_path TEXT,
            total_words INTEGER DEFAULT 0,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create indexes
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_words_length ON words(length)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_words_normalized ON words(normalized_form)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_words_length_normalized ON words(length, normalized_form)')
    cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_words_unique ON words(normalized_form, source)')
    
    # Enable performance optimizations
    cursor.execute('PRAGMA journal_mode = WAL')
    cursor.execute('PRAGMA synchronous = NORMAL')
    cursor.execute('PRAGMA cache_size = 10000')
    cursor.execute('PRAGMA temp_store = MEMORY')
    
    conn.commit()
    conn.close()
    
    print(f"Database created successfully at: {db_path}")

if __name__ == "__main__":
    create_database()