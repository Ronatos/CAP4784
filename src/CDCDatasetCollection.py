# Analyze statistical information of COVID-19 data including mean, median, mode,
# range, variance, quartiles, and standard deviation
#
# Alex Derby for Team Eva - CAP 4784 Data Analytics

import numpy as np
import os
import pandas as pd
from scipy import stats

contributing_conditions_dataset_filepath = os.path.join(os.getcwd(), "data/Conditions_contributing_to_deaths_involving_coronavirus_disease_2019__COVID-19___by_age_group_and_state__United_States..csv")
sex_age_state_dataset_filepath = os.path.join(os.getcwd(), "Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State.csv")

data = pd.read_csv(contributing_conditions_dataset_filepath)

columns = {
    0: 'COVID-19 Deaths',
    1: 'Pneumonia Deaths',
    2: 'Influenza Deaths',
    3: 'Pneumonia and COVID-19 Deaths'
}

age_groups = { 0: '0-24', 1: '25-44', 2: '45-64', 3: '65+'}

rows = [data.iloc[1:6], data.iloc[6:10], data.iloc[10:14], data.iloc[14:17]]

median_arr = np.zeros((4,4))
# mode_arr = np.zeros((4,4))
mean_arr = np.zeros((4,4))
range_arr = np.zeros((4,4))
variance_arr = np.zeros((4,4))
standard_deviation_arr = np.zeros((4,4))

# Get median
for x in range(len(rows)):
    print('Median for ages ' + str(age_groups.get(x)))
    row = rows[x]
    for y in range(len(columns)):
        median_arr[x][y] = np.median(row.loc[:,columns.get(y)].values.tolist())
        print(str(median_arr[x][y]), end=" ")
    print()
print()

# Get Mean
for x in range(len(rows)):
    print('Mean for ages ' + str(age_groups.get(x)))
    row = rows[x]
    for y in range(len(columns)):
        mean_arr[x][y] = np.mean(row.loc[:,columns.get(y)].values.tolist())
        print(mean_arr[x][y], end=" ")
    print()
print()

# Get Range
for x in range(len(rows)):
    print('Range for ages ' + str(age_groups.get(x)))
    row = rows[x]
    for y in range(len(columns)):
        range_arr[x][y] = np.ptp(row.loc[:,columns.get(y)].values.tolist())
        print(range_arr[x][y], end=" ")
    print()
print()

# Get Vairance

# Get Quartiles

# Get Standard Deviation
for x in range(len(rows)):
    print('Standard Deviaton for ages ' + str(age_groups.get(x)))
    row = rows[x]
    for y in range(len(columns)):
        standard_deviation_arr[x][y] = np.std(row.loc[:,columns.get(y)].values.tolist())
        print(standard_deviation_arr[x][y], end=" ")
    print()
