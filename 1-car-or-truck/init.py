import os
import zipfile

file = 'car-or-truck.zip'
os.system('kaggle datasets download -d ryanholbrook/car-or-truck')
with zipfile.ZipFile(file, 'r') as zip_ref:
    zip_ref.extractall('input/car-or-truck')
os.remove(file)
