import os
import pandas as pd


def get_structure_files(filepath):
    structure_files = []
    for file in os.listdir(filepath):
        if file.endswith('_structure_formation.txt'):
            structure_files.append(file)
    return structure_files

def structure_data(*structure_files):
    data = {}
    for file in structure_files:
        df = pd.read_csv(file, sep='\t')
        data[file] = df.set_index('Structures')['Percentages']
    return data
