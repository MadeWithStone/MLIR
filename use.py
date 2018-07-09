import tensorflow as tf
from tf_crnn.loader import PredictionModel
from scipy.misc import imread

model_dir = 'model'
image = imread('img.png', mode='L')[: ,:, None]

with tf.Session() as sess:
    model = PredictionModel(model_dir)
    predictions = model.predict(image)
    transcription = predictions['words']
    score = predictions['score']
    print(transcription,score)