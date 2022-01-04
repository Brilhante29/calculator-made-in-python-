import sys
from math import pow, sqrt
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QGridLayout,
    QLineEdit,
    QSizePolicy,
)

COLOR = "color: #00A2FF; font-weight: 700;"

class Calculator(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Calculadora")
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            "* {background: white; color: #000; font-size: 30px;}"
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.add_btn(QPushButton("7"), 1, 0, 1, 1)
        self.add_btn(QPushButton("8"), 1, 1, 1, 1)
        self.add_btn(QPushButton("9"), 1, 2, 1, 1)
        self.add_btn(QPushButton("+"), 1, 3, 1, 1)
        self.add_btn(
            QPushButton("CE"),
            1,
            4,
            1,
            1,
            lambda: self.display.setText(""),
            COLOR,
        )

        self.add_btn(QPushButton("4"), 2, 0, 1, 1)
        self.add_btn(QPushButton("5"), 2, 1, 1, 1)
        self.add_btn(QPushButton("6"), 2, 2, 1, 1)
        self.add_btn(QPushButton("-"), 2, 3, 1, 1)
        self.add_btn(
            QPushButton("C"),
            2,
            4,
            1,
            1,
            lambda: self.display.setText(self.display.text()[:-1]),
            COLOR,
        )

        self.add_btn(QPushButton("1"), 3, 0, 1, 1)
        self.add_btn(QPushButton("2"), 3, 1, 1, 1)
        self.add_btn(QPushButton("3"), 3, 2, 1, 1)
        self.add_btn(QPushButton("/"), 3, 3, 1, 1)
        self.add_btn(
            QPushButton("x²"),
            3,
            4,
            1,
            1,
            lambda: self.display.setText(str(pow(int(self.display.text()), 2))[:-2]),
            COLOR
        )

        self.add_btn(QPushButton("."), 4, 0, 1, 1, None, COLOR)
        self.add_btn(QPushButton("0"), 4, 1, 1, 1, None, COLOR)
        self.add_btn(
            QPushButton("√"),
            4,
            2,
            1,
            1,
            lambda: self.display.setText(str(sqrt(int(self.display.text())))[:-2]),
            COLOR
            
        )
        self.add_btn(QPushButton("*"), 4, 3, 1, 1, None, COLOR)
        self.add_btn(
            QPushButton("="),
            4,
            4,
            1,
            1,
            self.eval_equal,
            COLOR,
        )

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(self.display.text() + btn.text())
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_equal(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except Exception as e:
            self.display.setText("Conta errada")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec_()
