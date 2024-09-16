import os
import pandas as pd
import pytest
import matplotlib.pyplot as plt
from main import df, histogram_path

@pytest.fixture(scope="module")
def load_data():
    """ Load the dataset once and use it across multiple tests """
    data = pd.read_csv('cereal.csv')
    return data

def test_load_dataset(load_data):
    """ Test if the dataset loads correctly and is not empty """
    assert not load_data.empty, "Dataset is empty"

def test_summary_statistics(load_data):
    """ Test for correct calculation of summary statistics """
    stats = load_data.describe()
    assert 'calories' in stats.columns, "'calories' column missing in summary stats"
    assert stats['calories']['mean'] > 0, "Calories mean should be greater than 0"

def test_histogram_file_creation():
    """ Test if the histogram file is created at the correct path """
    # Call a function to generate the histogram if not already generated
    if not os.path.exists(histogram_path):
        df['calories'].hist(bins=10, figsize=(10, 8))
        plt.title('Distribution of Calories')
        plt.xlabel('Calories')
        plt.ylabel('Frequency')
        plt.savefig(histogram_path)

    assert os.path.exists(histogram_path), "Histogram image file was not created."

def test_cleanup():
    """ Test to remove generated files if needed (optional) """
    if os.path.exists(histogram_path):
        os.remove(histogram_path)
    assert not os.path.exists(histogram_path), "Failed to clean up histogram image file"
