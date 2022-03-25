import os
import zipfile

os.system('kaggle datasets download -d ryanholbrook/car-or-truck')
with zipfile.ZipFile('car-or-truck.zip', 'r') as zip_ref:
    zip_ref.extractall('input')
os.remove('car-or-truck.zip')
