import sys
from PyQt6.QtWidgets import (QApplication, QLabel,
                              QWidget, QGridLayout,
                                QFormLayout, QLineEdit,
                                  QDialog, QHBoxLayout,
                                    QDialogButtonBox, QMainWindow,
                                    QStatusBar, QToolBar,
                                    QLCDNumber, QListWidget,
                                    QVBoxLayout, QRadioButton)
from PyQt6.QtCore import Qt


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Recipe Book")
        
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
        
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        mainBoxLayout = QHBoxLayout()
        
        inputLayout = QVBoxLayout()
        formLayout = QFormLayout()
        optionsLayout = QHBoxLayout()
        
        recipesLayout = QVBoxLayout()
        ingredientsLayout = QVBoxLayout()

        titleBase = QLabel()
        font = titleBase.font()
        font.setPointSize(15)
        titleBase.setFont(font)
        
        
        inputTitle = titleBase
        inputTitle.setText("Input")
        inputTitle.setAlignment(Qt.AlignmentFlag.AlignTop)
        inputLayout.addWidget(inputTitle)
        
        formLayout.addRow("Item Name: ", QLineEdit())
        formLayout.addRow("Item Category: ", QLineEdit())
        inputLayout.addLayout(formLayout)


        recipeTitle = titleBase
        recipeTitle.setText("Recipes")
        recipeTitle.setAlignment(Qt.AlignmentFlag.AlignBottom)
        recipesLayout.addWidget(recipeTitle)
        recipesLayout.addWidget(QListWidget())

        ingredientsTitle = titleBase
        ingredientsTitle.setText("Ingredients")
        ingredientsTitle.setAlignment(Qt.AlignmentFlag.AlignTop)
        ingredientsLayout.addWidget(ingredientsTitle)
        ingredientsLayout.addWidget(QListWidget())
        
        
        
        

        
        

        mainBoxLayout.addLayout(inputLayout)
        
        
        mainBoxLayout.addLayout(ingredientsLayout)

        
        mainBoxLayout.addLayout(recipesLayout)

        
        
        
        centralWidget = QWidget(self)
        centralWidget.setLayout(mainBoxLayout)
        
        
        self.setCentralWidget(centralWidget)

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)
      
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Status")
        self.setStatusBar(status)

    

        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
class EntryWindow(QDialog):
    def __init__(self):
        super.__init__(parent=Window)
'''
