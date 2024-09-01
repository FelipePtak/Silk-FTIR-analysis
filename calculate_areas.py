import numpy as np

def gaussian_area(amp, wid):
    """
    A simple calculation of the area of a gaussian function
    """
    cst = 1 / np.sqrt(2*np.pi)
    area = amp * wid / cst
    return area

def areas_list(params):
    """
    Creates a list with the area of each individual gaussian composing the spectrum
    """
    areas = []
    for i in range(0, len(params), 3):
        amp = params[i]
        wid = params[i+2]
        area = gaussian_area(amp, wid)
        areas.append(area)
    total_area = sum(areas)
    return areas, total_area

def struc_areas(areas):
    """
    Assuming a 7-peak gaussian, this calculates the areas of each secondary structure
    1. alpha-helix
    2. beta-Sheet
    3. beta-turns
    Check 'Amide I Vibrational band assignments.txt' file for reference
    """
    helix_area = areas[3]
    sheet_area = areas[0] + areas[1] + areas[2] + areas[5] + areas[6]
    turn_area = areas[4]
    return helix_area, sheet_area, turn_area

def area_percentage(struc_area, total_area):
    percent = (struc_area / total_area) * 100
    return percent

def percentage_print(total_area, *structures_areas):
    percentages = {}
    struc_names = ['alpha-helix', 'beta-sheet', 'beta-turn']
    for (name, area) in zip(struc_names, structures_areas):
        percentages[name] = area_percentage(area, total_area)
    for (struc, val) in percentages.items():
        print(f'{struc} area: {val:.2f}%')
    return percentages
