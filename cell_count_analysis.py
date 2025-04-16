import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# Firs part: Compute Relative Frequencies
# Defining the immune cell populations from csv file.
cell_populations = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

# Read the CSV file (I am assuming cell-count.csv is in the current directory if not we have to change code)
df = pd.read_csv('cell-count.csv')

# Computing Relative Frequencies from the cell count

# First, I am going to calculate the total cell count per sample
df['total_count'] = df[cell_populations].sum(axis=1)

# Reshape the dataframe from wide to long format for each cell population
df_long = df.melt(id_vars=['sample', 'total_count'], value_vars=cell_populations, var_name='population',
                  value_name='count')

# Calculate relative frequency (will be in percentage) for each sample and population
df_long['percentage'] = (df_long['count']/df_long['total_count']) * 100

# Saving the transformed data to CSV
output_csv = 'cell_count_rel_freq.csv'
df_long.to_csv(output_csv, index=False)
print(f"Relative frequency data saved to {output_csv}")

# Second Part: Analysis for treatment tr1 on melanoma PBMC samples
# I think I will filter data first for PBMC samples from patients who had treatment tr1 and melanoma.
df_subset = df[(df['treatment'] == 'tr1') &
               (df['sample_type'] == 'PBMC') &
               (df['condition'].str.lower() == 'melanoma')]

# To store test result
stat_results = []

# Create a directory to store plots if not already existing
plot_dir = 'plots'
os.makedirs(plot_dir, exist_ok=True)

# Loop through each cell population to generate box plots and perform statistical tests

for pop in cell_populations:
    # First, I am melting the subset so that each row corresponds to a specific population's percentage.
    temp_df = df_subset[['sample', 'total_count', pop, 'response']].copy()
    temp_df['percentage'] = (temp_df[pop] / temp_df['total_count']) * 100

    # To see the responders and non_responders clearly
    responders = temp_df[temp_df['response'] == 'y']['percentage']
    non_responders = temp_df[temp_df['response'] == 'n']['percentage']

    # I am not sure about this but through research.
    # I decided to use matplotlib to generate the box plots(Still learning)
    plt.figure()
    plt.boxplot([responders, non_responders], labels=['Responder', 'Non-responder'])
    plt.title(f'{pop} Relative Frequency')
    plt.ylabel('Percentage (%)')
    plot_file = os.path.join(plot_dir, f"{pop}_boxplot.png")
    plt.savefig(plot_file)
    plt.close()
    print(f"Boxplot saved to {plot_file}")

    # Perform Mann-Whitney U test (non-parametric test)
    if len(responders) > 0 and len(non_responders) > 0:
        stat, p = mannwhitneyu(responders, non_responders, alternative='two-sided')
    else:
        stat, p = None, None

    stat_results.append({
        'population': pop,
        'statistic': stat,
        'p_value': p
    })

# Save results to a text file
with open('statistical_results.txt', 'w') as f:
    header = "Population\tMann-Whitney U Statistic\tp-value\n"
    f.write(header)
    for result in stat_results:
        line = f"{result['population']}\t{result['statistic']}\t{result['p_value']}\n"
        f.write(line)