# cow_controller.py
from Model.cow_model import CowModel
from Model.milk_model import MilkModel
from Model.udder_change_model import UdderChangeModel

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.milk_model = MilkModel(model)
        self.udder_change_model = UdderChangeModel(model)
        self.total_milk = 0  # กำหนดปริมาณน้ำนมรวม

    def check_animal(self):
        animal_id = self.view.get_id_input()
        if not animal_id.isdigit() or len(animal_id) != 8 or animal_id.startswith('0'):
            self.view.show_message("ID ไม่ถูกต้อง: ต้องเป็นตัวเลข 8 หลักและไม่เริ่มต้นด้วย 0")
            return

        animal = self.model.get_animal_by_id(animal_id)
        if animal is None:
            self.view.show_message("ไม่พบสัตว์ที่มี ID นี้")
        else:
            if animal['Age'] == '':  # หากเป็นแพะ
                self.view.show_message(f"ตรวจพบแพะ (ID : {animal_id}) กรุณไล่มันออกไป!")
                self.view.show_goat_removal_popup()
            else:
                if int(animal['Udders']) == 4:
                    self.view.show_milk_popup()
                else:
                    self.view.show_message("วัวไม่สามารถรีดนมได้เนื่องจากมีเต้านมไม่ครบ 4 เต้า")
                    # เรียกใช้การเปลี่ยนแปลงเต้านม
                    change_message = self.udder_change_model.check_udder_change(animal)
                    if change_message != "ไม่มีการเปลี่ยนแปลงเต้านม":
                        self.view.show_message(change_message)

    def milk_cow(self):
        animal = self.model.get_animal_by_id(self.view.get_id_input())
        milk_message = self.milk_model.milk_cow(animal)
        self.view.show_message(milk_message)

        if "ผลิต" in milk_message and "ลิตร" in milk_message:
            try:
                milk_amount_str = milk_message.split("ผลิต ")[1].split(" ลิตร")[0]
                if milk_amount_str.replace('.', '', 1).isdigit():
                    milk_amount = float(milk_amount_str)
                    self.total_milk += milk_amount
                    self.view.show_message(f"ปริมาณน้ำนมที่ผลิตทั้งหมด: {round(self.total_milk, 2)} ลิตร")
                else:
                    raise ValueError(f"ไม่สามารถแปลงเป็นตัวเลขได้: {milk_amount_str}")
            except (IndexError, ValueError) as e:
                print(f"ข้อผิดพลาดในการแยกข้อความ: {e}")
                self.view.show_message("รีดนมเสร็จแล้วไปกันต่อ")
        else:
            self.view.show_message("ไม่สามารถคำนวณปริมาณน้ำนมได้")

        change_message = self.udder_change_model.check_udder_change(animal)
        if change_message != "ไม่มีการเปลี่ยนแปลงเต้านม":
            self.view.show_message(change_message)

    def remove_goat(self):
        self.view.show_message("ไล่แพะออกจากเครื่องรีดเรียบร้อยแล้ว!")
