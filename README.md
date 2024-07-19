# Spelletron
Spelletron is a web-based app for correcting spelling errors using Levenshtein distance. Users paste text, set a maximum letter alternation, and receive suggestions based on a predefined word list. Built with Flask, HTML, and CSS, it offers efficient and customizable spell-checking.
### Project Description: Spelletron

#### Overview

Spelletron is a web-based application designed to help users identify and correct spelling errors in text. Utilizing the Levenshtein distance algorithm, Spelletron offers intelligent suggestions for misspelled words, enabling users to refine their text efficiently.

#### Features

- **Text Input**: Users can paste their text into a designated text box on the web page.
- **Spell Checking**: The application cross-references each word in the input against a list of correctly spelled words.
- **Error Detection**: Words not found in the list are flagged as misspelled.
- **Correction Suggestions**: For each identified misspelling, Spelletron suggests possible corrections based on Levenshtein distance, which measures the number of single-character edits needed to transform one word into another.
- **User Interaction**: Users can select the correct word from a list of suggestions for each misspelled word.
- **Updated Text Display**: After making corrections, the application updates the text and displays the revised version.

#### Technical Details

The backend is built with Flask, a lightweight Python web framework. The frontend is crafted using HTML for structure and CSS for styling, ensuring a user-friendly and visually appealing interface. The Levenshtein distance algorithm calculates the minimal number of edits required to match words, aiding in generating relevant correction suggestions. Spelletron uses a `words.txt` file, containing correctly spelled words, to verify input text.

#### Usage

1. **Paste Text**: Enter text into the provided text box on Spelletron's web page.
2. **Set Maximum Letter Alternation**: Specify the maximum number of allowable letter changes (Levenshtein distance) for suggesting corrections.
3. **Check Spelling**: Submit the text by clicking the "Check Spelling" button.
4. **Review Suggestions**: View suggested corrections for each misspelled word.
5. **Select Corrections**: Choose the correct word from the suggestions.
6. **Update Text**: The application displays the corrected version of the text.

#### Project Structure

```
your_project/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
└── words.txt
```

- **app.py**: Flask application file with backend logic.
- **templates/index.html**: HTML structure of the web page.
- **static/style.css**: CSS file for page styling.
- **words.txt**: Contains correctly spelled words.

#### Running the Application

Ensure Python and Flask are installed. Create the project structure and populate `words.txt`. Start the application with `python app.py` and access it at `http://127.0.0.1:5000/`.

#### Benefits

Spelletron offers an intuitive, efficient way to correct text, with customizable settings for the sensitivity of the spell-checking process.

write only main points for description under 200 words only
