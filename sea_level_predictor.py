import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    future_years = range(1880, 2051)
    line = slope * future_years + intercept
    ax.plot(future_years, line, color='red', linestyle='--', label='Line of best fit (1880-2050)')
    

    # Create second line of best fit
    df1 = df.loc[df['Year'] >= 2000]
    slope1, intercept1, _, _, _ = linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    year_00 = range(2000, 2051)
    line1 = slope1 * year_00 + intercept1
    ax.plot(year_00, line1, color='green', linestyle='--', label='Line of best fit (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title("Rise in Sea Level")
    ax.legend()
    ax.grid(True)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_"level_plot.png')
    return plt.gca()