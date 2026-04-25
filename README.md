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

### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Database Sources

The project incorporates eight different Lithuanian word databases:

### 1. **common_voice_17/**
- **Format**: `.tsv` files (Tab-separated values)
- **Content**: Common Voice dataset with Lithuanian sentences and words
- **Source**: https://huggingface.co/datasets/mozilla-foundation/common_voice_17_0/tree/main/transcript/lt

### 2. **Hunspell-Zodynai-ir-gramatika-v.45/**
- **Format**: `.dic` files (Hunspell dictionary format)
- **Content**: General Lithuanian dictionary
- **Source**: https://github.com/Semantika2/Hunspell-Zodynai-ir-gramatika-v.45


### 3. **ispell-lt/**
- **Format**: Various text files (`.zodziai`, `.vardai`, `.veiksmazodziai`, etc.)
- **Content**: Specialized word lists including regular words, names, verbs, and jargon
- **Source**: https://github.com/ispell-lt/ispell-lt

### 4. **Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika/**
- **Format**: `.dic` files (Hunspell format)
- **Content**: Alternative Lithuanian spelling checker dictionary
- **Source**: https://github.com/Semantika2/Lietuviu-kalbos-rasybos-tikrintuvai-bei-Hunspell-zodynai-gramatika

### 5. **Lithuanian-Hunspell-dictionary/**
- **Format**: `.dic` files (Hunspell format)
- **Content**: Lithuanian Hunspell dictionary
- **Source**: https://clarin.vdu.lt/xmlui/handle/20.500.11821/64

### 6. **lithuanian-words-txt/**
- **Format**: `.txt` file
- **Content**: Plain text list of Lithuanian words
- **Source**: https://github.com/giekaton/lithuanian-words-txt

### 7. **SkolintuZodynas/**
- **Format**: `.json` file
- **Content**: Dictionary of borrowed terms in Lithuanian
- **Source**: https://data.gov.lt/datasets/2883/#info

### 8. **vietovardziu_zodynas/**
- **Format**: `.csv` file
- **Content**: Lithuanian place names dictionary
- **Source**: https://data.gov.lt/datasets/2937/

Word Extraction and Normalization

The first phase involves extracting and standardizing all words from the various database formats into a unified format.

## Running the Java Code

If you want to run the latest Java implementation of the word square generator, use `App_Parallelized.java` with a precomputed word list.

### Prerequisites
- Java Development Kit (JDK) installed on your system
- `App_Parallelized.class` compiled from `App_Parallelized.java`
- A word list file (e.g., `8_letters.txt`) generated from the combined word counts

### Generate a Word List

The project uses `combined_word_counts.tsv` as the source for extracting words of specific lengths.

**Using `combine_counts.ipynb` (Recommended):**
1. Open `combine_counts.ipynb` in Jupyter.
2. Run the cells to aggregate word counts from all sources and generate `combined_word_counts.tsv`.
3. Set `n = 8` in the cell that filters the combined word counts.
4. Run the cell that reads `combined_word_counts.tsv` and saves `8_letters.txt`.

### Compile the parallel Java solver

From the repository root:

```powershell
cd "c:\Users\zabit\Documents\GitHub\Lithuanian-Word-Square"
javac App_Parallelized.java
```

### Run the parallel solver with the 8-letter list

```powershell
.\run_parallel_by_ranges_update.bat
```

This batch file launches `App_Parallelized` in four parallel JVM processes, each handling a different range of first-letter indices.

### Example: 8-letter word square run

- Input word list: `8_letters.txt`
- Java source: `App_Parallelized.java`
- Runner: `run_parallel_by_ranges_update.bat`
- Expected behavior: the solver loads `8_letters.txt`, divides the first-letter search range across processes, and searches for 8-letter Lithuanian word squares.

## Exporting Words by Length

The project uses `combined_word_counts.tsv` to extract words of specific lengths for the word square generator.

### Using `combine_counts.ipynb`

1. **Run the aggregation:** Open `combine_counts.ipynb` in Jupyter and run all cells to generate `combined_word_counts.tsv`.

2. **Filter by length:** In the notebook, modify the cell that filters words:
   - Change `n = 8` to your desired word length
   - The notebook will create a file named `{n}_letters.txt` with all words of that length

3. **Output:**
   - Creates a file named `{n}_letters.txt` (e.g., `8_letters.txt`)
   - Contains all unique words of the specified length, one per line
   - Words are filtered from `combined_word_counts.tsv` and sorted alphabetically

**Example:** To export all 5-letter words, set `n = 5` in the notebook and run the filtering cell. This will create `5_letters.txt` with all 5-letter Lithuanian words from the combined corpus.

## Using App.java

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