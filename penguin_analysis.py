import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress

# Location of the penguin data file on the internet
PENGUINS_URL = 'https://gist.githubusercontent.com/anibali/c2abc8cab4a2f7b0a6518d11a67c693c/raw/3b1bb5264736bb762584104c9e7a828bef0f6ec8/penguins.csv'

# Download the penguin data and turn it into a Pandas DataFrame object
df = pd.read_csv(PENGUINS_URL)

# Filter data for males
male_df = df[df["sex"] == "MALE"]

# Create dataframes for each species
gentoo_df = male_df[male_df["species"] == "Gentoo"]
adelie_df = male_df[male_df["species"] == "Adelie"]
chinstrap_df = male_df[male_df["species"] == "Chinstrap"]

# Set up the plot with a professional style
plt.figure(figsize=(10, 6), facecolor='white')

# Use a beautiful color palette
colors = sns.color_palette("husl", 3)

# Scatter plots for each species with customized markers
plt.scatter(gentoo_df["bill_length_mm"], gentoo_df["body_mass_g"], color=colors[0], label="Gentoo", alpha=0.7, marker='o', s=120)
plt.scatter(adelie_df["bill_length_mm"], adelie_df["body_mass_g"], color=colors[1], label="Adelie", alpha=0.7, marker='s', s=120)
plt.scatter(chinstrap_df["bill_length_mm"], chinstrap_df["body_mass_g"], color=colors[2], label="Chinstrap", alpha=0.7, marker='^', s=120)

# Regression lines with shaded confidence intervals
for species_df, color in zip([gentoo_df, adelie_df, chinstrap_df], colors):
    sns.regplot(x=species_df["bill_length_mm"], y=species_df["body_mass_g"], scatter=False, color=color, line_kws={'linewidth': 2})
    slope, intercept, r_value, p_value, std_err = linregress(species_df["bill_length_mm"], species_df["body_mass_g"])
    x_values = np.linspace(species_df["bill_length_mm"].min(), species_df["bill_length_mm"].max(), 100)
    y_values = slope * x_values + intercept
    plt.fill_between(x_values, y_values - std_err, y_values + std_err, color=color, alpha=0.1)

# Mean markers
for species_df, color in zip([gentoo_df, adelie_df, chinstrap_df], colors):
    mean_bill_length = np.mean(species_df['bill_length_mm'])
    mean_body_mass = np.mean(species_df['body_mass_g'])
    plt.scatter(mean_bill_length, mean_body_mass, color=color, marker='o', s=200, edgecolor='black', label=f'{species_df["species"].iloc[0]} Mean')

# Set labels and title with increased font size and professional font style
plt.xlabel("Bill Length (mm)", fontsize=14, fontweight='bold')
plt.ylabel("Body Mass (g)", fontsize=14, fontweight='bold')
plt.title("Penguin Bill Length vs Body Mass (Male Only)", fontsize=18, fontweight='bold')

# Add legend with adjusted location, border, and font style
plt.legend(loc='upper left', fontsize=12, edgecolor='black', fancybox=False)

# Annotations for regression equations
for species_df, color in zip([gentoo_df, adelie_df, chinstrap_df], colors):
    slope, intercept, r_value, p_value, std_err = linregress(species_df["bill_length_mm"], species_df["body_mass_g"])
    plt.text(50, slope * 50 + intercept + 500, f'y = {slope:.2f}x + {intercept:.2f}', fontsize=12, color=color)

# Set axis limits
plt.xlim(30, 70)
plt.ylim(2000, 7000)

# Add grid lines
plt.grid(True)

# Display the plot
plt.show()
