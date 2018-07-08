import tensorflow as tf 
import numpy
import PIL
from tf_crnn.loader import PredictionModel
from tf_crnn.data_handler import serving_single_input

sess = tf.Session()
data = serving_single_input("0/img0.png")
print(data)
image_content = "0/img0.png"
image = tf.rgb2gray(
    tf.image.is_jpeg(image_content),
    lambda: tf.image.decode_jpeg(image_content, channels=1, name='image_decoding_op',
                                    try_recover_truncated=True),
    lambda: tf.image.decode_png(image_content, channels=1, name='image_decoding_op'))

# Data augmentation

predictImage = PredictionModel("/output/export/1530744466/", sess)
predictImage.predict(image)
