#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from termcolor import colored
import csv
import pyautogui

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
print(colored("Driver successfully created as Firefox headless...", "green"))

with open('random_facts.csv', 'w') as f:
        csvwriter = csv.writer(f)
        headers = ["Fact"]
        csvwriter.writerow(headers)

"""
#Random Question Maker - seems like they have a small number of different questions
driver.get("https://randomquestionmaker.com/")

for x in range(0,1000):
    question_div = driver.find_element_by_class_name("col-md-12.dashed")
    question = question_div.find_element_by_tag_name("span").text
    with open('random_questions.csv', 'a') as f:
        csvwriter = csv.writer(f)
        headers = [question]
        csvwriter.writerow(headers)
    time.sleep(.5) #the refresh button needed 0.5 seconds to wait due to the animation
    driver.find_element_by_id("refresh").click()
    time.sleep(.5)
    #only 24 different questions...

#Conversation Starter World - supposedly 1700 unique questions
driver.get("https://conversationstartersworld.com/random-question-generator/")
time.sleep(3)
for x in range(0, 3000): #in order to get most if not all of the questions
    question_div = driver.find_element_by_class_name("quotescollection-quote")
    question = question_div.find_element_by_tag_name("p").text
    with open('random_questions.csv', 'a') as f:
        csvwriter = csv.writer(f)
        headers = [question]
        csvwriter.writerow(headers)

    outer_div = driver.find_element_by_id("tf_quotescollection_1")
    button = outer_div.find_element_by_class_name("nav-next") #issue finding this element (the next button)
    button.click()
    time.sleep(0.5)

    print(str(x) + " done...")


#Conversation Starters
driver.get("https://www.conversationstarters.com/generator.php")

for x in range(0, 1000): #in order to get most if not all of the questions
    question = driver.find_element_by_id("random").text
    with open('random_questions.csv', 'a') as f:
        csvwriter = csv.writer(f)
        headers = [question]
        csvwriter.writerow(headers)
    button = driver.find_element_by_class_name("button")
    button.click()
    print(str(x) + " done...")
"""

driver.get("http://randomfactgenerator.net/")
for x in range(0, 500):
    facts = driver.find_elements_by_id("z")
    for x in range(0, len(facts)):
        with open('random_facts.csv', 'a') as f:
            csvwriter = csv.writer(f)
            headers = [facts[x].text]
            csvwriter.writerow(headers)
    driver.refresh()
    print(str(x) + " done...")