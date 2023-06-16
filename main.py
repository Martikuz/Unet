# UNET Code based on youtube tutorial by Augmented Startups
# https://www.youtube.com/watch?v=n4_ZuntLGjg
# called on 16.06.2023

import os
import numpy as np
import cv2 as cv
from glob import glob
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPool2D, Conv2DTranspose, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, CSVLogger

# test if opencv works
#print( cv.__version__ )

# SEEDING
os.environ["PYTHONHASHSEED"] = str(42)
np.random.seed(42)
tf.random.set_seed(42)

#HYPERPARAMETERS
batch_size = 8
lr = 1e-4 ## 0.0001
epochs = 100
height = 768
width = 512

# PATH
dataset_path = os.path.join("dataset", "non-aug")

files_dir = os.path.join("files", "non-aug")
model_file = os.path.join(files_dir, "unet-non-aug.h5")
log_file = os.path.join(files_dir, "log-non-aug.csv")

# CREATING FOLDER
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

create_dir(files_dir)

# BUILDING UNET

# Conv Block
def conv_block(inputs, num_filters):
    x = Conv2D(num_filters, 3, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Conv2D(num_filters, 3, padding="same")(x)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    return x

# Encoder Block
def encoder_block(inputs, num_filters):
    x = conv_block(inputs, num_filters)
    p = MaxPool2D((2,2))(x)

    return x, p

# Decoder Block
def decoder_block(inputs, skip, num_filters):
    x = Conv2DTranspose(num_filters, (2,2), strides=2, padding="same")(inputs)
    x = Concatenate()([x, skip])
    x = conv_block(x, num_filters)

    return x

# UNET
def build_unet(input_shape):
    inputs = Input(input_shape)

    """ Encoder """
    s1, p1 = encoder_block(inputs, 64)
    s2, p2 = encoder_block(p1, 128)
    s3, p3 = encoder_block(p2, 256)
    s4, p4 = encoder_block(p3, 512)

    """ Bridge """
    b1 = conv_block(p4, 1024)

    """ Decoder """
    d1 = decoder_block(b1, s4, 512)
    d2 = decoder_block(d1, s3, 256)
    d3 = decoder_block(d2, s2, 128)
    d4 = decoder_block(d3, s1, 64)

    outputs = Conv2D(1, 1, padding="same", activation="sigmoid")(d4)

    model = Model(inputs, outputs, name="UNET")

    return model

# DATASET PIPELINE
# minute 09:20
# Line 10 might be not complete
