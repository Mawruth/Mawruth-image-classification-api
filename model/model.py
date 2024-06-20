from PIL import Image, ImageOps
import numpy as np
from initializers import model,class_names,data

def imagePreprocessing(image:Image) -> Image:
    image = image.convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    return image

def classifyImage(image:Image) -> str:
    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]

    return class_name[2:].strip()
