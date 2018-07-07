import data_handler as dh

fn = dh.preprocess_image_for_prediction.serving_input_fn()
print(fn)
