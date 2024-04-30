class our_quiz:
    def question(self):
        score=0
        first =input("cpu stands for? ")
        if (first.lower() == "centeral processing unit"):
            print("correct")
            score +=1
        else:
            print("incorrect")    
        first =input("GPU stands for? ")
        if (first.lower()== "graphics processing unit"):
            print("correct")
            score +=1
        else:
            print("incorrect")    
        first =input("rom stands for? ")
        if (first.lower() == "read only memory"):
            print("correct")
            score +=1
        else:
            print("incorrect")    
        first =input("ram stands for? ")
        if (first.lower() == "random access memory"):
            print("correct")
            score +=1
            print(score)
        else:
            print("incorrect")    
    def here(self):
        playing=input("want to play? y/n ")
        if (playing.lower() == 'y'):
            print("welcome to my computer quiz")
            self.question()
        else:
            print("Alright") 
teach=our_quiz()    
teach.here()
