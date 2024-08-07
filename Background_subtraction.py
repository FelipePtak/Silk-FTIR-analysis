from peakutils import baseline

"""This function subtracts a baseline
based on the peakutils function"""

def baselineSubtract(data):
    bl = baseline (data.absorption, deg=1)
    corrected_data = pd.DataFrame()
    corrected_data['wavenumber'] = data.wavenumber
    corrected_data['absorption'] = data.absorption - bl

    return corrected_data
