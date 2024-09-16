import pandas as pd
import os
import matplotlib.pyplot as plt
from main import df, summary_stats, histogram_path

def test_load_dataset():
    """ Test if the dataset is loaded correctly """
    assert not df.empty, "Dataframe is empty after loading the dataset."

def test_summary_statistics():
    """ Test if summary statistics are generated correctly """
    required_columns = ['calories', 'protein', 'fat', 'sodium']  # example columns
    for col in required_columns:
        assert col in summary_stats.columns, f"Expected column {col} in summary statistics."

def test_histogram_file_creation():
    """ Test if the histogram file is created at the correct path """
    assert os.path.exists(histogram_path), "Histogram image file was not created."

def test_file_creation():
    """ Test if summary statistics CSV file is created """
    summary_csv_path = 'summary_statistics.csv'
    assert os.path.exists(summary_csv_path), "Summary statistics CSV file was not created."

# Additional test to check the correctness of the histogram (Optional)
def test_histogram_content():
    """ Ensure histogram displays the correct data """
    fig, ax = plt.subplots()
    df['calories'].hist(bins=10, ax=ax)
    ax.set_title('Distribution of Calories')
    ax.set_xlabel('Calories')
    ax.set_ylabel('Frequency')
    # Assuming we can compare the visible output in some way, or check internal state of `ax`
    # This part is tricky without a graphical check but you can test properties like labels, titles, etc.

# Ensure cleanup if needed
def test_cleanup():
    """ Remove test output files if needed """
    os.remove('summary_statistics.csv')
    os.remove(histogram_path)
