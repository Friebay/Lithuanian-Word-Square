# Lithuanian Word Square Generator

This project aims to find the largest possible word square using Lithuanian words. A word square is an arrangement of words where the nth row reads the same as the nth column.

## Project Overview

This project uses multiple Lithuanian word databases to maximize the vocabulary available for creating word squares. The databases contain words from various sources including dictionaries, place names, borrowed terms, and more.

## Installation and Setup

Follow these steps to set up the Lithuanian Word Square Generator on your local machine:

### Step 1: Clone the Repository

```bash
git clone https://github.com/Friebay/Lithuanian-Word-Square.git
cd Lithuanian-Word-Square
```

### Step 2: Set Up the Database

The project uses an SQLite database to store all Lithuanian words. You have two options:

#### Option A: Use Pre-built Database
TODO: add link

#### Option B: Build Database from Source Data
Run the database setup script and create the database yourself:

```bash
python setup_database.py
```

## Database Sources

The project incorporates seven different Lithuanian word databases:

### 1. **common_voice_17/**
- **Format**: `.tsv` files (Tab-separated values)
- **Content**: Common Voice dataset with Lithuanian sentences and words
- **Structure**: Tab-separated format with sentence data
- **Source**: https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0

### 2. **Hunspell-Zodynai-ir-gramatika-v.45/**
- **Format**: `.dic` files (Hunspell dictionary format)
- **Content**: General Lithuanian dictionary
- **Structure**: Each line contains a word followed by grammatical information
- **Example**: `abakas/7	5` (word with morphological flags)

### 2. **ispell-lt/**
- **Format**: Various text files (`.zodziai`, `.vardai`, `.veiksmazodziai`, etc.)
- **Content**: Specialized word lists including regular words, names, verbs, and jargon
- **Structure**: Plain text with some grammatical annotations
- **Source**: https://github.com/ispell-lt/ispell-lt
- **Files**:
  - `lietuviu.zodziai` - General words
  - `lietuviu.vardai` - Personal names
  - `lietuviu.veiksmazodziai` - Verbs
  - `lietuviu.jargon` - Slang/jargon terms

### 3. **Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika/**
- **Format**: `.dic` files (Hunspell format)
- **Content**: Alternative Lithuanian spelling checker dictionary
- **Purpose**: Provides additional word variants and forms
- **Source**: https://github.com/Semantika2/Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika

### 4. **Lithuanian-Hunspell-dictionary/**
- **Format**: `.dic` files (Hunspell format)
- **Content**: Lithuanian Hunspell dictionary
- **Structure**: Standard Hunspell dictionary format
- **Source**: https://clarin.vdu.lt/xmlui/handle/20.500.11821/64

### 5. **lithuanian-words-txt/**
- **Format**: `.txt` file
- **Content**: Plain text list of Lithuanian words
- **Structure**: One word per line, alphabetically sorted
- **Example**: `a`, `AB`, `Abakai`, `Abarauskai`
- **Source**: https://github.com/giekaton/lithuanian-words-txt

### 6. **SkolintuZodynas/**
- **Format**: `.json` file
- **Content**: Dictionary of borrowed terms in Lithuanian
- **Structure**: JSON with detailed entries including etymology, definitions, and translations
- **Features**: Contains accented forms, synonyms, and multilingual translations
- **Source**: https://data.gov.lt/datasets/2883/#info

### 7. **vietovardziu_zodynas/**
- **Format**: `.csv` file
- **Content**: Lithuanian place names dictionary
- **Structure**: CSV with columns for place codes, full names, grammatical forms, etc.
- **Fields**: `vietovardis` (place name), `linksniai` (declensions), `vietovardzio_rusis` (type)
- **Source**: https://data.gov.lt/datasets/2937/

## Step 1: Word Extraction and Normalization

The first phase involves extracting and standardizing all words from the various database formats into a unified format.

### Extraction Process

#### 1. **Hunspell Dictionary Processing** (`.dic` files)
- Parse each line to extract the base word (before `/` or grammatical markers)
- Remove morphological flags and numerical codes
- Handle special characters and diacritics properly

#### 2. **Text File Processing** (`.txt`, `.zodziai`, etc.)
- Read line by line
- Remove grammatical annotations (e.g., `/D`, `/BUN`)
- Extract clean word forms

#### 3. **JSON Processing** (`SkolintuZodynas`)
- Parse CSV structure to extract `terminas`

#### 4. **CSV Processing** (`vietovardziu_zodynas`)
- Parse CSV structure to extract `vietovardis_pilnas_nekirciuotas`

### Output Format Options

Given the computational intensity of word square generation, multiple output formats will be created:

#### **Primary Storage: SQLite Database** (`words.db`)

### Data Quality Considerations

- **Character Encoding**: Ensure proper handling of Lithuanian diacritics (ą, č, ę, ė, į, š, ų, ū, ž)
- **Case Normalization**: Store both original and lowercase forms
- **Length Filtering**: Pre-compute length statistics for algorithm optimization
- **Frequency Data**: Track word usage frequency for prioritization

### Implementation
- **Python**
- **SQLite**

## Running the Java Code

If you want to run the Java implementation of the word square generator:

### Prerequisites
- Java Development Kit (JDK) installed on your system

## Exporting Words by Length

The project includes a Python script to export words of specific lengths from the database:

### Using export_words.py

1. **Modify the script** to specify your desired word length:
   - Open `export_words.py`
   - Change the parameter in the last line: `export_n_length_words(10)` 
   - Replace `10` with your desired word length

2. **Run the script:**
   ```bash
   python export_words.py
   ```

3. **Output:**
   - Creates a file named `{length}_length_words.txt` (e.g., `10_length_words.txt`)
   - Contains all unique words of the specified length, one per line
   - Words are exported in lowercase and sorted alphabetically

**Example:** To export all 5-letter words, change the script to `export_n_length_words(5)` and run it. This will create `5_length_words.txt` with all 5-letter Lithuanian words from the database.

### Using App.java

The Java word square generator is based on the algorithm from [matevz-kovacic/word-square](https://github.com/matevz-kovacic/word-square) and has been modified to work with Lithuanian letters and the Lithuanian alphabet.

1. **Compile the Java Code:**
   ```bash
   javac App.java
   ```

2. **Run the Compiled Program:**
   ```bash
   java App
   ```

This will compile the `App.java` file and then execute the main application.