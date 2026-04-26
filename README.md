 Airline Data Analysis Dashboard

 Project Overview
This project is an interactive web application developed to explore and analyze a large-scale airline dataset (98,619 records). The primary goal is to investigate data quality and perform a statistical analysis to determine if passenger demographics, specifically Age, have any impact on Flight Status (On Time, Delayed, or Cancelled).

This dashboard was created as part of the TM351: Data Management & Analysis course at the Arab Open University.


 Tech Stack
Language: Python

Web Framework: Streamlit

Data Manipulation: Pandas

Visualization: Plotly Express (Interactive Charts)

Statistical Logic: Chi-Square Test for Independence

 Key Features
Data Quality Assessment: Real-time tracking of missing values, duplicates, and data validity.

Interactive Filtering: Filter data by continent to see regional flight performance.

Hypothesis Testing: Visual and statistical investigation into the relationship between Age Groups and flight outcomes.

Responsive Visualizations: Interactive Stacked Bar Charts and Boxplots that provide detailed insights on hover.

 Research Findings
Hypothesis: "Is there a significant difference in flight status based on passenger age?"

Result: The analysis showed no statistically significant correlation between age and flight status. Delays and cancellations appear to be uniformly distributed across all age groups, suggesting external factors (weather, technicals) are the primary drivers of flight status.

📁 File Structure
app.py: The main Streamlit application code.

requirements.txt: List of Python dependencies.

Airline Dataset Updated - v2.csv: The core dataset used for analysis.