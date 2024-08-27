import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from interface.models import Materials, Bmaterials, nested


def import_csv_file(path):
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)
        materials = [
            Materials(
                Name = row['Name'],
                Cost_per_Unit = row['Cost_per_Unit'],
                Durability = row['Durability'],
                Strength = row['Strength'],
                Resistance = row['Resistance'],
                Performance = row['Performance'],
                Pressure = row['Pressure'],
                Construction_Cost_Over_Time_Years = row['Construction_Cost_Over_Time_Years'],
                Area_Measurements = row['Area_Measurements'],
                Risk_Score = row['Risk_Score'],
                Material_Score = row['Material_Score']
            )
            for row in reader
            ]
        Materials.objects.bulk_create(materials)

if __name__ == '__main__':
    import_csv_file('D:/S_project/backend/Files/materials.csv')


def import_bcsv_file(path1):
    with open(path1, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Bmaterials.objects.create(
                Name = row['Name'],
                Cost_per_Unit = row['Cost_per_Unit'],
                Durability = row['Durability'],
                Strength = row['Strength'],
                Resistance = row['Resistance'],
                Performance = row['Performance'],
                Pressure = row['Pressure'],
                Construction_Cost_Over_Time_Years = row['Construction_Cost_Over_Time_Years'],
                Area_Measurements = row['Area_Measurements'],
                Risk_Score = row['Risk_Score'],
                Material_Score = row['Material_Score']
            )
if __name__ == '__main__':
    import_bcsv_file('D:/S_project/backend/Files/s_materials.csv')


def import_for_nested(path2):
    with open(path2, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nested.objects.create(
                Name = row['Name'],
                Cost_per_Unit = row['Cost_per_Unit'],
                Durability = row['Durability'],
                Strength = row['Strength'],
                Resistance = row['Resistance'],
                Performance = row['Performance'],
                Pressure = row['Pressure'],
                Construction_Cost_Over_Time_Years = row['Construction_Cost_Over_Time_Years'],
                Area_Measurements = row['Area_Measurements'],
                Risk_Score = row['Risk_Score'],
                Material_Score = row['Material_Score']
            )
if __name__ == '__main__':
    import_for_nested('D:/S_project/backend/Files/materials.csv')


