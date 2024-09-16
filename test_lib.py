import pandas as pd
import pytest
import os

@pytest.fixture(scope="module")
def load_data():
    """ Load the dataset once and use it across multiple tests """
    df = pd.read_csv('cereal.csv')
    return df

@pytest.fixture(scope="session")
def histogram_path():
    """ Define the path for the histogram file once and use across tests """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'calories_histogram.png')

def test_load_dataset(load_data):
    """ Test if the dataset loads correctly and is not empty """
    assert not load_data.empty, "Dataset is empty"

def test_summary_statistics(load_data):
    """ Test for correct calculation of summary statistics """
    summary_stats = load_data.describe()
    assert 'calories' in summary_stats.columns, "'calories' column missing in summary stats"
    assert summary_stats['calories']['mean'] > 0, "Calories mean should be greater than 0"
    assert summary_stats['protein']['mean'] > 0, "Protein mean should be greater than 0"  # Example additional check

def test_histogram_creation(histogram_path):
    """ Test if the histogram image file is created """
    assert os.path.exists(histogram_path), "Histogram image not created at: " + histogram_path

def test_cleanup(histogram_path):
    """ Test to remove generated files if needed (optional) """
    if os.path.exists(histogram_path):
        os.remove(histogram_path)
    assert not os.path.exists(histogram_path), "Failed to clean up histogram image file"
