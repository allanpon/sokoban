from PyQt5.QtWidgets import QWidget

class sokobanModel(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.__x = 100
        self.__y = 100
        self.__texturePack = "marioworld"
        self.__player= [0,0]
        self.__nbrePas = 0
        self.__playerImage = "images/"+self.__texturePack+"/perso.png"
        #1 = vide
        #2 = caisse = bleu
        #3 = trou = rouge
        #4 = combi 2 + 3 = violet
        #5 = personnage + trou
        #6 = personnage
        self.__terrain = []
        text = []
        with open('level/1.txt') as f:
            text = f.readlines()

        for line in range(len(text)):
            self.__terrain.append([])
            for letter in range(len(text[line])):
                if (text[line][letter] != '\n'):
                    if (text[line][letter] != "6"):
                        self.__terrain[line].append(int(text[line][letter]))
                    else:
                        self.__player = [line, letter]
                        self.__terrain[line].append(0)

        self.__parent = parent
        self.__view = None
        self.__controller = None
        
    def setView(self,view):
        self.__view = view
        
    def getTexturePack(self):
        return self.__texturePack
    
    def setTexturePack(self,texture):
        self.__texturePack = texture
        self.__playerImage = "images/"+self.__texturePack+"/perso.png"
        self.__view.update()
    
    def getNbrePas(self):
        return self.__nbrePas
    
    def addNbrPas(self):
        self.__nbrePas += 1
        self.__parent.updateStatus()
        
    
    def keepPlaying(self):
        for i in range(len(self.__terrain)):
            if 3 in self.__terrain[i]:
                return True
        return False 
                
                
                
    def setController(self,controller):
        self.__controller = controller
    
    def getView(self):
        return self.__view
    
    def getController(self):
        return self.__controller
        
    def getTerrain(self):
        return self.__terrain
    
    def getJoueur(self):
        return self.__player
    
    def setJoueur(self,joueur):
        self.__joueur = joueur
        
    def getImageJoueur(self):
        return self.__playerImage
    
    def setImageJoueur(self,image):
        self.__playerImage = image
        
        
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def getW(self):
        return self.__w
    
    def getH(self):
        return self.__h
    
    def updatePlayer(self, player):
        self.__player = player
        self.__view.updateView()
