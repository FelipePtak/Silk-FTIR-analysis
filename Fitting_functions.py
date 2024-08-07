"""
Here we have two functions to try and fit the data.

There are two different gaussian functions, one where the peaks are fixed,
and another one where the peaks are free to be optimized.
For a reference, check the Amide I Vibrational band assignments.txt file

"""


def fixed_seven_gaussian(x, *params):
    """
    A 7 peak gaussian function
    In this function, the peaks are fixed and, Therefore
    they are no free parameters to optimize:
    """

    peaks = [1609, 1622, 1631, 1650, 1673, 1695, 1703]
    assert len(params) == 14 # Amplitude and deviation for each peak

    y = np.zeros_like(x)
    individual_peaks = []

    for i in range(len(peaks)):
        A = params[2*i + 1]
        sigma = params[2*i + 1]
        pk = peaks[i]
        single_peak = A * np.exp(-(x-pk)**2 / (2 * sigma**2))
        y += single_peak
        individual_peaks.append(single_peak)

    return y, individual_peaks

def seven_gaussian(x, *params):
    """
    A 7 peaks gaussian function in which
    the peaks are free parameters to be optimized
    """
    assert len(params) == 21

    y = np.zeros_like(x)
    individual_peaks = []

    for i in range(len(peaks)):
        amp = params[3*i]
        cen = params[3*i+1]
        wid = params[3*i+2]

        single_peak = amp * np.exp(-(x - cen)**2) / (2 * wid**2)
        y += single_peak
        individual_peaks.append(single_peak)
    return y, individual_peaks

def wrap_function(x, params*):
    """
    A function that returns only the total sum of the peaks
    """

    if len(params) == 14:
        y, _ = fixed_seven_gaussian(x, *params)

    y, _ = seven_gaussian(x, *params)
    return y
