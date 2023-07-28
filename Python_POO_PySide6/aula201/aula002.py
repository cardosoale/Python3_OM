# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

# type: ignore
import sys
from PySide6.QtWidgets import QApplication, \
    QPushButton, QGridLayout, QWidget

app = QApplication(sys.argv)  # type: ignore
botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red')
# botao.show()  # Add o widget na hierarquia e exibe na janela

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
# botao2.show()

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

central_widegt = QWidget()

layout = QGridLayout()
central_widegt.setLayout(layout)
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)

central_widegt.show()  # Central widget entre na
# hierarquia e mostre sua janela.
app.exec()  # O loop da aplicação
