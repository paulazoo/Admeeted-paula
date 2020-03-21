def chatbot():
    import random
    import pandas

    minutes = randint(2,4)
    time.sleep(minutes) #do the following every 2 to 4 minutes (random)

    #options (1) icebreaker... (2) trivia question (3) outrageous fact
    value = randint(1,3)
    if(value == 1):
        #chat an icebreaker
        icebreaker_data = pd.read_csv("random_questions.csv", encoding="ISO-8859-1")
        icebreaker = list(icebreaker_data['Question'])
        question_number = randint(0, len(icebreaker))
        #chat icebreaker[question_number]
    elif(value == 2):
        #chat a trivia question
    else:
        #chat an outrageous fact