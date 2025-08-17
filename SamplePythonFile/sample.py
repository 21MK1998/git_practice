import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os
import sys
import math

# abcdefg

def function2():
    """
    This is a sample function that does nothing.
    It is here to demonstrate the structure of a Python file.
    """
    pass

# Sample Python code for data analysis
# abcdefg

def sample:_function():
    # This is a sample function
    print("This is a sample function.")
    return "Sample output"

# Example usage
def analyze_data(data):
    """
    Analyzes the given data and returns some statistics.

    Parameters:
    data (pd.DataFrame): The data to analyze.

    Returns:
    dict: A dictionary containing mean and standard deviation of the data.
    """
    mean = data.mean()
    std_dev = data.std()
    return {'mean': mean, 'std_dev': std_dev}
