#!/user/bin/env python3
# -*- coding: utf-8 -*-
import os
import gzip
import pickle
try:
    import urllib.request
except ImportError:
    raise ImportError("You should use Python 3.X")
import numpy as np

# MNIST 数据在 OSSCI S3 上的镜像
url_base = 'https://ossci-datasets.s3.amazonaws.com/mnist/'

#文件名字典
key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}

#脚本目录的绝对路径
dataset_dir = os.path.dirname(os.path.abspath(__file__))
#最终保存pickle的路径
save_file = os.path.join(dataset_dir, 'mnist.pkl')

#图像数量和尺寸
train_num = 60000
test_num = 10000
img_dim = (1,28,28)
img_size = 784

def _download(file_name):
    """下载单个文件"""
    file_path = os.path.join(dataset_dir, file_name)
    #如果文件已存在跳过
    if os.path.exists(file_path):
        return
    print(f"Downloading {file_name}...")
    # 模拟浏览器的 User-Agent
    headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
    request = urllib.request.Request(url_base+file_name,headers=headers)
    response = urllib.request.urlopen(request).read()
    with open(file_path, 'wb') as f:
        f.write(response)
    print("Download complete.")

def download_mnist():
    """批量下载文件"""
    for v in key_file.values():
        _download(v)

def _load_label(file_name):
    """读取下载好的标签"""
    file_path = os.path.join(dataset_dir,file_name)
    print(f"convert {file_name} to Numpy array... ")
    with gzip.open(file_path,'rb') as f:
        # 跳过前8字节，剩下的每个字节就是一个标签（0-9）
        labels = np.frombuffer(f.read(),dtype=np.uint8,offset=8 )
    print("convert complete.")
    return labels

def _load_img(file_name):
    """读取下载好的图像"""
    file_path = os.path.join(dataset_dir,file_name)
    print(f"convert {file_name} to Numpy array... ")
    with gzip.open(file_path,'rb') as f:
        # 跳过前16字节，剩下的就是所有像素值
        img = np.frombuffer(f.read(),dtype=np.uint8,offset=16)
    img = img.reshape(-1,img_size)
    print("convert complete.")
    return img

def _convert_numpy():
    """批量读取标签和图像"""
    dataset = {}
    dataset['train_img'] = _load_img(key_file['train_img'])
    dataset['test_img'] = _load_img(key_file['test_img'])
    dataset['train_label'] = _load_label(key_file['train_label'])
    dataset['test_label'] = _load_label(key_file['test_label'])
    return dataset

def init_mnist():
    """下载读取图像和标签并且保存为pickle"""
    download_mnist()
    dataset = _convert_numpy()
    print("Create pickle file...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset,f,protocol=-1)
    print("MNIST initialization complete.")

def _change_one_hot_label(X):
    """One-hot 转换"""
    T = np.zeros((X.size,10),dtype=np.uint8)
    for idx,label in enumerate(X):
        T[idx,label] = 1
    return T

def load_mnist(normalize=True,flatten=True,one_hot_label=False):
    # 如果没有 pickle 文件，先初始化
    if not os.path.exists(save_file):
        init_mnist()

    #读取pickle
    with open(save_file,'rb') as f:
        dataset = pickle.load(f)

    #归一化到0-1
    if normalize:
        for key in ('train_img','test_img'):
            dataset[key] = dataset[key].astype('float32')/255.0

    # one-hot
    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])

    # 恢复成 N×1×28×28 形状
    if not flatten:
        # *img_dim 会把 (1,28,28) 拆成三个独立的参数 1,28, 28
        for key in ('train_img','test_img'):
            dataset[key] = dataset[key].reshape(-1,*img_dim)

    return (dataset['train_img'],dataset['train_label']),(dataset['test_img'],dataset['test_label'])

if __name__ == '__main__':
    init_mnist()
