import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    #  Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    #  Display
    display = Display()
    display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    #  Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # buttons_grid.addWidget(Button('1'), 0, 0)
    # buttons_grid.addWidget(Button('2'), 0, 1)
    # buttons_grid.addWidget(Button('3'), 0, 2)
    # buttons_grid.addWidget(Button('4'), 1, 0)
    # buttons_grid.addWidget(Button('5'), 1, 1)
    # buttons_grid.addWidget(Button('6'), 1, 2)
    # buttons_grid.addWidget(Button('7'), 2, 0)
    # buttons_grid.addWidget(Button('8'), 2, 1)
    # buttons_grid.addWidget(Button('9'), 2, 2)
    # buttons_grid.addWidget(Button('0'), 3, 0, 1, 3)

    #  Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
