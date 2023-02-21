from PyQt6 import QtWidgets, QtCore

class LoginTask(QtCore.QThread):
    result = QtCore.pyqtSignal(bool)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
    
    def run(self):
        from time import sleep
        sleep(6) # latency
        self.result.emit(True)       

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.threads = []
        self.container = QtWidgets.QVBoxLayout()

        self.button = QtWidgets.QPushButton("Login")
        self.anotherButton = QtWidgets.QPushButton("Clicky")

        self.container.addWidget(self.button)
        self.container.addWidget(self.anotherButton)

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.container)
        self.setCentralWidget(self.widget)
        self.button.clicked.connect(self.clicked_upon)
        self.anotherButton.clicked.connect(self.parallel)

    @QtCore.pyqtSlot()
    def clicked_upon(self):
        self.button.setEnabled(False)
        
        login_task = LoginTask()
        self.threads.append(login_task) # Avoid Being Garbage Collected
        login_task.start()
        login_task.result.connect(lambda result: after_clicked(self, result))
        
        def after_clicked(self: MainWindow, result):
            print(result)
            self.button.setEnabled(True)

    
    def parallel(self):
        self.button.setText(self.button.text() + '!')                



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())