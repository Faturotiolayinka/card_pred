# Card Prediction Flask Web App

## Overview

This project is a Flask-based web application for predicting the likelihood of a card transaction being fraudulent. It features user registration, login, and a prediction dashboard. The frontend is built with HTML/CSS/JS, the backend uses Flask (Python), and user data is stored in JSON format.

---

## Data Used

The app uses the following features for prediction:

- **distance_from_home**: Distance from the cardholder’s home to the transaction location.
- **distance_from_last_transaction**: Distance from the location of the last transaction.
- **ratio_to_median_purchase_price**: Ratio of the transaction amount to the median purchase price.
- **repeat_retailer**: 1 if the retailer is a repeat retailer, 0 otherwise.
- **used_chip**: 1 if the card’s chip was used, 0 otherwise.
- **used_pin_number**: 1 if a PIN was used, 0 otherwise.

---

## Problem Statement

The application addresses the problem of **credit card fraud detection**. By analyzing transaction details, it helps users determine if a transaction is likely to be fraudulent, providing both a prediction and an explanation.

---

## Features & Steps

### 1. Project Setup

- Flask project structure with `app.py` as the main file.
- `templates/` for HTML files, `static/` for images and CSS.

### 2. Frontend

- Registration, login, and prediction pages with modern, responsive design.
- Semi-transparent containers, background images, and accessibility features.
- Client-side validation, autocomplete, autofocus, and loading indicators.
- Simple CAPTCHA on login for security.

### 3. Backend

- User registration and login with password hashing.
- User data stored securely in a JSON file.
- Prediction logic based on user input, returning "Fraud" or "Not Fraud".
- Dynamic explanations for predictions based on input features.

### 4. Dashboard

- Displays prediction results and explanations.
- Uses semantic HTML and is accessible.

### 5. Optimization

- Minified and inlined CSS/JS for fast loading.
- Compressed and lazy-loaded images.
- Client-side and server-side validation.
- Responsive and accessible design.
- Prepared `requirements.txt` and `Procfile` for deployment.

### 6. Deployment

- Code hosted on GitHub.
- Deployed on Render for public access.
