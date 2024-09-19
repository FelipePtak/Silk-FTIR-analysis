from module_imports import pd
from config import amide_initial_band, amide_final_band

"""This function simply takes the full spectrum data
and assign the amide band (at principle 1580-1725 1/cm)
to a separate variable"""

def amide_band_data(data):
    amide_data = pd.DataFrame()
    amide_data = data[(data['wavenumber'] >= amide_initial_band) \
        & (data['wavenumber'] <= amide_final_band)]
    amide_data.reset_index(drop=True, inplace=True)
    return amide_data
