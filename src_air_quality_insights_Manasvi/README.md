# 🌍 Air Quality Insights Dashboard

## 1. Project Overview

The **Air Quality Insights Dashboard** is a Python-based data analysis project that analyzes air pollution data from different cities.

The project uses Python, Pandas and NumPy to clean datasets, perform statistical calculations, identify pollution patterns and generate useful insights about air quality.

The main objective is to understand pollution levels, compare different cities and identify unusually high PM2.5 readings.

**Note:** This project uses a synthetic educational dataset and does not represent actual government air-quality monitoring records.

---

## 2. Technologies Used

The following technologies and libraries are used:

- **Python:** Main programming language.
- **Pandas:** Data cleaning, manipulation and analysis.
- **NumPy:** Numerical and statistical calculations.
- **VS Code:** Development environment.

---

## 3. Dataset Description

The project uses a CSV dataset named `04_air_quality.csv`.

The dataset contains 360 observations from six cities:

1. Delhi
2. Ghaziabad
3. Mumbai
4. Kolkata
5. Bengaluru
6. Chennai

### Dataset Columns

| Column | Description |
|---|---|
| City | Name of the city |
| Date | Date of observation |
| PM2.5 | Fine particulate matter concentration |
| PM10 | Particulate matter concentration |
| Temperature | Recorded temperature |

---

## 4. Project Objectives

- Analyze air pollution levels across different cities.
- Identify and handle missing values.
- Calculate average, median and maximum PM2.5.
- Rank cities based on average pollution levels.
- Identify dates with the highest PM2.5 readings.
- Compare PM2.5 and PM10 concentrations.
- Calculate monthly average pollution levels.
- Detect outliers using the IQR method.
- Calculate standard deviation and percentiles using NumPy.
- Analyze the correlation between temperature and PM2.5.
- Categorize air quality using custom thresholds.
- Generate analytical reports in CSV format.

---

## 5. Data Analysis and Methodology

### A. Data Cleaning
- Identified missing values.
- Removed duplicate records.
- Replaced missing numerical values using median imputation.
- Converted the Date column into datetime format.

### B. Statistical Analysis
Calculated:
- Mean
- Median
- Maximum value
- Standard deviation
- 25th, 50th and 75th percentiles

### C. Outlier Detection

Used the Interquartile Range (IQR) method to identify unusually high or low PM2.5 readings.

### D. Correlation Analysis

Calculated the correlation between Temperature and PM2.5 to examine their linear relationship.

### E. Air Quality Categorization

Created four custom educational categories:

- Good
- Moderate
- Poor
- Very Poor

These categories are based on project-defined PM2.5 thresholds and are not official government AQI categories.

### F. Monthly and City-wise Analysis

Calculated monthly average PM2.5 levels and compared pollution levels across six cities.

---

## 6. Key Findings

Based on the synthetic dataset:

- Delhi recorded the highest average PM2.5 level.
- Bengaluru recorded the lowest average PM2.5 level.
- January was the most polluted month.
- Standard deviation of PM2.5 was 37.79.
- Two PM2.5 outliers were identified.
- Temperature and PM2.5 correlation was 0.04.
- 201 observations, or 55.83%, exceeded the selected threshold of 60 µg/m³.

---

## 7. Project Output Files

The project generates the following files inside the `output` folder:

| File Name | Description |
|---|---|
| `cleaned_air_quality.csv` | Final cleaned dataset |
| `city_pollution_ranking.csv` | City-wise pollution ranking |
| `highest_pollution_dates.csv` | Top 10 highest pollution readings |
| `monthly_pollution.csv` | Monthly average PM2.5 |
| `monthly_city_pollution.csv` | Monthly pollution comparison by city |
| `pm25_outliers.csv` | Identified outlier records |
| `pm25_pm10_comparison.csv` | City-wise PM2.5 and PM10 comparison |
| `air_quality_categories.csv` | Dataset with air-quality categories |
| `air_quality_categories_count.csv` | Number of observations in each category |

---

## 8. Public Awareness Recommendations

1. Encourage the use of public transportation and carpooling.
2. Promote regular monitoring of air pollution.
3. Increase awareness about the harmful effects of particulate matter.
4. Encourage precautions during periods of high pollution.
5. Support activities that help reduce air pollution.

---

## 9. Software Requirements

- Python 3.x
- Pandas
- NumPy
- Visual Studio Code

### Installation

Install the required libraries using:

```bash
pip install pandas numpy
```

---

## 10. Project Folder Structure

```text
AIR_QUALITY_INSIGHTS_DASHBOARD/
│
├── output/
│   ├── air_quality_categories_count.csv
│   ├── air_quality_categories.csv
│   ├── city_pollution_ranking.csv
│   ├── cleaned_air_quality.csv
│   ├── highest_pollution_dates.csv
│   ├── monthly_city_pollution.csv
│   ├── monthly_pollution.csv
│   ├── pm25_outliers.csv
│   └── pm25_pm10_comparison.csv
│
├── src_air_quality_insights_Manasvi/
│   ├── 04_air_quality.csv
│   └── air_quality_analysis.py
│
└── README.md
```

---

## 11. How to Run the Project

1. Open the project folder in Visual Studio Code.
2. Make sure Python, Pandas and NumPy are installed.
3. Ensure the dataset is available in the source folder.
4. Open the VS Code terminal.
5. Execute the following command from the main project folder:

```bash
python src_air_quality_insights_Manasvi/air_quality_analysis.py
```

6. The analysis results will appear in the terminal.
7. Generated CSV reports will be saved in the `output` folder.

---

## 12. Future Scope

The project can be enhanced in the future by:

- Integrating real-time air-quality data.
- Adding more cities and larger datasets.
- Developing an interactive dashboard.
- Implementing machine-learning-based pollution prediction.
- Adding geographical pollution comparisons.

---

## 13. Conclusion

The Air Quality Insights Dashboard demonstrates how Python, Pandas and NumPy can be used for data cleaning, statistical analysis and pollution trend identification.

The project provides useful insights into air-quality patterns and helps develop an understanding of environmental data analysis.

It also provides a foundation for future development of advanced air-quality monitoring and prediction systems.

---

**Project Name:** Air Quality Insights Dashboard

**Programming Language:** Python

**Libraries:** Pandas and NumPy

**Development Tool:** Visual Studio Code