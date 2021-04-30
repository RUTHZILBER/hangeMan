from Game import Game

def main():
    g = Game()
    print(g.getThisSentence())
    while g.getIsWinning() != "true":
         g.upNumTrying()
         g.enter_letter()
         g.update_sentence_to_show(g.getLastLetter())
         g.check_winning()

if __name__ == '__main__':
    main()