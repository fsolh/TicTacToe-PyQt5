from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(-10, -20, 201, 181))
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setMidLineWidth(0)
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(font)
        self.label_1.mouseReleaseEvent = self.clicked_tile1
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, -20, 191, 181))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_2.mouseReleaseEvent = self.clicked_tile2
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, -20, 201, 181))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.label_3.mouseReleaseEvent = self.clicked_tile3
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 160, 201, 181))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.label_4.mouseReleaseEvent = self.clicked_tile4
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 160, 191, 181))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.label_5.mouseReleaseEvent = self.clicked_tile5
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 160, 201, 181))
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)
        self.label_6.mouseReleaseEvent = self.clicked_tile6
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-10, 340, 201, 181))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font)
        self.label_7.mouseReleaseEvent = self.clicked_tile7
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 340, 191, 181))
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font)
        self.label_8.mouseReleaseEvent = self.clicked_tile8
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(380, 340, 201, 181))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font)
        self.label_9.mouseReleaseEvent = self.clicked_tile9
        #-------------------------description label---------------------------
        font = QtGui.QFont()
        font.setPointSize(16)
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 530, 560, 50))
        self.description.setText('You are "O". It is your turn.')
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.description.setFont(font)
        #-----------------------play again/refresh button-------------------
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.refresh())
        self.refreshButton.setGeometry(QtCore.QRect(235, 590, 100, 50))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.setText("Play Again")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #                            |          |
    #-------------------- d1x1y1 |   x1y2   | d2x1y3 ------------------
    #                            |          |
    #                    ----------------------------
    #                            |          |
    #--------------------  x2y1  | d1d2x2y2 |  x2y3 -------------------
    #                            |          |
    #                    ----------------------------
    #                            |          |
    #-------------------- d2x3y1 |   x3y2   | d1x3y3 ------------------
    #                            |          |


    # all tiles dictionary
    tiles_dict = {"d1x1y1": "label_1", 
                "x1y2": "label_2", 
                "d2x1y3": "label_3", 
                "x2y1": "label_4", 
                "d1d2x2y2": "label_5", 
                "x2y3": "label_6", 
                "d2x3y1": "label_7", 
                "x3y2": "label_8",
                "d1x3y3": "label_9"
                }

    # all tiles set
    tiles_set = set(tiles_dict.keys())

    # user selected rows(horizontal, vertical, diagonal) status
    user_dict = {"x1": 0,
                "x2": 0,
                "x3": 0,
                "y1": 0,
                "y2": 0,
                "y3": 0,
                "d1": 0,
                "d2": 0,
                }

    # system selected rows(horizontal, vertical, diagonal) status
    sys_dict = {"x1": 0,
                "x2": 0,
                "x3": 0,
                "y1": 0,
                "y2": 0,
                "y3": 0,
                "d1": 0,
                "d2": 0,
                }

    # selected tiles set
    selected_set = set()

    # a variable to check if the game is finished
    game_over = False

    # defining a funtion to split the tile's name into 2-characters strings and save them in a list
    def split_by_two(line):
        n = 2
        return [line[i:i+n] for i in range(0, len(line), n)]

    # function for system's turn
    def system_select(self):
        winner = ""
        danger_list = []        # horizontal, vertical, or diagonal rows that user have selected 2 tiles from and It's dangerous!
        safe_list = []          # horizontal, vertical, or diagonal rows that user have selected 1 tile from and it's not a danger yet! 
        possible_tiles = []     # tiles that system can select
        for key, value in Ui_MainWindow.user_dict.items():
            if value == 3:  # if 3 tiles in a row is selected it means user has won!
                Ui_MainWindow.game_over = True
                winner = "user"
                return winner
            elif value == 2:  # if 2 tiles in a row is selected it means it's a dangerous row
                danger_list.append(key)
            elif value == 1:  # if 1 tile in a row is selected it means it is still a safe row
                safe_list.append(key)
        available_tiles = Ui_MainWindow.tiles_set - Ui_MainWindow.selected_set
        for tile in available_tiles:
            for danger in danger_list:
                if danger in tile:
                    possible_tiles.append(tile)     # makes a list of dangerous tiles for the system to select from
        if len(possible_tiles)!=0:  # if there are dangerous tiles, it randomly selects one tile from the list
            one_tile = random.choice(possible_tiles)
            Ui_MainWindow.selected_set.add(one_tile)
            sys_selected_list = Ui_MainWindow.split_by_two(one_tile)
            for selected in sys_selected_list:
                Ui_MainWindow.sys_dict[selected] += 1
            tile_label = Ui_MainWindow.tiles_dict[one_tile]
            label = self.centralwidget.findChild(QtWidgets.QLabel, tile_label)
            label.setText("X")
            for key, value in Ui_MainWindow.sys_dict.items(): # checks if the system have 3 tiles in a row and if it has won!
                if value == 3:
                    Ui_MainWindow.game_over = True
                    winner = "system"
                    return winner
            return winner
        else:   # if there are no dangerous tiles it checks the safe tiles
            for tile in available_tiles:
                for safe in safe_list:
                    if safe in tile:
                        possible_tiles.append(tile)
            if len(possible_tiles)==0: # if there are no tiles left to select it means the game is over
                Ui_MainWindow.game_over = True
                winner = "gameover"
                return winner
            one_tile = random.choice(possible_tiles)
            Ui_MainWindow.selected_set.add(one_tile)
            sys_selected_list = Ui_MainWindow.split_by_two(one_tile)
            for selected in sys_selected_list:
                Ui_MainWindow.sys_dict[selected] += 1
            tile_label = Ui_MainWindow.tiles_dict[one_tile]
            label = self.centralwidget.findChild(QtWidgets.QLabel, tile_label)
            label.setText("X")
            for key, value in Ui_MainWindow.sys_dict.items():
                if value == 3:
                    Ui_MainWindow.game_over = True
                    winner = "system"
                    return winner
            return winner
    
    # checking the winner and show a message accordingly
    def check_winner(self, winner):
        if winner == "user":
            self.description.setText("You won!")
        elif winner == "system":
            self.description.setText("You lost!")
        elif winner == "gameover":
            self.description.setText("Game over! It's a tie!")
    
    # tile 1 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile1(self, event):
        if self.label_1.text() != "O" and self.label_1.text() != "X" and not Ui_MainWindow.game_over:
            self.label_1.setText("O")
            Ui_MainWindow.selected_set.add("d1x1y1")
            Ui_MainWindow.user_dict["d1"] += 1
            Ui_MainWindow.user_dict["x1"] += 1
            Ui_MainWindow.user_dict["y1"] += 1
            game = self.system_select()
            self.check_winner(game)
    
    # tile 2 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile2(self, event):
        if self.label_2.text() != "O" and self.label_2.text() != "X" and not Ui_MainWindow.game_over:
            self.label_2.setText("O")
            Ui_MainWindow.selected_set.add("x1y2")
            Ui_MainWindow.user_dict["x1"] += 1
            Ui_MainWindow.user_dict["y2"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 3 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile3(self, event):
        if self.label_3.text() != "O" and self.label_3.text() != "X" and not Ui_MainWindow.game_over:
            self.label_3.setText("O")
            Ui_MainWindow.selected_set.add("d2x1y3")
            Ui_MainWindow.user_dict["d2"] += 1
            Ui_MainWindow.user_dict["x1"] += 1
            Ui_MainWindow.user_dict["y3"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 4 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile4(self, event):
        if self.label_4.text() != "O" and self.label_4.text() != "X" and not Ui_MainWindow.game_over:
            self.label_4.setText("O")
            Ui_MainWindow.selected_set.add("x2y1")
            Ui_MainWindow.user_dict["x2"] += 1
            Ui_MainWindow.user_dict["y1"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 5 function on click event. If it's not occupied or the game is not over, shows "O" on the tile    
    def clicked_tile5(self, event):
        if self.label_5.text() != "O" and self.label_5.text() != "X" and not Ui_MainWindow.game_over:
            self.label_5.setText("O")
            Ui_MainWindow.selected_set.add("d1d2x2y2")
            Ui_MainWindow.user_dict["d1"] += 1
            Ui_MainWindow.user_dict["d2"] += 1
            Ui_MainWindow.user_dict["x2"] += 1
            Ui_MainWindow.user_dict["y2"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 6 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile6(self, event):
        if self.label_6.text() != "O" and self.label_6.text() != "X" and not Ui_MainWindow.game_over:
            self.label_6.setText("O")
            Ui_MainWindow.selected_set.add("x2y3")
            Ui_MainWindow.user_dict["x2"] += 1
            Ui_MainWindow.user_dict["y3"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 7 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile7(self, event):
        if self.label_7.text() != "O" and self.label_7.text() != "X" and not Ui_MainWindow.game_over:
            self.label_7.setText("O")
            Ui_MainWindow.selected_set.add("d2x3y1")
            Ui_MainWindow.user_dict["d2"] += 1
            Ui_MainWindow.user_dict["x3"] += 1
            Ui_MainWindow.user_dict["y1"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 8 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile8(self, event):
        if self.label_8.text() != "O" and self.label_8.text() != "X" and not Ui_MainWindow.game_over:
            self.label_8.setText("O")
            Ui_MainWindow.selected_set.add("x3y2")
            Ui_MainWindow.user_dict["x3"] += 1
            Ui_MainWindow.user_dict["y2"] += 1
            game = self.system_select()
            self.check_winner(game)

    # tile 9 function on click event. If it's not occupied or the game is not over, shows "O" on the tile
    def clicked_tile9(self, event):
        if self.label_9.text() != "O" and self.label_9.text() != "X" and not Ui_MainWindow.game_over:
            self.label_9.setText("O")
            Ui_MainWindow.selected_set.add("d1x3y3")
            Ui_MainWindow.user_dict["d1"] += 1
            Ui_MainWindow.user_dict["x3"] += 1
            Ui_MainWindow.user_dict["y3"] += 1
            game = self.system_select()
            self.check_winner(game)
    
    # refresh funtion to play again
    def refresh(self):
        # get the label names from tiles dictionary
        label_list = Ui_MainWindow.tiles_dict.values()

        # delete the text of all the tiles' labels
        for l in label_list:
            label = self.centralwidget.findChild(QtWidgets.QLabel, l)
            label.setText("")

        # reset the user_dict and sys_dict to 0
        for key in Ui_MainWindow.user_dict.keys():
            Ui_MainWindow.user_dict[key] = 0
        for key in Ui_MainWindow.sys_dict.keys():
            Ui_MainWindow.sys_dict[key] = 0

        #reset the selected tiles to an empty set
        Ui_MainWindow.selected_set.clear()

        # reset the description label
        self.description.setText('You are "O". It is your turn.')

        # reset game_over variable to False
        Ui_MainWindow.game_over = False
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        MainWindow.setWindowIcon(QtGui.QIcon('icons/tic-tac-toe_39453.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
