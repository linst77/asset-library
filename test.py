import sys
from PySide import QtGui, QtCore
from PySide.QtCore import SIGNAL
#from PyQt4 import QtGui

class QCustomQWidget (QtGui.QWidget): #, QtGui.QListWidgetItem):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        # QtGui.QListWidgetItem.__init__(parent)
        self.textQVBoxLayout = QtGui.QVBoxLayout()
        self.textUpQLabel    = QtGui.QLabel()
        self.textDownQLabel  = QtGui.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtGui.QHBoxLayout()
        self.iconQLabel      = QtGui.QPushButton()
        self.iconQLabel1      = QtGui.QPushButton()
        self.iconQLabel1.clicked.connect( self.magic)
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


        self.metaData = {}

    def magic(self):
        print ( self.metaData)
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


	# def iconQLabel.


class exampleQMainWindow (QtGui.QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget = QtGui.QListWidget(self)
        self.p_QWidget = []



        num = 0
        for index, name, icon in [
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png'),
            ('No.4', 'test', 'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.foo_set({"test" : num, "name": name, "this":"works"})
            myQCustomQWidget.setIcon(icon)
            self.p_QWidget.append( myQCustomQWidget)
            # Create QListWidgetItem
            myQListWidgetItem = QtGui.QListWidgetItem(self.myQListWidget)
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
            self.connect(self.myQListWidget, SIGNAL('customContextMenuRequested(const QPoint &)'), self.context_menu)
        self.myQListWidget.clicked.connect(self.itemClicked)            
        self.setCentralWidget(self.myQListWidget)

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


        
app = QtGui.QApplication([])
window = exampleQMainWindow()
window.show()
sys.exit(app.exec_())
