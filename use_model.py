import tensorflow as tf
import pandas as pd
import numpy as np

model = tf.keras.models.load_model('./models/settings')

CLASS_NAMES = {'Junior Network Administrator',
               'Junior Programmer', 'Junior Web Programmer'}

sample = {
    "iq": 139,
    "interest_outside_school": "Art",
    "interest_outside_school2": "Economics",
    "interest_outside_school3": "Sport",
    "interest_outside_school4": "",
    "favorite_subjects_it": "Desain web",
    "favorite_subjects_it2": "Pemrograman Web",
    "favorite_subjects_it3": "Komputer Animasi",
    "favorite_subjects_it4": "",
    "name": "Dina Berliana Br Sitohang",
    "hobbies": "Sport",
    "hobbies2": "Read books",
    "hobbies3": "Movies",
    "hobbies4": "Social Media",
    "hobbies5": "''",
    "hobbies6": "''",
    "hobbies7": "''",
    "hobbies8": "''",
    "hobbies9": "''",
    "junior_network_administrator": 82.8,
    "junior_web_programmer": 76.42,
    "junior_programmer": 80.7,
}

input_dict = {name: tf.convert_to_tensor(
    [value]) for name, value in sample.items()}
predictions = np.argmax(model.predict(input_dict))
predictions = pd.DataFrame(CLASS_NAMES)[0][predictions]
