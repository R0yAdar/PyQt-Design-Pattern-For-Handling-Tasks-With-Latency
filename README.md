# PyQt-Pattern-For-Handling-Tasks-With-Latency

```
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
```
