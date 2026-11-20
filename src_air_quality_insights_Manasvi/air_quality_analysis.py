#Name:MANASVI
#Email:manasvi.26b15410295@abes.ac.in
#Admission no.:2026B15410295
#GITHUB REPOSITORY NAME:https://github.com/manasvicode28/Air-Quality-insights-Dashboard_Manasvi



# ============================================================
# PROJECT: AIR QUALITY INSIGHTS DASHBOARD
# Technologies: Python, Pandas and NumPy
# ============================================================


# STEP 1: IMPORT LIBRARIES

import pandas as pd
import numpy as np
import os

os.makedirs("output", exist_ok=True)

# STEP 2: LOAD AND INSPECT DATASET

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

data_path = BASE_DIR / "04_air_quality.csv"

df = pd.read_csv(data_path)

print("\n========== DATASET INFORMATION ==========")

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe())


# STEP 3: DATA CLEANING

print("\n========== DATA CLEANING ==========")

# Identify missing values before cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Identify duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values using median
df['PM2.5'] = df['PM2.5'].fillna(df['PM2.5'].median())

df['PM10'] = df['PM10'].fillna(df['PM10'].median())

df['Temperature'] = df['Temperature'].fillna(
    df['Temperature'].median()
)

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract month information
df['Month'] = df['Date'].dt.month

df['Month_Name'] = df['Date'].dt.month_name()


# STEP 4: BASIC POLLUTION ANALYSIS

print("\n========== BASIC POLLUTION ANALYSIS ==========")

# Calculate average, median and maximum PM2.5
average_pm25 = df['PM2.5'].mean()

median_pm25 = df['PM2.5'].median()

maximum_pm25 = df['PM2.5'].max()

print("\nAverage PM2.5:", round(average_pm25, 2))

print("Median PM2.5:", round(median_pm25, 2))

print("Maximum PM2.5:", round(maximum_pm25, 2))


# Rank cities according to average PM2.5
city_pollution = df.groupby('City')['PM2.5'].mean()

city_ranking = city_pollution.sort_values(
    ascending=False
)

print("\nCity-wise Pollution Ranking:")
print(city_ranking.round(2))

city_ranking.to_csv(
    'output/city_pollution_ranking.csv'
)


# Identify dates with highest PM2.5 readings
highest_pollution = df.sort_values(
    by='PM2.5',
    ascending=False
)

print("\nTop 10 Highest PM2.5 Readings:")

print(
    highest_pollution[
        ['City', 'Date', 'PM2.5']
    ].head(10)
)

highest_pollution[
    ['City', 'Date', 'PM2.5']
].head(10).to_csv(
    'output/highest_pollution_dates.csv',
    index=False
)


# Compare PM2.5 and PM10 city-wise
pollution_comparison = df.groupby('City')[
    ['PM2.5', 'PM10']
].mean()

print("\nCity-wise PM2.5 and PM10 Comparison:")
print(pollution_comparison.round(2))

pollution_comparison.to_csv(
    'output/pm25_pm10_comparison.csv'
)


# STEP 5: MONTHLY POLLUTION ANALYSIS

print("\n========== MONTHLY POLLUTION ANALYSIS ==========")

monthly_pollution = df.groupby(
    'Month_Name'
)['PM2.5'].mean()

month_order = ['January', 'February', 'March']

monthly_pollution = monthly_pollution.reindex(
    month_order
)

print("\nMonthly Average PM2.5:")
print(monthly_pollution.round(2))

monthly_pollution.to_csv(
    'output/monthly_pollution.csv'
)

most_polluted_month = monthly_pollution.idxmax()

print("\nMost Polluted Month:", most_polluted_month)


# STEP 6: NUMPY STATISTICAL ANALYSIS

print("\n========== NUMPY STATISTICAL ANALYSIS ==========")

# Convert PM2.5 column into NumPy array
pm25_array = df['PM2.5'].to_numpy()

# Calculate standard deviation
pm25_std = np.std(pm25_array)

print("\nStandard Deviation of PM2.5:")
print(round(pm25_std, 2))

# Calculate percentiles
p25 = np.percentile(pm25_array, 25)

p50 = np.percentile(pm25_array, 50)

p75 = np.percentile(pm25_array, 75)

print("\nPM2.5 Percentiles:")

print("25th Percentile:", round(p25, 2))

print("50th Percentile:", round(p50, 2))

