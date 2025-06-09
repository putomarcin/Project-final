from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QFileDialog, QComboBox, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal
import sys

class ConverterThread(QThread):
    finished = pyqtSignal(bool, str)
    
    def __init__(self, input_file, output_file, parent=None):
        super().__init__(parent)
        self.input_file = input_file
        self.output_file = output_file
    
    def run(self):
        try:
            # Tutaj logika konwersji
            self.finished.emit(True, "Conversion successful!")
        except Exception as e:
            self.finished.emit(False, str(e))

class ConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Data Format Converter')
        self.setGeometry(100, 100, 500, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Input file selection
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('Input File:'))
        self.input_path = QLineEdit()
        input_layout.addWidget(self.input_path)
        input_btn = QPushButton('Browse...')
        input_btn.clicked.connect(self.browse_input)
        input_layout.addWidget(input_btn)
        layout.addLayout(input_layout)
        
        # Output file selection
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel('Output File:'))
        self.output_path = QLineEdit()
        output_layout.addWidget(self.output_path)
        output_btn = QPushButton('Browse...')
        output_btn.clicked.connect(self.browse_output)
        output_layout.addWidget(output_btn)
        layout.addLayout(output_layout)
        
        # Format selection
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel('Output Format:'))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['JSON', 'XML', 'YAML'])
        format_layout.addWidget(self.format_combo)
        layout.addLayout(format_layout)
        
        # Convert button
        convert_btn = QPushButton('Convert')
        convert_btn.clicked.connect(self.convert)
        layout.addWidget(convert_btn)
        
        central_widget.setLayout(layout)
    
    def browse_input(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Select Input File', '', 
                                            'Data Files (*.json *.xml *.yaml *.yml)')
        if file:
            self.input_path.setText(file)
    
    def browse_output(self):
        file, _ = QFileDialog.getSaveFileName(self, 'Select Output File', '', 
                                             'Data Files (*.json *.xml *.yaml *.yml)')
        if file:
            self.output_path.setText(file)
    
    def convert(self):
        input_file = self.input_path.text()
        output_file = self.output_path.text()
        
        if not input_file or not output_file:
            QMessageBox.warning(self, 'Warning', 'Please select both input and output files!')
            return
        
        self.thread = ConverterThread(input_file, output_file)
        self.thread.finished.connect(self.conversion_done)
        self.thread.start()
    
    def conversion_done(self, success, message):
        if success:
            QMessageBox.information(self, 'Success', message)
        else:
            QMessageBox.critical(self, 'Error', message)

def main():
    app = QApplication(sys.argv)
    gui = ConverterGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
