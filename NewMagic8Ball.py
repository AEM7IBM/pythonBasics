import sys,random,csv

class magic8ball:
    def __init__(self, name):
        self.__name: name
        self.__mQuestions: []
        self.__start_game()

    def __start_game(self):
        mResponses = ["Yes", "It is certain", "No", "Not likely", "Be patient", "Keep Moving Forward", "It's still processing",
                      "Outlook looks good", "Don't get your hopes up"]
        lQuestions = True
        print("Welcome " + self.__name)
        while lQuestions:
            mQues = input("Please ask a question: ")
            mRespond = mResponses[random.randint(0,7)]
            if mQues == "":
                print("Thank you for playing")
                self.__write_questions()
                sys.exit()
            else:
                print(mRespond)
                self.__mQuestions.append(mQues)

    def __write_questions(self):
        f = open("magic_questions.csv", "a", newline="")
        wrt = csv.writer(f)
        for q in self.__mQuestions:
            wrt.writerow([q])
        f.close()