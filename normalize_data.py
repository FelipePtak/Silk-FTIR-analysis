import pandas as pd

def normalize_data(data):
    max_abs = data.absorption.max()
    normalized_data = pd.DataFrame(data=data)
    normalized_data['normalized'] = data.absorption / max_abs
    return normalized_data
