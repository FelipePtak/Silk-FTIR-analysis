"""
A simple function to fit the data to the gaussian model
"""

from scipy.optimize import curve_fit
from Fitting_functions import *

def fit_data(func, data_x, data_y, p0, bnds):

    popt, pcov = curve_fit(func, \
        data_x, data_y, \
        p0, bnds)

    return popt, pcov

def fitted_result(popt):
    xift = np.arange(amide_initial_band, amide_final_band, 0.1)

    if len(popt) == 14:
        yfit = fixed_seven_gaussian(xfit, *popt)

    yfit = fixed_seven_gaussian(xfit, *popt)
    return yfit
