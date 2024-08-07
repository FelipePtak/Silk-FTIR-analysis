import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

"""Straightforward functions to select a file
and make it to a DataFrame."""


def selectFile():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title='Select data files',\
    file_types = (("csv files"), ("*.csv", "*.CSV"), ("All files", "*.*")))
    return file_paths

def loadData(file_path):
    data = pd.read_csv(file_path, names=['wavenumber', 'absorption'])
    return data
