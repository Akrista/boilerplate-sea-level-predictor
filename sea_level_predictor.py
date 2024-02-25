import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = range(1880, 2051)
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1')
    # Create second line of best fit
    slope_2000 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']).slope
    intercept_2000 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']).intercept
    x_pred_2000 = range(2000, 2051)
    y_pred_2000 = slope_2000 * x_pred_2000 + intercept_2000
    plt.plot(x_pred_2000, y_pred_2000, 'g', label='Best Fit Line 2') 

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