print("75th Percentile:", round(p75, 2))


# STEP 7: OUTLIER DETECTION USING IQR

print("\n========== OUTLIER DETECTION ==========")

Q1 = np.percentile(pm25_array, 25)

Q3 = np.percentile(pm25_array, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR

print("\nIQR:", round(IQR, 2))

print("Lower Limit:", round(lower_limit, 2))

print("Upper Limit:", round(upper_limit, 2))

# Identify outliers
outliers = df[
    (df['PM2.5'] < lower_limit) |
    (df['PM2.5'] > upper_limit)
]

print("\nNumber of Outliers:", len(outliers))

print("\nOutlier Records:")

print(
    outliers[
        ['City', 'Date', 'PM2.5']
    ]
)

outliers.to_csv(
    'output/pm25_outliers.csv',
    index=False
)


# STEP 8: CORRELATION AND THRESHOLD ANALYSIS

print("\n========== CORRELATION ANALYSIS ==========")

# Calculate correlation between Temperature and PM2.5
correlation = df['Temperature'].corr(df['PM2.5'])

print("\nCorrelation between Temperature and PM2.5:")

print(round(correlation, 2))


# Select a PM2.5 threshold
threshold = 60

above_threshold = df[
    df['PM2.5'] > threshold
]

percentage = (
    len(above_threshold) / len(df)
) * 100

print("\nPM2.5 Threshold Analysis:")

print("Selected Threshold:", threshold)

print("Readings Above Threshold:", len(above_threshold))

print("Percentage Above Threshold:",
      round(percentage, 2), "%")


# STEP 9: AIR QUALITY CATEGORIZATION

print("\n========== AIR QUALITY CATEGORIES ==========")

# Custom educational thresholds
def categorize_air_quality(value):

    if value <= 30:
        return "Good"

    elif value <= 60:
        return "Moderate"

    elif value <= 90:
        return "Poor"

    else:
        return "Very Poor"


# Create new category column
df['Air_Quality_Category'] = df['PM2.5'].apply(
    categorize_air_quality
)

# Count observations in each category
category_counts = df['Air_Quality_Category'].value_counts()

print("\nAir Quality Category Counts:")
print(category_counts)

category_counts.to_csv(
    'output/air_quality_categories_count.csv'
)


# Save categorized dataset
df.to_csv(
    'output/air_quality_categories.csv',
    index=False
)


# STEP 10: MONTHLY POLLUTION COMPARISON CITY-WISE

print("\n========== CITY-WISE MONTHLY ANALYSIS ==========")

monthly_city = df.groupby(
    ['City', 'Month_Name']
)['PM2.5'].mean().unstack()

monthly_city = monthly_city.reindex(
    columns=month_order
)

print("\nMonthly Average PM2.5 by City:")
print(monthly_city.round(2))

monthly_city.to_csv(
    'output/monthly_city_pollution.csv'
)


# STEP 11: PUBLIC AWARENESS RECOMMENDATIONS

print("\n========== PUBLIC AWARENESS RECOMMENDATIONS ==========")

highest_city = city_ranking.idxmax()

lowest_city = city_ranking.idxmin()

highest_month = monthly_pollution.idxmax()

print("\n1. Pollution Control:")

print(
    f"Focus pollution-control efforts in {highest_city}, "
    "which has the highest average PM2.5 in this dataset."
)

print("\n2. Use Public Transport:")

print(
    "Encourage buses, metro services, carpooling "
    "and cycling to help reduce vehicle emissions."
)

print("\n3. Regular Monitoring:")

print(
    f"{round(percentage, 2)}% of observations exceed "
    f"the selected threshold of {threshold}."
)

print("\n4. Seasonal Awareness:")

print(
    f"{highest_month} has the highest monthly average "
    "PM2.5 in this dataset. Monitor pollution levels "
    "during this period."
)

print("\n5. Public Health Awareness:")

print(
    "Educate people about air pollution and ways "
    "to reduce exposure during high-pollution periods."
)


# STEP 12: SAVE FINAL CLEANED DATASET

print("\n========== FINAL PROJECT OUTPUT ==========")

df.to_csv(
    'output/cleaned_air_quality.csv',
    index=False
)

print("\nFinal cleaned dataset saved successfully!")

print("Total Rows:", len(df))

print("Total Columns:", len(df.columns))

print("\nAll analysis files have been saved in the output folder.")

print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")
