import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from model.sokobanModel import sokobanModel
from view.sokobanView import sokobanView
from controller.sokobanController import sokobanController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.__model = sokobanModel(self)
        self.__view = sokobanView(app)
        self.__controller = sokobanController()
        
        self.__tailleStatusBar = 50
        self.setWindowTitle("Sokoban")
        self.setWindowIcon(QIcon('images/surprise.png'))
        self.__model.setView(self.__view)
        
        w = self.__model.getX()*len(self.__model.getTerrain()[0])
        h = self.__model.getY()*len(self.__model.getTerrain())+70
        self.setGeometry(1920 // 3,50, w,h)
        self.setFixedSize(w, h)
        self.setCentralWidget(self.__view)
        
        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)
        self.fenetreMenuBar()
        self.statusBar()
        self.__view.setFocus()

        self.show()

    def fenetreMenuBar(self):
        self.mainMenu = self.menuBar()
        self.setMenuBar(self.mainMenu)

        # Menu
        self.menu = self.mainMenu.addMenu("Menu")

        # Restart (Menu)
        self.restart = QAction("Restart", self)
        self.restart.setShortcut("Ctrl+R")
        self.menu.addAction(self.restart)
        self.restart.triggered.connect(self.restartApplication)

        # Quit (Menu)
        self.quit = QAction("Quit", self)
        self.quit.setShortcut("Ctrl+Q")
        self.menu.addAction(self.quit)
        self.quit.triggered.connect(self.quitterApplication)

        # Texture Pack
        self.texture = self.mainMenu.addMenu("Texture Pack")

        # Mario World | Allan Ponchaut
        self.mw = QAction("Mario World | Allan Ponchaut", self)
        self.texture.addAction(self.mw)
        self.mw.triggered.connect(lambda: self.__model.setTexturePack("marioworld"))

        # Mario 3D | Lucas Girod-Roux
        self.m3D = QAction("Mario 3D | Lucas Girod-Roux", self)
        self.texture.addAction(self.m3D)
        self.m3D.triggered.connect(lambda: self.__model.setTexturePack("mario3D"))

        # Sonic | Antoine Leva
        self.sonic = QAction("Sonic | Antoine Leva", self)
        self.texture.addAction(self.sonic)
        self.sonic.triggered.connect(lambda: self.__model.setTexturePack("sonic"))

        # Beta | Sullyvan Buyse
        self.beta = QAction("Beta | Sullyvan Buyse", self)
        self.texture.addAction(self.beta)
        self.beta.triggered.connect(lambda: self.__model.setTexturePack("beta"))

    def restartApplication(self):
        self.close()
        self.__model = sokobanModel(self)
        self.__view = sokobanView(app)
        self.__controller = sokobanController()

        self.__model.setView(self.__view)
        self.setCentralWidget(self.__view)

        self.__view.setModel(self.__model)
        self.__view.setController(self.__controller)
        self.__controller.setView(self.__view)
        self.__controller.setModel(self.__model)

        self.__view.setFocus()

        self.statusBar.showMessage("Nombre de pas: 0")

        self.show()

    def quitterApplication(self):
        sys.exit(app.exec_())


    def statusBar(self):
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet("min-height:"+str(self.__tailleStatusBar)+";background-color:white;font-size: 36px;")
        self.statusBar.showMessage("Nombre de pas: 0")

    def updateStatus(self):
        self.statusBar.showMessage("Nombre de pas: "+str(self.__model.getNbrePas()))

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

