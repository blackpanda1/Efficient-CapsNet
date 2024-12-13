# -*- coding: utf-8 -*-
"""기계학습특론_프로젝트_efficient_capsnet_train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sCvnJLGir9Y3JhUsnwg0oI9yCq1sSADg
"""

!git clone https://github.com/EscVM/Efficient-CapsNet.git

# Commented out IPython magic to ensure Python compatibility.
# 현재 작업 디렉토리 확인
!ls

# 클론한 레포지토리로 이동
# %cd Efficient-CapsNet

# 레포지토리 내 파일 및 폴더 확인
!ls

import sys
sys.path.append('/content/Efficient-CapsNet')  # 경로를 Python 경로에 추가

!pip install -r requirements.txt

# TensorFlow와 Addons 호환성을 맞추기 위해 버전 조정
!pip install tensorflow==2.12.0 tensorflow-addons==0.20.0

# 런타임 재시작
import os
os.kill(os.getpid(), 9)

# 런타임 재시작 후 코드 실행
import tensorflow as tf
from utils import Dataset, plotImages, plotWrongImages, plotHistory
from models import EfficientCapsNet

import tensorflow as tf
print("사용 가능한 GPU:", tf.config.list_physical_devices('GPU'))

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

# some parameters
model_name = 'MNIST'

dataset = Dataset(model_name, config_path='config.json')

n_images = 20 # number of images to be plotted
plotImages(dataset.X_test[:n_images,...,0], dataset.y_test[:n_images], n_images, dataset.class_names)

model_train = EfficientCapsNet(model_name, mode='train', verbose=True)

dataset_train, dataset_val = dataset.get_tf_data()

history = model_train.train(dataset, initial_epoch=0)