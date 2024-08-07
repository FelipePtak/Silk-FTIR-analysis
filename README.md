# Silk-FTIR-analysis
Analysis of the secondary structure in reconstituted silk fibroin (RSF) by deconvolution of the Amide I region.

The deconvolution is made with a 7 peaks gaussian function.
The peaks and analysis are described in Reference 1.

# Peaks

| Wavenumber (1/cm) | Assignment      |
| :-----------------:|:--------------:|
| 1609 | Intermolecular B-Sheet       |
| 1621 | Intermolecular B-Sheet       |
| 1631 | Intermolecular B-Sheet       |
| 1650 | A-Helix/Random Coil          |
| 1673 | B-Turn                       |
| 1695 | Antiparallel Amyloid B-Sheet |
| 1703 | Antiparallel Amyloid B-Sheet |


# The program

The protocol is simple. As this is an ongoing project, so far I'm only doing it for RSF films.
The spectra of the films can be done directly from the measurement, while for the RSF solution one needs to subtract the vapors and the solvent spectra.

The steps are:

1. Load FTIR specturm file
2. Separate the Amide I band into a different file. We can try the following ranges:
    1. 1580-1725 1/cm
    2. 1600-1700 1/cm (actual Amide I band)
3. Use Savitsky-Golay filter to smooth the data
    1. Window length: 50
    2. Polynomial order: 2
4. Subtract a baseline. We can try the following methods:
    1. Built-in function from peakutils library -> peakutils.baseline(data, polynomial order) [2];   
    2. Using a Bezier function (See Anastasia-Ragulskaya code on GitHub) [3]
    3. Get anchor points from the second derivative of the spectrum
5. Fit the data to a Gaussian function:
    1. Peaks to be used on the "Amide I Vibrational band assignment.txt" file
        1. The peaks are also used as free parameters for optimization, respecting the range of \pm 2 1/cm stated in Reference 1.
    2. An alternative is to fit the data with a Voigt function (on development...). [4]
6. Calculate the area of each peak to discriminate between the types of secondary structure present in the sample.

# References
1. D. Eliaz. et al., "Micro and nano-scale compartments guide the structural transition of silk protein monomers into silk fibers". Nature Communications 13, 7856 (2022)
doi: https://doi.org/10.1038/s41467-022-35505-w
2. https://peakutils.readthedocs.io/en/latest/
3. https://github.com/anastasia-ragulskaya/FTIR_code
4. A. Sadata and I. J. Joye, "Peak Fitting Applied to Fourier Transform Infrared and Raman Spectroscopic Analysis of Proteins". Appl. Sci. 10(7), 5918 (2020) doi: https://doi.org/10.3390/app10175918
