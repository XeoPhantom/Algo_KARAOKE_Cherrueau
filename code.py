#Je défenie mes classes de joueurs par les cathégorie suivante (Speudo, chanson et score)
class Player:
     def __init__(self, speudo, chansontest, score):
         self.speudo = speudo
         self.chansontest = chansontest
         self.score = score

p1 = Player("Prometeus", "voyage voyage", 80)
p2 = Player("Guy", "voyage voyage", 70)
p3 = Player("Jesus", "voyage voyage", 50)
p4 = Player("Jesus Le retour", "voyage voyage", 80)

print("le speudo du  joueurs 1 est " + p1.speudo)
print("la chanson chanter récament par le joueur2 est" + p2.chansontest)
print("le speudo entrer par le joueur 4 est" + p4.speudo)
print(p3.score)

class Karaoke:
     def __init__(self, chanson1, point):
        self.chanson1 = chanson1
        self.point = point


ch1 = Karaoke("chanson.py", 50)
ch2 = Karaoke("hello word", 50)
ch3 = Karaoke("sous le vent", 50)
ch4 = Karaoke("everybody is kungfu fighting", 50)

#print(ch3.chanson1)
#print(ch4.point)
#print(ch1.chanson1)
#print(ch2.chanson1)
#test pour voir si tout vas bien 

print("bienvenue dans la partie de Karaoke de nombreux joueurs propose leur performance aujourd'hui")
participation = input("voulez vous participer?:" 1/"non" 2/ "oui")

    if 1 print("très bien passer une bonne journée") :

    else 2 print("parfait vous serez le joueur 01") :
        choixchanson = input("choissisez une chanson :" 1/"chanson.py" 2/"hello word" )
            
            if 1 ch1 =  Karaoke("chanson.py", 70) 
                print(ch1.point)
                p1 = Player("Joueur 01", "chanson.py", 70)
                print(p1.chansontest)
                print(p1.speudo)

            else 2
                print(ch2.point)
            
