from config import pandas as pd
from config import numpy as np

def amplitudes_initial_guess(data, *peaks):
    """
    This function is used to get the absorption values at the peaks associated
    with each structure. It locates the closest value to the wanted peak value,
    and returns the absorption value of that wavenumber
    """
    amplitudes_guess = []
    for peak in peaks:
        idx = abs(data['wavenumber'] - peak).idxmin()
        guess = data['absorption'][idx]
        amplitudes_guess.append(guess)
    return amplitudes_guess

def build_initial_guess(peaks, amplitudes_values):
    """
    A function made to construct the initial guess for the fitting,
    so that the user won't have to input themselves
    """
    initial_width = 25 # This will be constant
    initial_guess = []
    for (amp, peak) in zip(amplitudes_values, peaks):
        initial_guess.append(amp)
        initial_guess.append(peak)
        initial_guess.append(initial_width)
    return initial_guess
