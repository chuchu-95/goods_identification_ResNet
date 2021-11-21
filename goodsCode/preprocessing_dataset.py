import zipfile
from pathlib import Path
import os

def deleteEmptyFile(dir):
    lst = os.listdir(dir)
    for i in lst:
        p = dir + "//" + i
        if not os.listdir(p): 
            os.rmdir(p)


def zipDocument(path, uzipPath):
    with zipfile.ZipFile(path, 'r') as f:
        for fn in f.namelist():
            extracted_path = Path(f.extract(fn))
            extracted_path.rename(fn.encode('cp437').decode('gbk'))
    deleteEmptyFile(uzipPath)
    
# print(curPath)   
zipDocument("goods_test.zip", "goods_test")
zipDocument("goods_train.zip", "goods_train") 