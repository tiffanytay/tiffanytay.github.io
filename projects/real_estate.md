## Real Estate Price Prediction Model

**Project Overview:** Built a machine learning model to predict property prices per unit area based on location and urban infrastructure features, using a real estate dataset from Kaggle.

**Key Accomplishments:**  
- Cleaned and analyzed a real estate dataset in Azure Data Studio (Jupyter Notebook), handling missing values and outliers.  
- Engineered a **Ridge Regression model** achieving **0.82 R-squared** and **5.2 MAE** (mean absolute error) on test data.  
- Identified key price drivers:  
  - **-12% price impact** per km from public transit  
  - **+3.8% price gain** per nearby convenience store  
  - **-0.4% annual depreciation** from house age  
- Deployed the model as an interactive web widget for real-time predictions.  

**Technical Skills Demonstrated:**  
- Machine Learning: Ridge Regression, hyperparameter tuning (alpha=1.2)  
- Data Engineering: Feature selection, outlier detection (IQR method)  
- Tools: scikit-learn, pandas, Matplotlib, Jupyter Notebook  
- Deployment: Model serialization (Pickle), widget integration  

**Future Enhancements:**  
- Incorporate satellite imagery for greenery/urban density scoring  
- Expand location features with walkability indexes  
- Test ensemble methods (Random Forest, XGBoost)  

**Impact:** This project demonstrates end-to-end ML capabilities—from data cleaning to production deployment—providing actionable insights for property investors and urban planners to assess valuation factors in competitive markets.  

---

### Interactive Prediction Tool

[See tool](/airbnbIndex.html)

<img src="images/airbnb_screenshot_UWS.png?raw=true"/>

---

### References

[1] Dataset from [Kaggle Real Estate](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction?resource=download)
[2] Image generated from [Google Gemini](https://gemini.google.com)
