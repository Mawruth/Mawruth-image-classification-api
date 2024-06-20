from keras.saving import load_model
import numpy as np

np.set_printoptions(suppress=True)

model = load_model("model/keras_model.h5", compile=False)

class_names = open("model/labels.txt", "r", encoding="utf-8").readlines()

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)    