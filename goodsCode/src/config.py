#easydict模块用于以属性的方式访问字典的值
from easydict import EasyDict as edict

import os
import glob

_DATASET_NAME_TEST = "goods_test"   # the path of the test document
_DATASET_NAME_TRAIN = "goods_train"   # the path of the train document

# 数据处理
def createPath(dir, dictionary): # 列出文件夹下所有的目录与文件
    lst = os.listdir(dir) 
    idx = 0
    lstLen = len(lst)
    while idx < len(lst):
        # path = os.path.join(dir, lst[idx])
        dictionary[lst[idx]] = idx 
        idx += 1
    return dictionary

def createclass_name(dir, dictionary): # 列出文件夹下所有的目录与文件
    lst = os.listdir(dir) 
    idx = 0
    #lstLen = len(lst)
    while idx < len(lst):
        # path = os.path.join(dir, lst[idx])
        dictionary[idx] = lst[idx]
        idx += 1
    return dictionary

#{'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
dic = createPath(_DATASET_NAME_TRAIN,{})
class_names = createclass_name(_DATASET_NAME_TRAIN,{})
dicLen = len(dic)

#计算图片数目
path_file_number = 0
for key in dic.keys():
    #print(type(key))
    fileName = key
    path_file = glob.glob(_DATASET_NAME_TRAIN+'/' + fileName + '/*.jpg')
    fileLen = len(path_file)
    path_file_number += fileLen

    
cfg = edict({
    'data_path': _DATASET_NAME_TRAIN,   #训练数据集，如果是zip文件需要解压
    'test_path': _DATASET_NAME_TEST,     #测试数据集，如果是zip文件需要解压
    'data_size': path_file_number,
    'HEIGHT': 400,  # 图片高度
    'WIDTH': 200,  # 图片宽度
    '_R_MEAN': 123.68,
    '_G_MEAN': 116.78,
    '_B_MEAN': 103.94,
    '_R_STD': 1,
    '_G_STD': 1,
    '_B_STD':1,
    '_RESIZE_SIDE_MIN': 256,
    '_RESIZE_SIDE_MAX': 512,
    
    'batch_size': 32,
    'num_class': dicLen,     # 分类类别
    'epoch_size': 200,  # 训练次数
    'loss_scale_num':1024,
    
    'prefix': 'resnet-ai',
    'directory': './model_resnet',
    'save_checkpoint_steps': 10,
})