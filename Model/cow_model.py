# cow_model.py
import csv
import os

class CowModel:
    def __init__(self, csv_file='cow_data.csv'):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        cows = []
        file_path = os.path.join(os.path.dirname(__file__), self.csv_file)
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cows.append(row)
        return cows

    def save_data(self):
        """บันทึกข้อมูลที่เปลี่ยนแปลงกลับไปยังไฟล์ CSV"""
        file_path = os.path.join(os.path.dirname(__file__), self.csv_file)
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['ID', 'Age', 'Udders']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
        print("บันทึกข้อมูลสำเร็จ!")

    def get_animal_by_id(self, animal_id):
        for animal in self.data:
            if animal['ID'] == animal_id:
                return animal
        return None
