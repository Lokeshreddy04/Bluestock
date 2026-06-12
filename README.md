# Bluestock Financial Analytics Platform

## Overview

Bluestock Financial Analytics Platform is an end-to-end financial analytics application built using Python, PostgreSQL, Django REST Framework, React, and Power BI.

The platform analyzes financial data of Indian listed companies, generates financial health scores, identifies similar companies using machine learning, forecasts future revenue, and provides interactive dashboards through a modern web application.

---

## Features

### Financial Analytics

* Profit & Loss Analysis
* Balance Sheet Analysis
* Cash Flow Analysis
* KPI Dashboard

### Machine Learning

* Financial Health Scoring
* Company Similarity Analysis
* Revenue Forecasting
* Outlier Detection

### Backend

* Django REST Framework APIs
* Swagger/OpenAPI Documentation
* PostgreSQL Data Warehouse
* Unified Dashboard Endpoint

### Frontend

* Company Search with Autocomplete
* Interactive Company Dashboard
* Sector Analytics Dashboard
* Revenue Trend Visualization
* Similar Company Recommendations

### Business Intelligence

* Power BI Dashboard
* Sector-Level Analysis
* Risk vs Reward Analysis

---

## Architecture

CSV Files

↓

Pandas ETL Pipeline

↓

PostgreSQL Data Warehouse

↓

Machine Learning Models

↓

Django REST APIs

↓

React Frontend

↓

Power BI Dashboard

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework
* PostgreSQL

### Frontend

* React
* Axios
* React Router

### Machine Learning

* Pandas
* NumPy
* Scikit-learn

### Visualization

* Power BI
* Recharts

---

## API Endpoints

### Companies

* `/api/v1/companies/`

### Financial Statements

* `/api/v1/profit-loss/<symbol>/`
* `/api/v1/balance-sheet/<symbol>/`
* `/api/v1/cash-flow/<symbol>/`

### Analytics

* `/api/v1/health-score/<symbol>/`
* `/api/v1/forecast/<symbol>/`
* `/api/v1/peers/<symbol>/`

### Dashboard

* `/api/v1/company-dashboard/<symbol>/`

### Sectors

* `/api/v1/sectors/`
* `/api/v1/sectors/<sector_name>/`

### Documentation

* `/api/docs/`

---

## Screenshots

### Home Page

Insert: `screenshots/home.png`

### Company Dashboard

Insert: `screenshots/dashboard.png`

### Sector Analytics

Insert: `screenshots/sector.png`

### Swagger Documentation

Insert: `screenshots/swagger.png`

### Power BI Dashboard

Insert: `screenshots/powerbi.png`

---

## Future Enhancements

* Stock Price Integration
* Real-Time Market Data
* Advanced Forecasting Models
* User Authentication
* Portfolio Analytics

---

## Author

Lokesh Reddy

Built as a full-stack financial analytics and machine learning project.
