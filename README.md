# words
Simple python project to solve "paraulògic" word game.

You can run words.py to find words based on input defined on 
```Python
MAIN_LETTER = "g"
SECONDARY_LETTERS = ["c", "a", "r", "i", "m", "l"]
```

Or you can run ``paraulogic_solver.py`` that will:
1. Use Selenium libraries to open a Chromium browser
2. Extract the letters of the puzzle
3. Run ``get_matching_words_from_file`` from words.py
4. Input the results to the website and store the valid ones.

To run ``paraulogic_solver.py`` you'll need to download the chromedriver that can be found here https://chromedriver.chromium.org/downloads 