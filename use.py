import tensorflow as tf
from tf_crnn.loader import PredictionModel
from scipy.misc import imread

model_dir = '/output/export/1530744466/'
image = imread('/Users/maxwellstone/Downloads/IMG_6577 2.JPG', mode='L')[: ,:, None]

with tf.Session() as sess:
    model = PredictionModel(model_dir)
    predictions = model.predict(image)
    transcription = predictions['words']
    score = predictions['score']
    print(transcription,score)