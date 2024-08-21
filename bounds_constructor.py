import numpy as np

def build_lower_bounds(peaks):
    lower_bounds = []
    for peak in peaks:
        lower_bounds.append(0)
        lower_bounds.append(peak - 2)
        lower_bounds.append(0)
    return lower_bounds

def build_upper_bounds(peaks):
    upper_bounds = []
    for peak in peaks:
        upper_bounds.append(np.inf)
        upper_bounds.append(peak + 2)
        upper_bounds.append(np.inf)
    return upper_bounds
