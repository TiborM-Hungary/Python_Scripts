from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt

"""
PyQt consists of:
Widgets, signals and slots
btn.clicked.connect(make_sentence)
Widget: btn
Signal: clicked
Slot(a function call): show_currency
"""


# Slots (Functions)

def open_files():
    global filenames
    # 2 inputs:
    # list of file names (absolute path) -> filenames
    # _ -> is for some additional info that is returned by getOpenFileNames(), we don't care hence the '_'
    # window -> variable holding the Q widget
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
    upper_message.setText('Following files are selected for destruction:')
    buttom_message.setText('\n'.join(filenames))


def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            # write an empty byte 'text' into the file, safe deletion method
            file.write(b'')
        # delete path (file associated with that path object)
        path.unlink()
    upper_message.setText('')
    buttom_message.setText('Destruction Successful!')


# Window
app = QApplication([])
window = QWidget()

# Widgets
# --Can use HTML tags in QLabel
description = QLabel(
    'Select the files your want to destroy. The files will be <font color="red">permanently</font> deleted.'
)

# Button 01
open_btn = QPushButton('Open Files')
open_btn.setToolTip('Select files for destruction')
open_btn.setFixedWidth(100)
open_btn.clicked.connect(open_files)

# Button 02
destroy_btn = QPushButton('Destroy Files')
open_btn.setToolTip('Destroy previously selected files')
destroy_btn.setFixedWidth(100)
destroy_btn.clicked.connect(destroy_files)

# Label 01 and Label 02
upper_message = QLabel('')
buttom_message = QLabel('')

# Layout
layout = QVBoxLayout()
layout.addWidget(description)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
layout.addWidget(upper_message)
layout.addWidget(buttom_message, alignment=Qt.AlignmentFlag.AlignCenter)

# Window settings
window.setWindowTitle('File Destroyer')
window.setLayout(layout)
window.show()
app.exec()
