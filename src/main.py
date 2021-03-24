# For data set "Conditions_contributing_to_deaths_involving_coronavirus_disease_2019__COVID-19___by_age_group_and_state__United_States..csv"
#     For each unique age group in the data set
#         Accumulate all values from column "Covid-19 Deaths"
#         Determine mean of this set
#         Add it to the relevant Age Group column in the Mean row in the relevant _Analysis.csv file generated for this data set
#         Determine median of this set
#         Add it to the relevant Age Group column in the Median row in the relevant _Analysis.csv file generated for this data set
#         Determine mode of this set
#         Add it to the relevant Age Group column in the Mode row in the relevant _Analysis.csv file generated for this data set
#         Determine range of this set
#         Add it to the relevant Age Group column in the Range row in the relevant _Analysis.csv file generated for this data set
#         Determine variance of this set
#         Add it to the relevant Age Group column in the Variance row in the relevant _Analysis.csv file generated for this data set
#         Determine quartiles of this set
#         For each quartile
#             Add it to the relevant Age Group column in the Quartile n row in the relevant _Analysis.csv file generated for this data set
#         Determine standard deviation of this set
#         Add it to the relevant Age Group column in the Standard Deviation row in the relevant _Analysis.csv file generated for this data set

# For data set "Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State.csv"
#     For each unique age group in the data set
#         For each column with the word "Deaths"
#             Determine mean of this set
#             Add it to the relevant Age Group column in the Mean row in the relevant _Analysis.csv file generated for this data set
#             Determine median of this set
#             Add it to the relevant Age Group column in the Median row in the relevant _Analysis.csv file generated for this data set
#             Determine mode of this set
#             Add it to the relevant Age Group column in the Mode row in the relevant _Analysis.csv file generated for this data set
#             Determine range of this set
#             Add it to the relevant Age Group column in the Range row in the relevant _Analysis.csv file generated for this data set
#             Determine variance of this set
#             Add it to the relevant Age Group column in the Variance row in the relevant _Analysis.csv file generated for this data set
#             Determine quartiles of this set
#             For each quartile
#                 Add it to the relevant Age Group column in the Quartile n row in the relevant _Analysis.csv file generated for this data set
#             Determine standard deviation of this set
#             Add it to the relevant Age Group column in the Standard Deviation row in the relevant _Analysis.csv file generated for this data set

import numpy as np
import os
import pandas as pd
import csv
from scipy import stats

# Consult README.md for instructions setting up the data folder
contributing_conditions_dataset_filepath = os.path.join(os.getcwd(), "data/Conditions_contributing_to_deaths_involving_coronavirus_disease_2019__COVID-19___by_age_group_and_state__United_States..csv")
sex_age_state_dataset_filepath = os.path.join(os.getcwd(), "Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State.csv")

data = pd.read_csv(sex_age_state_dataset_filepath)

# Program works up to here
# --------------- For Provisional COVID-19 Death Counts by Sex, Age, and State dataset ---------------
data.rename(columns={"Age Group": "Age_Group"}, inplace = True)

age_groups = {
    0: 'All Ages',
    1: 'Under 1 year',
    2: '0-17 years',
    3: '1-4 years',
    4: '5-14 years',
    5: '15-24 years',
    6: '18-29 years',
    7: '25-34 years',
    8: '30-39 years',
    9: '35-44 years',
    10: '40-49 years',
    11: '45-54 years',
    12: '50-64 years',
    13: '55-64 years',
    14: '65-74 years',
    15: '75-84 years',
    16: '85 years and over'
}

covid_deaths_array = []
pneumonia_deaths_array = []
influenza_deaths_array = []
pneumonia_and_covid_deaths_array = []
pneumonia_influenza_or_covid_array = []
total_deaths_array = []
results_array = []

# Get values from CSV. Each death type list holds lists of values from each age group
for x in range(len(age_groups)):
    covid_deaths_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'COVID-19 Deaths'])
    pneumonia_deaths_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'Pneumonia Deaths'])
    influenza_deaths_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'Influenza Deaths'])
    pneumonia_and_covid_deaths_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'Pneumonia and COVID-19 Deaths'])
    pneumonia_influenza_or_covid_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'Pneumonia, Influenza, or COVID-19 Deaths'])
    total_deaths_array.append(data.loc[(data.Group == 'By Total') & (data.State != 'United States') & (data.Sex == 'All Sexes') & (data.Age_Group == age_groups.get(x))].loc[:, 'Total Deaths'])

def performstats(input):
    global results_array
    results_array = []
    for x in range(len(input)):
        y = []
        y.append(age_groups.get(x))
        #Median
        y.append(np.nanmedian(input[x].values.tolist()))
        #Mean
        y.append(np.nanmean(input[x].values.tolist()))
        #Range
        y.append(np.ptp(input[x].values.tolist()))
        #Variance
        y.append(np.nanvar(input[x].values.tolist()))
        #First Quartile
        y.append(np.nanmedian(input[x].quantile(.25)))
        #Third Quartile
        y.append(np.nanmedian(input[x].quantile(.75)))
        #Standard Deviation
        y.append(np.nanstd(input[x].values.tolist()))
        results_array.append(y)

#Testing CSV file write
header = ['Median', 'Mean', 'Range', 'Variance', '1st Quartile', '3rd Quartile', 'Standard Deviation']

performstats(covid_deaths_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_COVID-19_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

performstats(pneumonia_deaths_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_Pneumonia_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

performstats(influenza_deaths_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_Influenza_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

performstats(pneumonia_and_covid_deaths_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_Pneumonia_and_COVID-19_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

performstats(pneumonia_influenza_or_covid_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_Pneumonia_Influenza_or_COVID-19_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

performstats(total_deaths_array)
with open('Provisional_COVID-19_Death_Counts_by_Sex__Age__and_State_Total_Deaths_Analysis.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(results_array)

# ---------------------------------------------------------------------------------------------------------