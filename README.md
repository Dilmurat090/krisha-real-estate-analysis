# Krisha.kz Real Estate Price Prediction

## Overview
Parsed 10000+ real estate listings from Krisha.kz (Almaty) 
and built ML models to predict apartment prices.

## Results
| Model | R² (CV) | R² (Test) | RMSE |
|-------|---------|-----------|------|
| Linear Regression | 0.73 | 0.69 | 15,877,381 ₸ |
| Random Forest | 0.80 | 0.80 | 18,413,496 ₸ |

## Stack
Python, pandas, BeautifulSoup, scikit-learn, Matplotlib, Seaborn

## Structure
- parcing_data.py — web scraping script
- EDA.ipynb — exploratory data analysis
- models.ipynb — ML models and evaluation
