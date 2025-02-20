#!/usr/bin/python3
from random import randint
import pandas as pd
import time

def chatbot():
    time_length = 10

    for x in range(0, 10*60):
        minutes = randint(1,3)
        time.sleep(minutes) #do the following every 1 to 3 minutes (random)

        #options (1) icebreaker... (2) trivia question (3) outrageous fact
        value = randint(1,3)
        if(value == 1):
            #chat an icebreaker
            icebreaker_data = pd.read_csv("random_questions.csv", encoding="ISO-8859-1")
            icebreaker = list(icebreaker_data['Question'])
            question_number = randint(0, len(icebreaker))
            print("Question #" + str(question_number) + ": " + str(icebreaker[question_number]))

        elif(value == 2):
            #chat trivia and then 10 seconds later an answer
            trivia_data = pd.read_csv("random_trivia.csv", encoding="ISO-8859-1")
            trivia = list(trivia_data['Trivia'])
            answer = list(trivia_data['Answer'])
            trivia_number = randint(0, len(trivia))
            print("Trivia #" + str(trivia_number) + ": " + str(trivia[trivia_number]))
            time.sleep(10)
            print(answer[trivia_number])
            #chat a trivia question  

        else:
            #chat an outrageous fact
            fact_data = pd.read_csv("random_facts.csv", encoding="ISO-8859-1")
            fact = list(fact_data['Fact'])
            fact_number = randint(0, len(fact))
            print("Fact #" + str(fact_number) + ": " + str(fact[fact_number]))
        
        time.sleep(time_length)

chatbot()