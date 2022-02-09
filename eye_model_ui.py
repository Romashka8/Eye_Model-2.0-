from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup
import images_qrc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(':\graphics\icon.ico'))
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(71, 167, 106);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.aye_field_bg = QtWidgets.QLabel(self.centralwidget)
        self.aye_field_bg.setGeometry(QtCore.QRect(10, 10, 780, 400))
        self.aye_field_bg.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                        "border: 5px solid rgb(0,    128,    0);")
        self.aye_field_bg.setText("")
        self.aye_field_bg.setPixmap(QtGui.QPixmap(":\graphics\\models/mod30.png"))
        self.aye_field_bg.setObjectName("aye_field_bg")
        self.akk_bg = QtWidgets.QLabel(self.centralwidget)
        self.akk_bg.setGeometry(QtCore.QRect(540, 430, 250, 150))
        self.akk_bg.setStyleSheet("border:2px solid black;")
        self.akk_bg.setText("")
        self.akk_bg.setObjectName("akk_bg")
        self.aye_type_bg = QtWidgets.QLabel(self.centralwidget)
        self.aye_type_bg.setGeometry(QtCore.QRect(270, 430, 250, 150))
        self.aye_type_bg.setStyleSheet("border:2px solid black;")
        self.aye_type_bg.setText("")
        self.aye_type_bg.setObjectName("aye_type_bg")
        self.dist_val_lb = QtWidgets.QLabel(self.centralwidget)
        self.dist_val_lb.setGeometry(QtCore.QRect(160, 430, 60, 40))
        self.dist_val_lb.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border: 3px solid;\n"
                                       "border-color: rgb(0, 128, 0);\n"
                                       "border-right-color: rgb(255, 255, 255);")
        self.dist_val_lb.setObjectName("dist_val_lb")
        self.model_btn = QtWidgets.QPushButton(self.centralwidget)
        self.model_btn.setGeometry(QtCore.QRect(10, 540, 250, 40))
        self.model_btn.setStyleSheet("QPushButton{\n"
                                     "    background-color: rgb(30, 89, 69);\n"
                                     "    border: 3px solid;\n"
                                     "    border-color: rgb(0, 128, 0);\n"
                                     "    }\n"
                                     "\n"
                                     "QPushButton:hover{background-color: rgb(127, 255, 0);    }\n"
                                     "")
        self.model_btn.setObjectName("model_btn")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(217, 430, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("QPushButton{\n"
                                           "    background-color: rgb(30, 89, 69);\n"
                                           "    border: 3px solid;\n"
                                           "    border-bottom: 2px;\n"
                                           "    border-color: rgb(0, 128, 0);\n"
                                           "    }\n"
                                           "\n"
                                           "QPushButton:hover{background-color: rgb(127, 255, 0);}")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(217, 450, 20, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("QPushButton{\n"
                                            "    background-color: rgb(30, 89, 69);\n"
                                            "    border: 3px solid;\n"
                                            "    border-top: 2px;\n"
                                            "    border-color: rgb(0, 128, 0);\n"
                                            "    }\n"
                                            "\n"
                                            "QPushButton:hover{background-color: rgb(127, 255, 0);}")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.dist_lb = QtWidgets.QLabel(self.centralwidget)
        self.dist_lb.setGeometry(QtCore.QRect(80, 440, 80, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dist_lb.setFont(font)
        self.dist_lb.setObjectName("dist_lb")
        self.sm_lb = QtWidgets.QLabel(self.centralwidget)
        self.sm_lb.setGeometry(QtCore.QRect(240, 442, 20, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sm_lb.setFont(font)
        self.sm_lb.setObjectName("sm_lb")
        self.type_lb = QtWidgets.QLabel(self.centralwidget)
        self.type_lb.setGeometry(QtCore.QRect(345, 420, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.type_lb.setFont(font)
        self.type_lb.setObjectName("type_lb")
        self.akk_lb = QtWidgets.QLabel(self.centralwidget)
        self.akk_lb.setGeometry(QtCore.QRect(620, 420, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.akk_lb.setFont(font)
        self.akk_lb.setObjectName("akk_lb")
        self.bliz_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.bliz_rbtn.setGeometry(QtCore.QRect(280, 470, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bliz_rbtn.setFont(font)
        self.bliz_rbtn.setObjectName("bliz_rbtn")
        self.norm_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.norm_rbtn.setGeometry(QtCore.QRect(280, 490, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.norm_rbtn.setFont(font)
        self.norm_rbtn.setObjectName("norm_rbtn")
        self.far_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.far_rbtn.setGeometry(QtCore.QRect(280, 510, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.far_rbtn.setFont(font)
        self.far_rbtn.setObjectName("far_rbtn")
        self.norm_akk_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.norm_akk_rbtn.setGeometry(QtCore.QRect(550, 470, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.norm_akk_rbtn.setFont(font)
        self.norm_akk_rbtn.setObjectName("norm_akk_rbtn")
        self.far_akk_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.far_akk_rbtn.setGeometry(QtCore.QRect(550, 490, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.far_akk_rbtn.setFont(font)
        self.far_akk_rbtn.setObjectName("far_akk_rbtn")
        self.aut_akk_rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.aut_akk_rbtn.setGeometry(QtCore.QRect(550, 510, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aut_akk_rbtn.setFont(font)
        self.aut_akk_rbtn.setObjectName("aut_akk_rbtn")
        MainWindow.setCentralWidget(self.centralwidget)

        # creating RadioButton groups
        self.norm_rbtn.setChecked(True)
        self.aye_type_group = QButtonGroup()
        self.aye_type_group.addButton(self.bliz_rbtn, id=1)
        self.aye_type_group.addButton(self.norm_rbtn, id=2)
        self.aye_type_group.addButton(self.far_rbtn, id=3)

        self.aut_akk_rbtn.setChecked(True)
        self.akk_dist_group = QButtonGroup()
        self.akk_dist_group.addButton(self.norm_akk_rbtn, id=1)
        self.akk_dist_group.addButton(self.far_akk_rbtn, id=2)
        self.akk_dist_group.addButton(self.aut_akk_rbtn, id=3)

        # Set up button functions
        self.model_btn.pressed.connect(self.do_model)
        self.pushButton_plus.pressed.connect(self.increase_dist)
        self.pushButton_minus.pressed.connect(self.decrease_dist)

        # set up values for checking
        self.values = {"Нормальный|Нормальная": "40", "Нормальный|Дальняя": "50",
                       "Близорукий|Нормальная": "30", "Близорукий|Дальняя": "40",
                       "Дальнозоркий|Нормальная": "70", "Дальнозоркий|Дальняя": "80"}
        self.values_means = [self.values[i] for i in self.values]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Модель глаза"))
        self.dist_val_lb.setText(_translate("MainWindow", "0"))
        self.model_btn.setText(_translate("MainWindow", "Смоделировать"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.dist_lb.setText(_translate("MainWindow", "Дистанция = "))
        self.sm_lb.setText(_translate("MainWindow", "СМ"))
        self.type_lb.setText(_translate("MainWindow", "    Тип глаза"))
        self.akk_lb.setText(_translate("MainWindow", "  Аккомодация"))
        self.bliz_rbtn.setText(_translate("MainWindow", "Близорукий"))
        self.norm_rbtn.setText(_translate("MainWindow", "Нормальный"))
        self.far_rbtn.setText(_translate("MainWindow", "Дальнозоркий"))
        self.norm_akk_rbtn.setText(_translate("MainWindow", "Нормальная"))
        self.far_akk_rbtn.setText(_translate("MainWindow", "Дальняя"))
        self.aut_akk_rbtn.setText(_translate("MainWindow", "Автоматическая"))

    def do_model(self):
        if (self.aye_type_group.checkedButton()).text() + "|" + (
        self.akk_dist_group.checkedButton()).text() in self.values:
            self.dist_val_lb.setText((self.values[
                (self.aye_type_group.checkedButton()).text() + "|" + (self.akk_dist_group.checkedButton()).text()]))
            self.aye_field_bg.setPixmap(QtGui.QPixmap(
                f":\graphics\\models/{(self.aye_type_group.checkedButton()).text()}{self.dist_val_lb.text()}.png"))

        else:
            self.aye_field_bg.setPixmap(QtGui.QPixmap(
                f":\graphics\\models/{(self.aye_type_group.checkedButton()).text()}{self.dist_val_lb.text()}.png"))
            self.aut_akk_rbtn.setChecked(True)
        # print(f":\graphics\\models/{(self.aye_type_group.checkedButton()).text()}{self.dist_val_lb.text()}.png")

    def increase_dist(self):
        if int(self.dist_val_lb.text()) < 90:
            new_val = int(self.dist_val_lb.text()) + 10
            self.dist_val_lb.setText(str(new_val))
        else:
            self.dist_val_lb.setText(str(0))

    def decrease_dist(self):
        if int(self.dist_val_lb.text()) > 0:
            new_val = int(self.dist_val_lb.text()) - 10
            self.dist_val_lb.setText(str(new_val))
        else:
            self.dist_val_lb.setText(str(90))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
