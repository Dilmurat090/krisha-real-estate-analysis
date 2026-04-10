# Krisha.kz Real Estate Price Prediction

## Overview
Parsed 10,000+ real estate listings from Krisha.kz (Almaty) 
and built ML models to predict apartment prices.

## Results
| Model | R² (CV) | R² (Test) | MAE |
|-------|---------|-----------|-----|
| Linear Regression | 0.731 | 0.697 | 14,436,488 ₸ |
| Random Forest | 0.804 | 0.801 | 10,590,039 ₸ |

Random Forest performed better with R² = 0.80 on test data.

## Stack
Python, pandas, BeautifulSoup, scikit-learn, Matplotlib, Seaborn

## Structure
- `parcing_data.py` — web scraping script
- `EDA.ipynb` — exploratory data analysis  
- `models.ipynb` — ML models and evaluation
- `krisha_clean.csv` — cleaned dataset
