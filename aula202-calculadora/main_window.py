from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(
            self, parent: QWidget | None = None,
            *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #  Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #  Título da janela
        self.setWindowTitle('Calc Python')

    def adjustFixedSize(self):
        #  Última coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widegt: QWidget):
        self.vLayout.addWidget(widegt)
        # self.adjustFixedSize()

    def MakeMsgBox(self):
        return QMessageBox(self)
