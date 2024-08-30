"""
This is for all the imports that will be necessary,
as well as some useful variables and kwargs
"""

peaks = [1609, 1621, 1631, 1650, 1673, 1695, 1703]

amide_initial_band = 1580 # 1/cm
amide_final_band = 1725 # 1/cm

titleFonts = {'fontname' : 'Arial', 'fontsize' : 16}
axisFonts = {'fontname' : 'Arial', 'fontsize' : 14}

amide_limits = [amide_initial_band, amide_final_band]
full_data_limits = [4000, 500]

peak_colors = ['c', 'c', 'c', 'm', 'y', 'c', 'c']
peak_labels = [r'$\beta$-Sheet', '_no_', '_no_',r'$\alpha$-Helix/Random Coil', r'$\beta$-Turn', '_no_', '_no_']
ycolors=['r', 'g', 'b', 'm', 'c', 'y', 'k']
