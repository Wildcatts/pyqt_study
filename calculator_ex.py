import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from_class = uic.loadUiType("calculator.ui")[0]

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        # 계산 결과를 표시할 라벨
        self.label = QLabel('0', self)
        self.label.setStyleSheet("font-size: 24px; border: 1px solid black;")
        self.label.setMargin(10)

        # 숫자 버튼 및 연산자 버튼을 담을 레이아웃
        button_layout = QVBoxLayout()

        # 각 버튼 그룹을 생성하고 버튼을 추가합니다.
        button_groups = [
            ['AC', '+/-', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        for button_group in button_groups:
            h_layout = QHBoxLayout()
            for button_text in button_group:
                button = QPushButton(button_text, self)
                button.clicked.connect(self.buttonClicked)
                h_layout.addWidget(button)
            button_layout.addLayout(h_layout)

        # 레이아웃을 수직으로 정렬
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # 현재 입력 중인 값을 저장할 변수
        self.current_input = ""
        # 이전 연산자를 저장할 변수
        self.last_operator = None
        # 이전 연산자 이후에 숫자가 입력되었는지 여부를 저장할 변수
        self.operator_pressed = False

    def buttonClicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == '=':
            try:
                # 현재 입력된 값과 이전에 저장된 연산자를 사용하여 계산 수행
                result = eval(self.current_input)
                self.label.setText(str(result))
                self.current_input = str(result)
            except ZeroDivisionError:
                self.label.setText("Error: Division by zero")
                self.current_input = ""
            except Exception as e:
                self.label.setText("Error")
                self.current_input = ""
            self.operator_pressed = False
        elif button_text == 'C':
            # 현재 입력된 값을 초기화
            self.current_input = ""
            self.label.setText('0')
            self.operator_pressed = False
        elif button_text == 'AC':
            # 모든 값을 초기화
            self.current_input = ""
            self.label.setText('0')
            self.last_operator = None
            self.operator_pressed = False
        elif button_text in ['+', '-', '*', '/']:
            # 연산자를 누른 경우
            if not self.operator_pressed:
                self.current_input += button_text
                self.operator_pressed = True
        elif button_text == '%':
            try:
                # 현재 입력된 값에 100을 나눠준 후 라벨에 표시
                value = float(self.current_input)
                result = value / 100
                self.label.setText(str(result))
                self.current_input = str(result)
            except ZeroDivisionError:
                self.label.setText("Error: Division by zero")
                self.current_input = ""
            except Exception as e:
                self.label.setText("Error")
                self.current_input = ""
        elif button_text == '+/-':
            try:
                # 현재 입력된 값의 부호를 바꿔줌
                value = float(self.current_input)
                result = -value
                self.label.setText(str(result))
                self.current_input = str(result)
            except Exception as e:
                self.label.setText("Error")
                self.current_input = ""
        else:
            # 숫자 또는 소수점 버튼을 누른 경우
            if self.label.text() == '0' or self.operator_pressed:
                # 현재 화면에 표시된 값이 0이거나 연산자를 누른 직후에는 새로운 숫자로 대체
                self.current_input = button_text
                self.operator_pressed = False
            else:
                # 기존 숫자에 숫자나 소수점 추가
                self.current_input += button_text

            self.label.setText(self.current_input)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())