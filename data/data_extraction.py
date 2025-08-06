import os 
import requests
from pathlib import Path

path=f"{Path(__file__).parent}/raw"
os.makedirs(path,exist_ok=True)
url="https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
response=requests.get(url)
with open(os.path.join(path,"data.csv"),mode="wb") as f:
    f.write(response.content)
