# cow_view_pyqt.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CowView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("ระบบจัดการรีดนมวัวและตรวจสอบแพะ")
        self.setGeometry(100, 100, 500, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.title_label = QLabel("ระบบจัดการรีดนมวัวและตรวจสอบแพะ")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.id_label = QLabel("กรุณาใส่ ID:")
        self.id_label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.id_label)

        self.entry = QLineEdit()
        self.entry.setFont(QFont("Arial", 12))
        self.entry.setPlaceholderText("ใส่รหัสวัวหรือแพะที่นี่")
        self.layout.addWidget(self.entry)

        self.check_button = QPushButton("ตรวจสอบ")
        self.check_button.setFont(QFont("Arial", 12))
        self.check_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px;")
        self.check_button.clicked.connect(self.check_animal)
        self.layout.addWidget(self.check_button)

        self.status_label = QLabel("")
        self.status_label.setFont(QFont("Arial", 12))
        self.status_label.setStyleSheet("color: red;")
        self.layout.addWidget(self.status_label)

    def get_id_input(self):
        return self.entry.text()

    def show_message(self, message):
        self.status_label.setText(message)
        QMessageBox.information(self, "ข้อมูล", message)

    def check_animal(self):
        self.controller.check_animal()

    def show_goat_removal_popup(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("ตรวจพบแพะ")
        msg_box.setText("ตรวจพบแพะ กรุณาไล่แพะออกจากเครื่องรีด!")
        msg_box.setIcon(QMessageBox.Warning)
        remove_button = msg_box.addButton("ไล่แพะออก", QMessageBox.AcceptRole)
        cancel_button = msg_box.addButton("ยกเลิก", QMessageBox.RejectRole)

        msg_box.exec_()

        if msg_box.clickedButton() == remove_button:
            self.controller.remove_goat()
        elif msg_box.clickedButton() == cancel_button:
            self.show_message("ยกเลิกการไล่แพะออกจากเครื่องรีด")

    def show_milk_popup(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("รีดนมวัว")
        msg_box.setText("วัวสามารถรีดนมได้ กดปุ่มเพื่อรีดนม")
        msg_box.setIcon(QMessageBox.Information)
        milk_button = msg_box.addButton("รีดนม", QMessageBox.AcceptRole)
        cancel_button = msg_box.addButton("ยกเลิก", QMessageBox.RejectRole)

        msg_box.exec_()

        if msg_box.clickedButton() == milk_button:
            self.controller.milk_cow()
        elif msg_box.clickedButton() == cancel_button:
            self.show_message("ยกเลิกการรีดนม")
