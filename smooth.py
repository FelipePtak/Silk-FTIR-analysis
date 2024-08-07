from scipy import signal

"""
This function takes in the amide data
and smooths it with the Savitzky-Golay filter
Initial parameters:
window length: 50
polynomial order: 2
"""

def smoothFilter(data):
    smoothed_absorption = signal.savgol_filter(data['absorption'],\
    window_length = 50, polyorder=2)
    smoothed_data = pd.DataFrame()
    smoothed_data['wavenumber'] = data.wavenumber
    smoothed_data['absorption'] = smoothed_absorption

    return smoothed_data
