# Bluestock – AI-Powered Financial Analytics Platform

## Live Application

### Frontend (Vercel)

https://bluestock.vercel.app

### Backend API (Render)

https://bluestock-6rhm.onrender.com

---

# Overview

Bluestock is an AI-powered financial analytics platform designed to provide company-level financial insights, health scoring, peer comparison, revenue forecasting, and sector analytics for Indian listed companies.

The project combines Data Engineering, Machine Learning, Backend Development, Frontend Development, Cloud Deployment, and Financial Analytics into a single production-ready application.

---

# Key Features

## Company Search

* Real-time company search
* Auto-complete suggestions
* Symbol-based lookup

## Company Dashboard

* Revenue Analysis
* Net Profit Analysis
* Balance Sheet Metrics
* Cash Flow Analysis
* Financial Health Score
* Revenue Forecasting
* Peer Company Recommendations

## Sector Analytics

* Sector-wise company exploration
* Industry comparison
* Sector performance insights

## Machine Learning Features

### Financial Health Score

Companies are classified into:

* Excellent
* Good
* Average
* Weak

based on financial performance indicators.

### Revenue Forecasting

Predicts future company revenue using historical financial data.

### Peer Similarity Engine

Recommends similar companies based on financial characteristics and business performance.

---

# System Architecture

Frontend (React + Vite)

↓

Django REST API

↓

PostgreSQL Data Warehouse

↓

Machine Learning Models

↓

Neon Cloud Database

---

# Tech Stack

## Frontend

* React
* Vite
* Axios
* React Router
* CSS

## Backend

* Django
* Django REST Framework
* Gunicorn
* WhiteNoise

## Database

* PostgreSQL
* Neon Database

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy

## Deployment

* Vercel (Frontend)
* Render (Backend)
* Neon (Database)

## Development Tools

* Git
* GitHub
* VS Code
* pgAdmin

---

# Database Schema

## Dimension Tables

### dim_company

Stores company master information.

### dim_sector

Stores sector classifications.

### dim_year

Stores fiscal period information.

### dim_health_label

Stores health score categories.

---

## Fact Tables

### fact_profit_loss

Profit and loss statements.

### fact_balance_sheet

Balance sheet information.

### fact_cash_flow

Cash flow statements.

### fact_ml_scores

Machine learning generated health scores.

### fact_forecasts

Revenue forecast predictions.

### fact_peers

Peer company recommendations.

### fact_analysis

Analytical financial metrics.

### fact_pros_cons

Company strengths and weaknesses.

---

# Machine Learning Pipeline

## Financial Health Scoring

### Input Features

* Revenue Growth
* Profit Growth
* Debt-to-Equity Ratio
* Asset Strength
* Cash Flow Metrics

### Outputs

* Health Score
* Health Label

---

## Revenue Forecasting

### Input

Historical revenue data

### Output

Future revenue prediction

---

## Peer Similarity Engine

### Input

Financial metrics and company fundamentals

### Output

Top similar companies

---

# API Endpoints

## Companies

GET

/api/v1/companies/

GET

/api/v1/companies/<symbol>/

---

## Search

GET

/api/v1/search/?q=tcs

---

## Dashboard

GET

/api/v1/company-dashboard/<symbol>/

---

## Financial Statements

GET

/api/v1/profit-loss/<symbol>/

GET

/api/v1/balance-sheet/<symbol>/

GET

/api/v1/cash-flow/<symbol>/

---

## Machine Learning

GET

/api/v1/health-score/<symbol>/

GET

/api/v1/forecast/<symbol>/

GET

/api/v1/peers/<symbol>/

---

## Sector Analytics

GET

/api/v1/sectors/

GET

/api/v1/sectors/<sector_name>/

---

# Screenshots

## Home Page

![Home](screenshots/Home.png.png)

## Company Dashboard

![Dashboard](screenshots/dashboard.png.png)

## Sector Analytics

![Sector Analytics](screenshots/sector.png.png)

## Power BI Dashboard

![Power BI](screenshots/Power BI.png.png)

---

# Deployment Journey

This project was successfully deployed using:

* Neon for cloud PostgreSQL hosting
* Render for Django backend deployment
* Vercel for React frontend deployment

Key deployment challenges solved:

* PostgreSQL schema migration to Neon
* Django model synchronization
* Production API integration
* Dependency resolution
* Render deployment troubleshooting
* Vercel frontend integration
* API routing and endpoint debugging

---

# Future Improvements

## AI Financial Copilot

Natural language financial analysis:

* Why is TCS healthy?
* Compare TCS and Infosys.
* What are the risks of Reliance?

## Portfolio Analytics

* Portfolio tracking
* Risk assessment
* Investment recommendations

## Advanced Forecasting

* LSTM forecasting
* Multi-year projections

## Real-Time Market Data

* Live stock prices
* Market sentiment analysis

## Authentication

* User login
* Watchlists
* Personalized dashboards

---

# Author

Lokesh Reddy

Aspiring AI Engineer focused on building practical AI-powered applications that solve real-world problems.

---

# License

MIT License
