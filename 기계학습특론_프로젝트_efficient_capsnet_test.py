# -*- coding: utf-8 -*-
"""기계학습특론_프로젝트_efficient_capsnet_test.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qeYrWIp_X9jG2xXE_9OOxPzLC1bqvXiF

# Efficient-CapsNet Model Test

In this notebook we provide a simple interface to test the different trained Efficient-CapsNet models on the three datasets:

- MNIST (MNIST)
- smallNORB (SMALLNORB)
- Multi-MNIST (MULTIMNIST)

**NB**: remember to modify the "config.json" file with the appropriate parameters.
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

# Commented out IPython magic to ensure Python compatibility.
# %load_ext autoreload
# %autoreload 2

# 런타임 재시작 후 코드 실행
import tensorflow as tf
from utils import Dataset, plotImages, plotWrongImages
from models import EfficientCapsNet

# test는 데이터양이 적어서 gpu를 사용하지 않아도 됨
# gpus = tf.config.experimental.list_physical_devices('GPU')
# tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
# tf.config.experimental.set_memory_growth(gpus[0], True)

import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')

# Check if any GPUs are detected
if gpus:
    # Set the first GPU as visible and enable memory growth
    tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
    tf.config.experimental.set_memory_growth(gpus[0], True)
    print("GPU is available and configured.")
else:
    print("No GPU detected. Using CPU instead.")

# some parameters
model_name = 'MNIST'
custom_path = None # if you've trained a new model, insert here the full graph weights path

"""# 1.0 Import the Dataset"""

dataset = Dataset(model_name, config_path='config.json')

"""## 1.1 Visualize imported dataset"""

n_images = 20 # number of images to be plotted
plotImages(dataset.X_test[:n_images,...,0], dataset.y_test[:n_images], n_images, dataset.class_names)

"""# 2.0 Load the Model"""

model_test = EfficientCapsNet(model_name, mode='test', verbose=True, custom_path=custom_path)

model_test.load_graph_weights() # load graph weights (bin folder)

"""# 3.0 Test the Model"""

model_test.evaluate(dataset.X_test, dataset.y_test) # if "smallnorb" use X_test_patch

"""## 3.1 Plot misclassified images"""

#not working with MultiMNIST
y_pred = model_test.predict(dataset.X_test)[0] # if "smallnorb" use X_test_patch

n_images = 20
plotWrongImages(dataset.X_test, dataset.y_test, y_pred, # if "smallnorb" use X_test_patch
                n_images, dataset.class_names)