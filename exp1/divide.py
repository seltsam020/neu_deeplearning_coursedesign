'''
Author: seltsam020 73098253+seltsam020@users.noreply.github.com
Date: 2022-05-13 14:54:26
LastEditors: seltsam020 73098253+seltsam020@users.noreply.github.com
LastEditTime: 2022-05-13 15:11:30
FilePath: \neu_deeplearning_coursedesign\exp1\divide.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import random
trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = './data/train_location'
txtsavepath = './data/label'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('data/ImageSet/trainval.txt', 'w')
ftest = open('data/ImageSet/test.txt', 'w')
ftrain = open('data/ImageSet/train.txt', 'w')
fval = open('data/ImageSet/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
