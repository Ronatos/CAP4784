import numpy
import scipy.stats


data = numpy.genfromtxt('brfss-cdc.csv', dtype='int', delimiter=',', skip_header=1)

print("\nFirst Five Rows of the Data:")
first_5_rows = data[:5, :6]
print(first_5_rows)
print("Shape of the data:", data.shape)

print("\nDescriptive Statistics for Weight Change Data:")
weight_change = numpy.subtract(data[:, 2], data[:, 3])
weight_change_mean = numpy.mean(weight_change)
weight_change_median = numpy.median(weight_change)
weight_change_standard_deviation = numpy.std(weight_change)
weight_change_interquartile_range = scipy.stats.iqr(weight_change)
print("Mean:", numpy.round(weight_change_mean, 2))
print("Median:", weight_change_median)
print("Standard Deviation:", numpy.round(weight_change_standard_deviation, 2))
print("Interquartile Range:", weight_change_interquartile_range)

print("\nFirst Five Rows of the Data with Weight Changes:")
data = numpy.column_stack((data, weight_change))
first_5_rows = data[:5, :7]
print(first_5_rows)
print("Shape of the data:", data.shape)

print("\nFirst Five Rows of the Data relevant to Males:")
male_data = data[data[:, 5] == 1, :]  # boolean mask saves the day
first_5_rows = male_data[:5, :7]
print(first_5_rows)
print("Shape of the data:", male_data.shape)

# I did this in this way to mirror the screenshots provided,
# but wouldn't it be more useful to do these operations on the
# weight change column?
print("\nDescriptive Statistics for Data relevant to Males:")
print("Mean:", numpy.round(numpy.mean(male_data), 2))
print("Median:", numpy.median(male_data))
print("Standard Deviation:", numpy.round(numpy.std(male_data), 2))
print("Interquartile Range:", scipy.stats.iqr(male_data))

print("\nFirst Five Rows of the Data relevant to Females:")
female_data = data[data[:, 5] == 2, :]  # boolean mask saves the day
first_5_rows = female_data[:5, :7]
print(first_5_rows)
print("Shape of the data:", female_data.shape)

# I did this in this way to mirror the screenshots provided,
# but wouldn't it be more useful to do these operations on the
# weight change column?
print("\nDescriptive Statistics for Data relevant to Females:")
print("Mean:", numpy.round(numpy.mean(female_data), 2))
print("Median:", numpy.median(female_data))
print("Standard Deviation:", numpy.round(numpy.std(female_data), 2))
print("Interquartile Range:", scipy.stats.iqr(female_data))
