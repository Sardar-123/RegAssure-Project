import numpy as np


def extract_features(elements):
    features = []

    for element in elements:
        feature_vector = np.array([
            len(element['tag']),
            len(element['attributes']),
            element['text_length']
        ])
        features.append(feature_vector)

    return np.array(features)