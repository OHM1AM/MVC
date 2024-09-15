# cow_mvc.py
from Model.cow_model import CowModel
from View.cow_view_pyqt import CowView
from Controller.cow_controller import CowController
from PyQt5.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)  # สร้าง QApplication สำหรับ PyQt5
    model = CowModel()  # สร้างโมเดล
    view = CowView(controller=None)  # สร้างวิวโดยไม่เชื่อมต่อกับคอนโทรลเลอร์ก่อน
    controller = CowController(model, view)  # เชื่อมต่อโมเดลและวิวกับคอนโทรลเลอร์
    view.controller = controller  # ตั้งคอนโทรลเลอร์ให้กับวิว
    view.show()  # แสดงหน้าจอโปรแกรม
    sys.exit(app.exec_())  # รันแอปพลิเคชัน GUI

if __name__ == "__main__":
    main()
