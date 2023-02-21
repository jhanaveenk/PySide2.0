import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice


# class MainWindow(QMainWindow):

#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#       #   self.button_is_checked = True

#         self.button = QPushButton("Press Me!")
#       #   self.button.setCheckable(True)
#         self.button.clicked.connect(self.the_button_was_clicked)
#       #   self.button.clicked.connect(self.the_button_was_toggled)

#         # Set the central widget of the Window.
#         self.setCentralWidget(self.button)

#    #  def the_button_was_clicked(self):
#    #      print("Clicked!")

#    #  def the_button_was_toggled(self, checked):
#    #    self.button_is_checked = checked

#    #    print(self.button_is_checked)


#     def the_button_was_clicked(self):
#         self.button.setText("You already clicked me.")
#         self.button.setEnabled(False)

#         # Also change the window title.
#         self.setWindowTitle("My Oneshot App")


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)
        

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)


    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)








app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()