import time

from words import get_matching_words_from_file
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# https://chromedriver.chromium.org/downloads
s = Service('./chromedriver.exe')

driver = webdriver.Chrome(service=s)


# returns True if word is valid on the website or False if is not
def input_word(word):
    # print("Trying word " + word)
    input_word_box = driver.find_element(By.ID, "test-word")
    driver.execute_script("arguments[0].innerText = '{}'".format(word), input_word_box)
    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()
    result_web = driver.find_element(By.ID, "message")
    if "+" in result_web.text.lower():
        return True
    else:
        return False


time.sleep(1)
driver.get("https://vilaweb.cat/paraulogic/")
time.sleep(1)
driver.refresh()
time.sleep(1)

grid = driver.find_element(By.ID, "hex-grid")
time.sleep(1)
words = grid.text.lower().split("\n")
time.sleep(1)
# middle letter is the main_letter
word = words[3]
words = words[0: 3] + words[4:]

print(word)
print(words)

word_results = get_matching_words_from_file('catalan_dictionary.txt', word, words)

print(word_results)

valid_words = []

for word in word_results:
    time.sleep(0.2)
    if input_word(word):
        valid_words.append(word)

print(valid_words)
