import pathlib
import tensorflow as tf
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import os

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos.tar', origin=dataset_url, extract=True)
data_dir = pathlib.Path(data_dir).with_suffix('')

categories = ['roses', 'dandelion','daisy','sunflowers','tulips']

data=[]
labels=[]

for category_idx, category in enumerate(categories):
    category_path = data_dir /category
    for file in os.listdir(os.path.join(data_dir,category)):
        img_path = os.path.join(data_dir,category, file)
        img = imread(img_path)
        img = resize(img, (15,15))
        data.append(img.flatten())
        labels.append(category_idx)

data = np.asarray(data)
labels = np.asarray(labels)