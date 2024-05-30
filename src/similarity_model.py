import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from src.feature_extractor import extract_features


def create_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(model, features1, features2):
    X = np.concatenate([features1, features2])
    y = np.concatenate([np.ones(len(features1)), np.zeros(len(features2))])
    model.fit(X, y, epochs=10, batch_size=8)

def compare_features(model, elements1, elements2):
    features1 = extract_features(elements1)
    features2 = extract_features(elements2)

    encoded_features1 = model.predict(features1)
    encoded_features2 = model.predict(features2)
    similarities = cosine_similarity(encoded_features1, encoded_features2)

    similarity_info = []
    for i, element1 in enumerate(elements1):
        for j, element2 in enumerate(elements2):
            similarity_info.append({
                'element1': element1['name'],
                'element2': element2['name'],
                'similarity': similarities[i][j]
            })

    # Calculate overall similarity percentage
    avg_similarity = np.mean([info['similarity'] for info in similarity_info]) * 100

    return similarity_info, avg_similarity