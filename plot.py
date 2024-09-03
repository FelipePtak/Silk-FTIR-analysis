from config import amide_initial_band, amide_final_band, axisFonts, titleFonts, peak_colors,\
ycolors, peak_labels, amide_limits, full_data_limits
from module_imports import plt

plt.style.use('seaborn-v0_8')

def plot_fulldata(xdata, ydata):
    fig = plt.figure()
    plt.plot(xdata, ydata, 'ko', label='Data')
    plt.title('Full spectrum', **titleFonts)
    plt.xlabel('Wavenumber (1/cm)', **axisFonts)
    plt.ylabel('Normalized absorption (a.u.)', **titleFonts)
    plt.xlim(full_data_limits)
    plt.legend()
    plt.show()
    return fig

def plot_amide(xdata, ydata):
    fig = plt.figure()
    plt.plot(xdata, ydata, 'ko', label='Data')
    plt.title('Amide I region', **titleFonts)
    plt.xlabel('Wavenumber (1/cm)', **axisFonts)
    plt.ylabel('Normalized absorption (a.u.)', **titleFonts)
    plt.xlim(amide_limits)
    plt.legend()
    plt.show()
    return fig

def plot_filter(original_data, filtered_data):
    xdata = original_data.wavenumber
    ydata = original_data.normalized
    y_savgol = filtered_data.normalized
    fig = plt.figure()
    plt.plot(xdata, ydata, 'r-', linewidth=2, label='Data')
    plt.plot(xdata, y_savgol, 'g-', linewidth=2, label='Filtered data')
    plt.xlabel('Wavenumber (1/cm)', **axisFonts)
    plt.ylabel('Normalized absorption (a.u.)', **titleFonts)
    plt.title('Amide I region', **titleFonts)
    plt.xlim(amide_limits)
    plt.legend()
    plt.show()
    return fig

def plot_fit(xdata, ydata, xfit, yfit):
    fig = plt.figure()
    plt.plot(xdata, ydata, 'ko', label='Data')
    plt.plot(xfit, yfit, 'r-', label='Fit')
    plt.title('Amide I region', **titleFonts)
    plt.xlabel('Wavenumber (1/cm)', **axisFonts)
    plt.ylabel('Absorption (a.u.)', **titleFonts)
    plt.xlim(amide_limits)
    plt.legend()
    plt.show()
    return fig

def plot_separate_peaks(xfit, *peaks):
    fig = plt.figure()
    for idx, peak in enumerate(peaks):
        plt.plot(xfit, peak, color=peak_colors[idx], label=peak_labels[idx])
        plt.fill_between(xfit, peak.min(), peak, color=peak_colors[idx], alpha=0.5)
    plt.show()
    return fig
