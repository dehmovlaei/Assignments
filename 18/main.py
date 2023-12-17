import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    if buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X":
        msgBox = QMessageBox()
        msgBox.setText(f"Player_{player} Has WIN This Turn")
        msgBox.setWindowTitle("Congratulations!")
        msgBox.exec()
def play(row, col):
    global player
    if player == 1 and buttons[row][col].text() == "":
        buttons[row][col].setText("X")
        player = 2
    elif player == 2 and buttons[row][col].text() == "":
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: rgb(241, 178, 55); background-color: rgb(31, 53, 64)")
        player = 1
    check()

player = 1
loader = QUiLoader()
app = QApplication(sys.argv)
ui = loader.load("mainWindow.ui")
ui.show()

buttons = [[ui.btn_1, ui.btn_2, ui.btn_3],
          [ui.btn_4, ui.btn_5, ui.btn_6],
          [ui.btn_7, ui.btn_8, ui.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

app.exec()