## Real Estate Price Prediction Model

**Project Overview:** Built a machine learning model to predict property prices per unit area based on location and urban infrastructure features, using a real estate dataset from Kaggle.

**Key Accomplishments:**  
- Cleaned and analyzed a real estate dataset in Azure Data Studio (Jupyter Notebook), handling missing values and outliers.  
- Engineered a **Ridge Regression model** achieving **0.63 R-squared** and **5.91 MAE** (mean absolute error) on test data.  
- Identified key price drivers:  
  - **+$7.74 price gain per unit area** for each degree increase in latitude (moving north) - showing northern neighborhoods may be more valuable
  - **+$5.63 price gain per unit area** for each unit increase in time - showing market appreciation over time
  - **+$1.27 price gain per unit area** for each additional nearby convenience store - showing the value of neighborhood amenities
- Deployed the model in a function that returns the model's prediction and as an interactive widget for real-time predictions.  

**Technical Skills Demonstrated:**  
- Machine Learning: Ridge Regression
- Data Engineering: Feature selection, multicollinearity detection
- Tools: scikit-learn, pandas, seaborn, plotly, ipywidgets, Jupyter Notebook  
- Deployment: Pandas function, widget integration  

**Future Enhancements:**  
- Incorporate satellite imagery for greenery/urban density scoring  
- Expand location features with walkability indexes  
- Test ensemble methods (Random Forest, XGBoost)
- Compare this R-squared with simpler models or industry standards to gauge relative performance  

**Impact:** This project demonstrates end-to-end ML capabilities—from data cleaning to production deployment—providing actionable insights for property investors and urban planners to assess valuation factors in competitive markets.  Older properties near many convenience stores in northern areas hold better value.

---

### Interactive Prediction Tool

[See code](/projects/real_estate_code.html)

<br><img src="/images/realestateimage.jpg?raw=true"/>

---

### References

[1] Dataset from [Kaggle Real Estate](https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction?resource=download)
<br>[2] Cover image on home page generated from [Google Gemini](https://gemini.google.com)
