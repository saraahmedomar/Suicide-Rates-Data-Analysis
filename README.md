# Global Suicide Insights

A Streamlit-based analytics project that explores global suicide data through interactive visualizations, country-specific insights, demographic analysis, and socio-economic relationships.

## Project Overview

This project analyzes suicide statistics from a cleaned and enriched dataset. It provides exploratory dashboards, country-level insights, and visual storytelling focused on patterns across gender, age groups, generations, and economic factors.

## Key Files

- `Home.py` - Main Streamlit app page for global overview, KPIs, and interactive charts.
- `pages/Country-Specific Insights.py` - Dedicated page for deep-dive analysis on a selected country.
- `pages/About & Data.py` - Supporting page for dataset and project context.
- `pages/Demographic Analysis.py` - Page for demographic trends and risk profiles.
- `pages/Prediction.py` - Prediction-focused page for modeling and forecasts.
- `pages/Socio-Economic Impact.py` - Page exploring economic drivers and correlations.
- `style_utils.py` - Theme and styling utilities used across the Streamlit app.
- `Cleaned_df.csv` - Cleaned dataset used by the app.
- `master.csv` - Original raw dataset used during preprocessing and exploration.
- `Suicide.ipynb` - Jupyter notebook for data exploration, cleaning, and feature engineering.

## Dataset

The dataset includes suicide records by country, year, sex, age group, population, suicide counts, rates per 100k, GDP, and generational segments. The sheet also contains engineered features such as `new_age` and `sex_numeric`.

## Features

- Interactive filters for year range, country, gender, and age groups
- Country-specific analysis with historical trends, peak year analysis, and ranking
- Demographic and generational breakdowns
- Socio-economic correlation visualizations
- Custom theming and dynamic insights

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the Streamlit app:

```bash
streamlit run Home.py
```

3. Open the local URL shown in the terminal to use the dashboard.

## Notes

- The app currently excludes incomplete or unreliable records for the year 2016 in the main analysis.
- Use the sidebar filters to refine the displayed visualizations.

## Contact

For updates or improvements, review the notebook and Streamlit page code to adjust filters, charts, and analysis logic.
