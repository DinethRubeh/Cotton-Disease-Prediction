import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Saved model path
model_path ='models/model_vgg19.h5'

# Load trained model
model = load_model(model_path)


def predict(image_path):

    # prediction classes
    pred_classes = {
        0:'diseased cotton leaf',
        1:'diseased cotton plant',
        2:'fresh cotton leaf',
        3:'fresh cotton plant'
        }

    # load image and resize to original trained model image size
    loaded_img = image.load_img(image_path, target_size=(224,224))

    ## image preprocessing

    # convert to array format
    img = image.img_to_array(loaded_img)
    # rescale
    img = img/255 
    # batch of 1 (conv2d require input in [batch, height, width, channels])
    img = np.expand_dims(img, axis=0)

    # model prediction
    pred = model.predict(img)
    pred = pred.argmax(axis=1)[0]

    return "This is a {}".format(pred_classes[pred])