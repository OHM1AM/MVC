import random

class UdderChangeModel:
    def __init__(self, model):
        self.model = model

    def check_udder_change(self, cow):
        udders = int(cow['Udders'])
        if udders == 3:
            # โอกาส 99% วัวจะกลับมามีเต้านม 4 เต้า
            if random.random() < 0.99:
                print(f"ก่อนเปลี่ยนแปลง: วัว (ID: {cow['ID']}) มีเต้านม {cow['Udders']} เต้า")

                # อัปเดตข้อมูลใน cow และใน self.data ด้วย
                cow['Udders'] = '4'
                # ค้นหา cow ใน self.data และอัปเดตข้อมูล
                for item in self.model.data:
                    if item['ID'] == cow['ID']:
                        item['Udders'] = cow['Udders']
                        break

                self.model.save_data()  # บันทึกการเปลี่ยนแปลงไปยัง CSV
                print(f"หลังเปลี่ยนแปลง: วัว (ID: {cow['ID']}) มีเต้านม {cow['Udders']} เต้า")
                return f"วัว (ID: {cow['ID']}) กลับมามีเต้านมครบ 4 เต้า"
        return "ไม่มีการเปลี่ยนแปลงเต้านม"