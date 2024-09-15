import random

class MilkModel:
    def __init__(self, model):
        self.model = model

    def milk_cow(self, cow):
        udders = int(cow['Udders'])
        if udders == 4:
            # โอกาส 5% ที่เต้านมจะลดลง
            if random.random() < 0.05:
                cow['Udders'] = '3'
                self.model.save_data()  # บันทึกการเปลี่ยนแปลงไปยัง CSV
                return f"วัว (รหัส: {cow['ID']}) ถูกรีดนมและเสียเต้านมไป 1 เต้า เหลือ {cow['Udders']} เต้า"
            else:
                # คำนวณปริมาณน้ำนมที่ผลิตได้
                milk_amount = self.calculate_milk_production(cow)
                self.model.save_data()  # บันทึกการเปลี่ยนแปลงไปยัง CSV
                return f"วัว (รหัส: {cow['ID']}) ถูกรีดนมสำเร็จ มี {cow['Udders']} เต้า ผลิตน้ำนมได้ {milk_amount} ลิตร"
        return "วัวไม่สามารถรีดนมได้เนื่องจากมีเต้านมไม่ครบ 4 เต้า"

    def calculate_milk_production(self, cow):
        """คำนวณปริมาณน้ำนมจากอายุของวัว"""
        age = cow['Age']
        # ตรวจสอบว่า Age มีข้อมูลหรือไม่เพื่อป้องกันข้อผิดพลาด
        if age:
            years, months = map(int, age.replace(' years ', ' ').replace(' months', '').split())
            milk_amount = years + (months / 12)  # คำนวณน้ำนมจากปีและเดือน
            return round(milk_amount, 2)  # แสดงผลลัพธ์เป็นทศนิยม 2 ตำแหน่ง
        return 0  # คืนค่า 0 ถ้า Age ไม่มีข้อมูล