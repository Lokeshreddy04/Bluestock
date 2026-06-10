# Bluestock Financial Analytics Platform

## Overview

An end-to-end financial analytics platform built using Python, PostgreSQL, Power BI, Machine Learning, and Django REST Framework.

The project analyzes financial statements of publicly listed companies, generates financial health scores, performs anomaly detection and clustering, and exposes insights through REST APIs and interactive dashboards.

---

## Features

### Data Engineering

* Data cleaning and preprocessing using Pandas
* ETL pipeline for financial statement data
* PostgreSQL data warehouse
* Star schema design

### Business Intelligence

* Executive Overview Dashboard
* Company Deep Dive Dashboard
* Sector Analytics Dashboard
* Risk & Leverage Analysis
* Growth & Profitability Dashboard
* Cash Flow & Operational Efficiency Dashboard
* Investment Decision Dashboard

### Machine Learning

* Financial Health Scoring
* Outlier Detection
* Isolation Forest Anomaly Detection
* K-Means Clustering
* Peer Similarity Engine
* Revenue Forecasting

### Backend APIs

Built using Django REST Framework.

#### Available Endpoints

* `/api/v1/companies/`
* `/api/v1/companies/<symbol>/`
* `/api/v1/profit-loss/<symbol>/`
* `/api/v1/balance-sheet/<symbol>/`
* `/api/v1/cash-flow/<symbol>/`
* `/api/v1/health-score/<symbol>/`
* `/api/v1/company-dashboard/<symbol>/`

#### API Documentation

* `/api/docs/`
* `/api/schema/`

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Analytics

* Pandas
* NumPy
* Scikit-Learn
* Statsmodels

### Visualization

* Power BI

### Documentation

* Swagger / OpenAPI

---

## Project Structure

```text
backend/
notebooks/
powerbi/
sql/
requirements.txt
README.md
```

---

## Future Enhancements

* React Frontend
* JWT Authentication
* User Watchlists
* Portfolio Tracking
* Automated Data Refresh
* Cloud Deployment

---

## Author

Lokesh Reddy
