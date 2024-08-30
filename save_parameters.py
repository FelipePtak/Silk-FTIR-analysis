"""
A function to save the fitted parameters and areas
"""

def params_list(*params):
    amps = []
    cens = []
    wids = []
    for i in range(0, len(params) , 3):
        amps.append(params[i])
        cens.append(params[i+1])
        wids.append(params[i+2])
    return amps, cens, wids

def save_fitted_parameters(filepath, peaks, amps, cens, wids):
    with open(filepath, 'w') as f:
        f.write("Original peak (1/cm)\tAmplitude (a.u.)\tFitted peak (1/cm)\tWidth (1/cm)\n")
        for (peak, amp, cen, wid) in zip(peaks, amps, cens, wids):
            f.write(f"{peak : ^10}\t{amp : ^10}\t{cen : ^10}\t{wid : ^10}\n")
        f.close()

def save_percentage(filepath, percent_dict: dict):
    with open(filepath, 'w') as f:
        f.write('Structure\tPercentage\n')
        for (struc, val) in percent_dict.items():
            f.write(f"{struc : ^10}\t{val:.2f}\n")
        f.close()
