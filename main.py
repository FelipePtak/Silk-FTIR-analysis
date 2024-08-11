"""
Main function. Will run everything.
Still under development...
"""

from config import *
from load_data import *
from plots import *

def main():
    file_path = selectFile()
    fullspectrum = loadData(file_path)

    normalized_data = normalize_data(fullspectrum)
    plot_fulldata(normalized_data.wavenumber, normalized_data.normalized)

    amide_data = amide(fullspectrum)
    plot_amide(amide_data.wavenumber, amide_data.normalized)

    smoothed_data = smooth(amide_data)
    plot_filter(amide_data, smoothed_data)

    amide_baseline_sub = baselineSubtract(amide_data)
    corrected_data = baselineSubtract(smoothed_data)
    plot_filter(amide_baseline_sub, corrected_data)



if __name__ == "__main__":
    main()
