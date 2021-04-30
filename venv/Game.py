import random

class Game:
    def __init__(self):
         self.__sentences=self.get_sentences("C:/DATA/xt.txt")

         self.__last_letter="p"
         self.__numTrying=0
         self.__this_sentence=""
         self.__sentence=self.choose_sentences()
         self.__sentenceToShow=self.__init_sentence_to_show()
         self.__isWinning="false"

    def getLastLetter(self):
        return self.__last_letter
    def getIsWinning(self):
        return self.__isWinning

    def upNumTrying(self):
        self.__numTrying+=1

    def getThisSentence(self):
        return self.__sentence
    def setThisSentence(self):
        self.__this_sentence+="-"

    def get_sentences(self,path):

        with open(path) as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
        return lines


    def choose_sentences(self):
        length=len(self.__sentences)
        y=random.randint(0,(length-1))
        z=self.__sentences[y]
        for i in range(len(z)):
            self.__this_sentence=self.__this_sentence+"-"
        return z


    def __init_sentence_to_show(self):
        self.upNumTrying()
        s=str(self.__sentence)
        z=6
        zz=len(self.__sentence)-1
        return (s[0:zz])
    

    def  update_sentence_to_show(self,letter):
        x=self.__sentence
        w=""
        for i in range(len(x)):
            if (x[i]==letter):
                w=w+letter
            else:
                w=w+self.__this_sentence[i]
        self.__this_sentence=w





    def check_winning(self):
        flag="true"
        for i in range(len(self.__this_sentence)-1):
            if self.__this_sentence[i]=="-":
                flag="false"
        if flag=="true":
            self.__isWinning="true"
            print(f"you win in {self.__numTrying} times to find the word {self.__sentence}")
        return flag

    def show_page(self):
        print(self.__sentence)

    def enter_letter(self):
        yourLetter=input("press a letter! ")
        print(yourLetter)
        self.__last_letter=yourLetter