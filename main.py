import os
import numpy as np
import matplotlib.pyplot as plt
from config import *
from load_data import *
from plots import *
from normalize_data import *
from amide import *
from smooth import *
from baseline_subtraction import *
from Fitting_functions import *
from scipy.optimize import curve_fit
from first_guess import *
from bounds_constructor import *
from calculate_areas import *
from save_parameters import *

plt.style.use('seaborn-v0_8')

def main():
    # Loading files
    file_path = selectMultipleFiles()
    print(f"Selected files: {file_path}")
    print("\n\n")
    files_list = list(file_path)
    for file in files_list:
        fullspectrum = loadData(file)
        print("Full spectrum data: \n", fullspectrum.head())

        normalized_data = normalize_data(fullspectrum)
        plot_fulldata(normalized_data.wavenumber, normalized_data.normalized)

        amide_data = amide_band_data(normalized_data)
        print("Amide I data: \n", amide_data.head())
        plot_amide(amide_data.wavenumber, amide_data.normalized)

        smoothed_data = smoothFilter(amide_data)
        plot_filter(amide_data, smoothed_data)

        amide_baseline_sub = baselineSubtract(amide_data)
        corrected_data = baselineSubtract(smoothed_data)
        plot_filter(amide_baseline_sub, corrected_data)

        peaks = [1609, 1621, 1631, 1650, 1673, 1695, 1703]
        assignments = [r'Intermolecular B-Sheet', r'Intermolecular B-Sheet', \
        r'Intermolecular B-Sheet', r'A-Helix/Random Coils', 'B-Truns', \
        r'Antiparallel amyloid B-Sheet', r'Antiparallel amyloid B-Sheet']

        print("These are the peaks we want to fit:\n")
        print(f'{'Peak (1/cm)' : ^10} | {'Assignment': ^10}\n')
        for (peak, struc) in zip(peaks, assignments):
            print(f"{peak : >5} | {struc: ^10}\n")

        print("Calculating initial guess for data fit...\n")
        initial_amplitudes = amplitudes_initial_guess(corrected_data, *peaks)
        initial_guess = build_initial_guess(peaks, initial_amplitudes)
        init_guess_file = 'initial_guess.txt'
        print('Initial guess parameters:\n')
        for i in range(len(peaks)):
            print(f'Amp{i+1}: {initial_guess[3*i]}')
            print(f'Peak{i+1}: {initial_guess[3*i+1]}')
            print(f'Width{i+1}: {initial_guess[3*i+2]}')

        lower_bounds = build_lower_bounds(peaks)
        upper_bounds = build_upper_bounds(peaks)

        bounds = (lower_bounds, upper_bounds)

        print("\nCalculating fit...")
        popt, pcov = curve_fit(wrap_function,\
        corrected_data.wavenumber, corrected_data.normalized,\
        p0=initial_guess, bounds=bounds)

        print(f"Fitted parameters: \n")
        for i in range(len(peaks)):
            print(f'Amplitude{i+1}: {popt[3*i] : ^10}')
            print(f'Peak{i+1}: {popt[3*i + 1] : ^10}')
            print(f'Width{i+1}: {popt[3*i + 2] : ^10}\n')

        xfit = np.arange(amide_initial_band, amide_final_band, 0.1)
        yfit, separate_peaks = seven_gaussian(xfit, *popt)
        xdata = corrected_data.wavenumber
        ydata = corrected_data.normalized
        plt.plot(xdata, ydata, 'ko', label='Data')
        plt.plot(xfit, yfit, 'r-', label='Fit')
        plt.title('Amide I region', **titleFonts)
        plt.xlabel('Wavenumber (1/cm)', **axisFonts)
        plt.ylabel('Absorption (a.u.)', **titleFonts)
        plt.xlim(amide_limits)
        plt.legend()
        plt.show()

        plt.plot(xdata, ydata, 'ko', label='Data')
        plt.plot(xfit, yfit, 'r-', label='Fit')

        for idx, peak in enumerate(separate_peaks):
            plt.plot(xfit, peak, color=peak_colors[idx], label=peak_labels[idx])
            plt.fill_between(xfit, peak.min(), peak, color=peak_colors[idx], alpha=0.5)

        plt.title('Amide I region', **titleFonts)
        plt.xlabel('Wavenumber (1/cm)', **axisFonts)
        plt.ylabel('Absorption (a.u.)', **titleFonts)
        plt.xlim(amide_limits)
        plt.legend()
        plt.show()

        # Calculating areas

        areas, total_area = areas_list(popt)
        helix_area, sheet_area, turn_area = struc_areas(areas)
        struc_list = [helix_area, sheet_area, turn_area]
        percentages = percentage_print(total_area, *struc_list)

        # Saving parameters into a file

        filename = os.path.basename(file)
        filename = filename.lower()
        filename = filename.removesuffix('.csv')
        full_path = os.path.dirname(file)

        parameters_output = filename + '_fitted_parameters.txt'
        parameters_file = os.path.join(full_path, parameters_output)

        percentages_output = filename + '_structures_formation.txt'
        percentages_file = os.path.join(full_path, percentages_output)

        amps, cens, wids = params_list(*popt)
        save_fitted_parameters(parameters_file, peaks, amps, cens, wids)
        save_percentage(percentages_file, percentages)




if __name__ == "__main__":
    main()
