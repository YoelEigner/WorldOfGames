import sys

from selenium.webdriver.firefox.options import Options
from selenium import webdriver


def test_scores_service(url, element_to_find):
    # firefox_driver = webdriver.Firefox(executable_path="C:\windows\system32\geckodriver.exe")

    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options, executable_path="C:\windows\system32\geckodriver.exe")

    browser.get(url)
    element = browser.find_element_by_id(element_to_find).text
    score = int(element)
    try:
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except BaseException as e:
        pass


def main_function():
    test_score = test_scores_service()

    if test_score != True:
        print("your score table is out of range")
        sys.exit(1)
        
        

main_function()
