# Cell Count Analysis Project

## Author
- Name: Dustin Nguyen
- GitHub: DustinDungNguyen
- Github repo: 
- Date: 16th April, 2025

## Overview

The Cell Count Analysis Project is designed to analyze cell count data from various immune cell populations. This project processes raw cell count data, converts it to relative frequencies, and compares these frequencies in melanoma patients under treatment `tr1` by their response status (responders vs. non-responders). In addition, the project includes a database design prototype with sample SQL queries demonstrating potential analytical queries and data aggregation strategies.

## Files in the Project

- **cell-count.csv**: Input data file containing cell count information and sample metadata.
- **cell_count_analysis.py**: Python script that:
  - Converts raw cell counts into relative frequencies.
  - Generates a CSV file (`cell_count_rel_freq.csv`) with the transformed data.
  - Produces boxplots for each immune cell population comparing responders and non-responders (saved in the `plots/` directory).
  - Performs statistical tests (Mann–Whitney U tests) and writes the results to `statistical_results.txt`.
- **requirements.txt**: Lists the Python packages needed (pandas, matplotlib, scipy).
- **clean.sh**: Shell script to remove output files (CSV, plots, statistical results) so that the project starts clean.
- **DATABASE_DESIGN.md**: A document detailing the proposed database schema and benefits of using a database for the data.
- **queries.sql**: Contains sample SQL queries that summarize subjects, filter samples by criteria, and provide breakdowns by projects, response status, and gender.
- **README.md**: This file, providing instructions on setting up and running the project.

## Setup Instructions

### Prerequisites

- A Unix-based operating system.
- Python 3 installed on your system.

### Installation

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/DustinDungNguyen/cell_count_project.git
   cd cell_count_project
   
2. **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate

3. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt

### Running the Project
1. **Clean Previous Outputs (Optional but Recommended)**
- Before running the analysis, remove any previously generated files. Execute the cleanup script:
    ```bash
    ./clean.sh

This script deletes:
- The output CSV file (cell_count_rel_freq.csv).

- The statistical_results.txt file.

- The plots/ directory (and its contents).

2. **Execute the Analysis Script**
- Run the main analysis script to process the input data, generate the transformed CSV, produce boxplots, and output statistical test results:

  ```bash   
   python cell_count_analysis.py 
  
- After running the script, you should see messages indicating

- The creation of cell_count_rel_freq.csv.

- The saving of boxplot images in the plots/ directory.

- The creation of statistical_results.txt.

3. **Verify the Outputs**
- CSV Output: Open cell_count_rel_freq.csv to confirm that it contains the columns: sample, total_count, population, count, and percentage.

- Box plots: Check the plots/ directory for the generated PNG files, one per immune cell population.

- Statistical Results: Review the statistical_results.txt file for p-values and other test statistics.

## Database Design and SQL Queries
- DATABASE_DESIGN.md: Contains the proposed database schema along with an explanation of its advantages, including handling scalability, data integrity, and flexibility for querying.

- queries.sql: Includes sample SQL queries to:

- Summarize the number of subjects per condition.

- Return baseline melanoma PBMC samples (plus bladder cancer samples as specified) for treatment tr1.

- Provide breakdowns by project, response status, and gender.

