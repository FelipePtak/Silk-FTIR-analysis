from module_imports import os, plt

def save_fullspectrum_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_full_spectrum_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')

def save_amide_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_amide_band_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')

def save_savgol_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_savgol_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')

def save_baseline_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_baseline_correction_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')

def save_data_fit_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_data_fit_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')

def save_assignments_plot(figure, file):
    filename = filename.lower()
    filename = filename.removesuffix('.csv')
    full_path = os.path.dirname(filename)
    suffix = '_structures_plot.png'
    output_name = filename + suffix
    full_file_name = os.path.join(full_path, output_name)
    figure.savefig(full_file_name, dpi=300, bbox_inches='tight')
