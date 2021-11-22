from PyQt5.QtMultimedia import *

class sokobanController:
    def __init__(self):
        self.__model = None
        self.__view = None
        self.__sonBoite = QSound("audio/boite.wav")
        
    def setView(self,view):
        self.__view = view
        
    def setModel(self,model):
        self.__model = model
    
    def checkGauche(self,x,y):
        #0 = vide
        #1 = mur
        #2 = caisse = bleu
        #3 = trou = rouge
        #4 = combi caisse (2) + trou (3) = jaune
        #5 = personnage + trou = rouge foncé
        bouge = False
        if(self.__model.getTerrain()[x][y-1] == 0):
            bouge = True
        elif(self.__model.getTerrain()[x][y-1] == 2):
            if self.__model.getTerrain()[x][y-2] == 0:
                self.__model.getTerrain()[x][y-1] = 0
                self.__model.getTerrain()[x][y-2] = 2
                bouge = True
            elif self.__model.getTerrain()[x][y-2] == 3:
                self.__sonBoite.play()
                self.__model.getTerrain()[x][y-1] = 0
                self.__model.getTerrain()[x][y-2] = 4
                bouge = True
        elif(self.__model.getTerrain()[x][y-1] == 3):
            self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
            bouge = True
        
        elif(self.__model.getTerrain()[x][y-1] == 4):
            if(self.__model.getTerrain()[x][y-2] == 0):
                self.__model.getTerrain()[x][y-1] = 3
                self.__model.getTerrain()[x][y-2] = 2
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
            elif(self.__model.getTerrain()[x][y-2] == 3):
                self.__sonBoite.play()
                self.__model.getTerrain()[x][y-1] = 3
                self.__model.getTerrain()[x][y-2] = 4
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
        if(bouge == True):
            if(self.__model.getTerrain()[x][y] == 3 and self.__model.getTerrain()[x][y-1] == 0):
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/perso.png")
        return bouge
        
    def checkHaut(self,x,y):
        #0 = vide
        #1 = mur
        #2 = caisse = bleu
        #3 = trou = rouge
        #4 = combi 2 + 3 = violet
        #5 = personnage + trou
        bouge = False
        if(self.__model.getTerrain()[x-1][y] == 0):
            bouge = True
        elif(self.__model.getTerrain()[x-1][y] == 2):
            if self.__model.getTerrain()[x-2][y] == 0:
                self.__model.getTerrain()[x-1][y] = 0
                self.__model.getTerrain()[x-2][y] = 2
                bouge = True
            elif self.__model.getTerrain()[x-2][y] == 3:
                self.__sonBoite.play()
                self.__model.getTerrain()[x-1][y] = 0
                self.__model.getTerrain()[x-2][y] = 4
                bouge = True
        elif(self.__model.getTerrain()[x-1][y] == 3):
            self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
            bouge = True
        #0 = vide
        #1 = mur
        #2 = caisse = bleu
        #3 = trou = rouge
        #4 = combi caisse (2) + trou (3) = jaune
        #5 = personnage + trou = rouge foncé
        elif(self.__model.getTerrain()[x-1][y] == 4):
            if(self.__model.getTerrain()[x-2][y] == 0):
                self.__model.getTerrain()[x-1][y] = 3
                self.__model.getTerrain()[x-2][y] = 2
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
            elif(self.__model.getTerrain()[x-2][y] == 3):
                self.__sonBoite.play()
                self.__model.getTerrain()[x-1][y] = 3
                self.__model.getTerrain()[x-2][y] = 4
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
        if(bouge == True):
            if(self.__model.getTerrain()[x][y] == 3 and self.__model.getTerrain()[x-1][y] == 0):
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/perso.png")
        return bouge
    
    def checkDroite(self,x,y):
        bouge = False
        if(self.__model.getTerrain()[x][y+1] == 0):
            bouge = True
        elif(self.__model.getTerrain()[x][y+1] == 2):
            if self.__model.getTerrain()[x][y+2] == 0:
                self.__model.getTerrain()[x][y+1] = 0
                self.__model.getTerrain()[x][y+2] = 2
                bouge = True
            elif self.__model.getTerrain()[x][y+2] == 3:
                self.__sonBoite.play()
                self.__model.getTerrain()[x][y+1] = 0
                self.__model.getTerrain()[x][y+2] = 4
                bouge = True
        elif(self.__model.getTerrain()[x][y+1] == 3):
            self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
            bouge = True
            
        elif(self.__model.getTerrain()[x][y+1] == 4):
            if(self.__model.getTerrain()[x][y+2] == 0):
                self.__model.getTerrain()[x][y+1] = 3
                self.__model.getTerrain()[x][y+2] = 2
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
            elif(self.__model.getTerrain()[x][y+2] == 3):
                self.__sonBoite.play()
                self.__model.getTerrain()[x][y+1] = 3
                self.__model.getTerrain()[x][y+2] = 4
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
                
        if(bouge == True):
            if(self.__model.getTerrain()[x][y] == 3 and self.__model.getTerrain()[x][y+1] == 0):
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/perso.png")
        return bouge
    
    def checkBas(self,x,y):
        bouge = False
        if(self.__model.getTerrain()[x+1][y] == 0):
            bouge = True
        elif(self.__model.getTerrain()[x+1][y] == 2):
            if self.__model.getTerrain()[x+2][y] == 0:
                self.__model.getTerrain()[x+1][y] = 0
                self.__model.getTerrain()[x+2][y] = 2
                bouge = True
            elif self.__model.getTerrain()[x+2][y] == 3:
                self.__sonBoite.play()
                self.__model.getTerrain()[x+1][y] = 0
                self.__model.getTerrain()[x+2][y] = 4
                bouge = True
           
        elif(self.__model.getTerrain()[x+1][y] == 4):
            if(self.__model.getTerrain()[x+2][y] == 0):
                self.__model.getTerrain()[x+1][y] = 3
                self.__model.getTerrain()[x+2][y] = 2
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
            elif(self.__model.getTerrain()[x+2][y] == 3):
                self.__musiqueIntro = QSound("boite.wav")
                self.__musiqueIntro.play()
                self.__model.getTerrain()[x+1][y] = 3
                self.__model.getTerrain()[x+2][y] = 4
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
                bouge = True
        elif(self.__model.getTerrain()[x+1][y] == 3):
            self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/persoP.png")
            bouge = True
            
        if(bouge == True):
            if(self.__model.getTerrain()[x][y] == 3 and self.__model.getTerrain()[x+1][y] == 0):
                self.__model.setImageJoueur("images/"+self.__model.getTexturePack()+"/perso.png")
        return bouge
    
    
    
            
            
        
