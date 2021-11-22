from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys


class sokobanView(QWidget):
    def __init__(self,app,parent = None):
        super().__init__()
        self.__model = None
        self.__controller = None
        self.__compteur = None
        self.__caisse = True
        self.__musiqueMouvement = QSound("audio/bruit1.wav")
        self.__app = app
        self.__parent = parent
        
    def getModel(self):
        return self.__model
    
    def getController(self):
        return self.__controller
    
    def setModel(self,model):
        self.__model = model
        
    def setCompteur(self,compteur):
        self.__compteur = compteur
        
    def setController(self,controller):
        self.__controller = controller
        
    def getParent(self):
        return self.__parent
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        model = self.__model
        terrain = model.getTerrain()
        if self.__model.keepPlaying() == False:
            self.__app.quit()
        for i in range(len(terrain)):
            for j in range(len(terrain[i])):
                r = QRect(j*model.getY(),i*model.getX(), model.getX(), model.getY())
                case = terrain[i][j]
                if(i == model.getJoueur()[0] and j == model.getJoueur()[1]):
                    if case != 3:
                        image_path = self.__model.getImageJoueur()
                        pixmap = QPixmap(image_path)
                        pixmap = pixmap.scaled(r.size())
                        painter.drawPixmap(r, pixmap)
                elif(case == 1):
                    image_path = "images/"+self.__model.getTexturePack()+"/mur.png"
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(r.size())
                    painter.drawPixmap(r, pixmap)
                elif(case == 2):
                    image_path = "images/"+self.__model.getTexturePack()+"/pousse.png"
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(r.size())
                    painter.drawPixmap(r, pixmap)
                elif(case == 3):
                    image_path = "images/"+self.__model.getTexturePack()+"/trou.png"
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(r.size())
                    painter.drawPixmap(r, pixmap)
                elif(case == 4):
                    image_path = "images/"+self.__model.getTexturePack()+"/pousseT.png"
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(r.size())
                    painter.drawPixmap(r, pixmap)
                if(case == 3 and i == model.getJoueur()[0] and j == model.getJoueur()[1]):
                    r = QRect(j*model.getY(),i*model.getX(), model.getX(), model.getY())
                    image_path = "images/"+self.__model.getTexturePack()+"/persoP.png"
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(r.size())
                    painter.drawPixmap(r, pixmap)
        
    def getCaisse(self):
        return self.__caisse
    
    def keyPressEvent(self,event):
        fleche = event.key() - 16777234
        joueur = self.__model.getJoueur()
        control = self.getController()
        if(fleche == 0):
            self.__musiqueMouvement.play()
            if(control.checkGauche(joueur[0],joueur[1])):
                self.__model.updatePlayer([joueur[0],joueur[1]-1])
                self.__model.addNbrPas()
         
        elif(fleche == 1):
            self.__musiqueMouvement.play()
            if(control.checkHaut(joueur[0],joueur[1])):
                self.__model.updatePlayer([joueur[0]-1,joueur[1]])
                self.__model.addNbrPas()
                
        elif(fleche == 2):
            self.__musiqueMouvement.play()
            if(control.checkDroite(joueur[0],joueur[1])):
                self.__model.updatePlayer([joueur[0],joueur[1]+1])
                self.__model.addNbrPas()
                
                

        elif(fleche == 3):
            self.__musiqueMouvement.play()
            if(control.checkBas(joueur[0],joueur[1])):
                self.__model.updatePlayer([joueur[0]+1,joueur[1]])
                self.__model.addNbrPas()
    
        if not self.__model.keepPlaying():
            self.__caisse = False
        
    def updateView(self):
        self.update()
        
        
