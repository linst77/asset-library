import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

qt_creator_file = "./resource/mainwindow.ui"
qt_item_file = "./resource/itemview.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
Ui_MainWindow2, QtBaseClass2 = uic.loadUiType(qt_item_file)


#class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#        QtWidgets.QMainWindow.__init__(self)
#        Ui_MainWindow.__init__(self)
#        self.setupUi(self)


# set model for treeview
data = [
        {"type": "Sword", "objects": ["Long Sword", "Short Sword"], "picture": "sword.png"},
        {"type": "Shield", "objects": ["Wood Shield", "iron Shied"], "picture": "shield.png"},
        ]




class QCustomQWidget (QtWidgets.QWidget, Ui_MainWindow2): #, QtGui.QListWidgetItem):

    def __init__ (self,  treeView, parent = None,):
        '''
        setup UI file for item view
        '''

        QtWidgets.QWidget.__init__( self)

        # super(QCustomQWidget, self).__init__(parent)

        self.metaData = {}
        self.treeView = treeView

        # print ( self.treeView)
        # QtGui.QListWidgetItem.__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel    = QtWidgets.QLabel()
        self.textDownQLabel  = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QPushButton()
        self.iconQLabel1      = QtWidgets.QPushButton()
        self.iconQLabel.clicked.connect( self.magic01, )
        self.iconQLabel1.clicked.connect( self.magic, )
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addWidget(self.iconQLabel1, 1)

        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 2)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(255, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')


    def magic01(self):
        # self.treeView.clear()
        # self.treeView.clear()
        model = QtWidgets.QFileSystemModel()
        model.setRootPath( QtCore.QDir.currentPath())
        self.treeView.setModel(model)
        # print ( self.metaData)



    def magic(self):
        # self.treeView.clear()
        # self.treeView.clear()
        model = QtWidgets.QFileSystemModel()
        model.setRootPath( 'C:\\construct')
        self.treeView.setModel(model)
        # print ( self.metaData)

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)
    def setTextDown (self, text):
        self.textDownQLabel.setText(text)
    def setIcon (self, imagePath):
        pass
        #self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))
    def foo_set (self, kw):
        self.metaData = kw
    def foo( self):
        print ( self.metaData)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        '''
        setup main window for the asset library
        '''

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # print ( self.listWidget)
        self.myQListWidget = self.listWidget
        self.p_QWidget = []

        num = 0
        for index, name, icon in [
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png'),
            ('No.4', 'test', 'icon.png'),
            ('No.5', 'test', 'icon.png'),
            ('No.6', 'test', 'icon.png'),
            ('No.7', 'test', 'icon.png'),
            ('No.8', 'test', 'icon.png'),
            ('No.9', 'test', 'icon.png'),
            ('No.10', 'test', 'icon.png'),
            ('No.11', 'test', 'icon.png'),
            ('No.12', 'test', 'icon.png'),
            ('No.13', 'test', 'icon.png'),
            ('No.14', 'test', 'icon.png'),
            ]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget( self.treeView)
            print ( self.treeView)

            # myQCustomQWidget.treeview = 
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.foo_set({"test" : num, "name": name, "this":"works"})
            myQCustomQWidget.setIcon(icon)
            self.p_QWidget.append( myQCustomQWidget)
            # Create QListWidgetItem
            myQListWidgetItem = QtWidgets.QListWidgetItem(self.myQListWidget)
            if num % 2 : myQListWidgetItem.setBackground(QtGui.QColor(245, 245, 245))
            # myQListWidgetItem.setText("test")
            myQListWidgetItem.setToolTip(str(num))
            myQListWidgetItem.setData( QtCore.Qt.UserRole, name)
            num = num + 1
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            # self.connect(self.myQListWidget, SIGNAL('customContextMenuRequested(const QPoint &)'), self.context_menu)

        self.myQListWidget.clicked.connect(self.itemClicked)
        # self.setCentralWidget(self.myQListWidget)

    def context_menu(self):
        menu = QMenu(self)
        menu.addAction("Test01")
        menu.addAction("Test02")
        menu.addAction(":)")
        menu.exec_(QCursor.pos())

    def itemClicked(self):
        widget = self.myQListWidget.itemWidget(self.myQListWidget.currentItem())
        widget.magic()

        #test = self.myQListWidget.selectedItems()[0]
        #print test.data(QtCore.Qt.UserRole)


import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle('Asset Library v0.0.1')
    w.show()
    #app.setStyle("plastique") 
    sys.exit(app.exec_())