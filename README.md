# Hospital Management System with AI-Integrated Customer Feedback and Stock Management

## Overview

This project is a comprehensive **Hospital Management System (HMS)** that integrates **AI-powered customer feedback analysis** and **intelligent stock/inventory management**. The system automates key hospital operations, enhances patient experience through real-time sentiment analysis of feedback, and optimizes resource management using AI-driven inventory forecasting.

As the **full-stack developer and solution architect**, I was responsible for the design, development, and deployment of the system, ensuring it is scalable, secure, and efficient.

## Features

### 1. **AI-Integrated Customer Feedback Reporting**
- **Sentiment Analysis**: Analyzes patient feedback to assess satisfaction levels using Natural Language Processing (NLP).
- **Automated Reporting**: Generates dynamic reports to visualize feedback trends and insights, helping management address areas of concern.
- **Real-Time Feedback Categorization**: Classifies feedback into actionable categories (positive, neutral, negative) for quick review.

### 2. **AI-Based Stock and Inventory Management**
- **Predictive Inventory Forecasting**: Uses machine learning models to predict inventory demand based on historical data and hospital usage trends.
- **Automated Restocking Alerts**: Alerts management when stocks are low and automates the reordering process.
- **Supply Chain Optimization**: Minimizes wastage by aligning inventory levels with actual demand, reducing excess stock and shortages.

### 3. **User-Friendly Interface**
- A responsive front-end built with **React** to manage and display patient records, feedback reports, and inventory data.
- Real-time dashboards to monitor hospital operations, feedback trends, and inventory status.

### 4. **Data Security and Compliance**
- Ensures compliance with **HIPAA** and other healthcare data privacy regulations.
- Implements **role-based access control (RBAC)** to restrict access based on user roles (e.g., admin, doctor, nurse).

## Technologies Used

- **Frontend**: React, JavaScript, HTML5, CSS3
- **Backend**: Django (Python), REST APIs
- **AI/ML**: TensorFlow, Scikit-Learn, Natural Language Processing (NLP), Sentiment Analysis
- **Database**: PostgreSQL, SQL
- **Cloud**: AWS (EC2, RDS, S3)
- **Other**: Docker (for containerization), Git (version control)

## Installation

### Prerequisites

Before running the project, make sure you have the following installed on your machine:

- Python 3.x
- Node.js (for React front-end)
- SQLlite or any compatible database
- Docker (optional, for containerization)

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshanaWAJ/hospital_management_system.git
   cd hospital-management-system
   pip install virtualenv
   env/scripts/activate
   pip install django
   pip install transformers torch
   python manage.py runserver
   
