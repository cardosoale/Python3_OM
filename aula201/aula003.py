# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys
from PySide6.QtWidgets import (QApplication,
                               QPushButton, QGridLayout, QWidget,
                               QMainWindow)

app = QApplication(sys.argv)
window = QMainWindow()
central_widegt = QWidget()
window.setCentralWidget(central_widegt)
window.setWindowTitle('Meu app')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 40px; color: red')
# botao.show()  # Add o widget na hierarquia e exibe na janela

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
# botao2.show()

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout()
central_widegt.setLayout(layout)
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 2, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


#  status bar
status_bar = window.statusBar()
status_bar.showMessage('Mostra a mensagem na barra de status')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(  # type: ignore
    lambda: slot_example(status_bar))

window.show()
app.exec()  # O loop da aplicação
