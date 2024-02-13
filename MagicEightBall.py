import sys
import random

responses = ["It is certain","You may rely on it","As I see it, Yes","Outlook looks good",
             "Most likely","It is decidely so","Without a doubt","Yes,Definetly"]
questions = True

while questions:
    ques = input("What are you wondering about? ")
    if ques == "":
        sys.exit()
    else:
        print(responses[random.randint(0,7)])
