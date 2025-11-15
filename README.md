# Crop Recommendation & Yield Prediction System  
### Leveraging Machine Learning for Sustainable Agriculture
### By: Fawaaz Kamali Siddiqui, Bilal Sheikh, Mousa Kahloon, Hassan Akbar

---

## 🌱 Introduction

This project develops a **machine-learning–powered crop recommendation and yield prediction system**.  
Using three real-world datasets — **crop profiles**, **current field conditions**, and **historical field performance** — our goal is to determine:

- Which crop is **most suitable** for a given field
- How sustainable that crop would be under current & predicted conditions
- Expected **yield (t/ha)** based on available environmental and agronomic inputs

We implemented a **HistGradientBoostingRegressor**, chosen for its ability to:

- Handle **missing values (NaNs) natively**
- Support **numerical and encoded categorical input**
- Work efficiently on medium-sized tabular datasets  
- Provide competitive performance compared to XGBoost/LightGBM without requiring external dependencies

This model forms the computational backbone of a future **Streamlit-based interactive dashboard**.

---

## 🔧 Our Process

### 1. **Data Preparation**
We used three CSV files:

1. `crop_profiles_data.csv`  
2. `current_conditions_data.csv`  
3. `field_historical_data.csv`

Before model training, datasets underwent critical cleaning:

- Removed unrealistic crop yields (e.g., **yield > 200 t/ha**)
- Converted temperature values with trailing `F` to Celsius
- Standardized units and column formats
- Ensured consistent naming across datasets
- Treated categorical features (crop types, soil type, irrigation) using **scikit-learn's categorical encoding**
- Ensured target variable `yield_t_ha` had **no NaN values**

### 2. **Model Selection**
We initially attempted GradientBoostingRegressor but switched to:

### ✅ **HistGradientBoostingRegressor**

Selected due to:

- Native handling of missing data  
- Strong performance on tabular datasets  
- Faster training vs. classic Gradient Boosting  
- Handles categorical features via `CategoricalDtype`

### 3. **Training the Model**

- We assigned `df = historical_data_df` (no new copy created).  
- Split into training/testing sets (80/20).  
- Converted categorical columns into `category` types for the model.  
- Trained the Hist Gradient Boosting model with hyperparameters similar to XGBoost:
  - `max_depth`
  - `learning_rate`
  - `max_leaf_nodes`
  - `min_samples_leaf`

### 4. **Model Evaluation**

We used:

- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**

Example output:

MSE: 9.02
RMSE: 3.00


This means:

- On average, predictions differ from actual yield by **≈3 t/ha**
- This is acceptable depending on crop variability, but there is room for improvement

---

## 📊 Our Findings (So Far)

1. **Environmental variables** (temperature, rainfall, soil moisture) show strong correlation with yield.
2. **Crop type, soil classification, and irrigation method** significantly affect yield predictability.
3. Using **HistGradientBoostingRegressor reduced preprocessing complexity**, especially around missing values.
4. The typical prediction error (~3 t/ha) indicates the model captures general trends but struggles with:
   - Extreme weather conditions  
   - Sparse or incomplete historical data  
   - Rare crops with limited samples  

5. Cleaning temperature units (C/F inconsistencies) improved performance noticeably.

6. Removing unrealistic yields (>200 t/ha) stabilized training by eliminating outliers.

---

## 🚀 Improvements & Next Steps

### 1. **Deploy Streamlit App**
We will build an interactive dashboard that:

- Accepts user inputs (soil type, weather, irrigation, crop choice)
- Predicts **expected yield**
- Rates **crop sustainability** on a scoring system
- Visualizes:
  - Feature importances
  - Historical yield trends
  - Recommended vs. unsuitable crops

### 2. **Model Enhancements**

- Hyperparameter tuning (Optuna or GridSearchCV)
- Train a **classification model** for crop suitability alongside regression
- Use:
  - CatBoost (handles categorical features extremely well)
  - XGBoost/LightGBM (if missing values are imputed)

### 3. **Data Improvements**

- Add satellite NDVI/vegetation data  
- Include nutrient information (NPK levels)  
- Improve historical weather merging  
- Add more fields and crop types for better generalization

### 4. **Production Pipeline**

- Automate preprocessing  
- Implement model versioning with MLflow  
- Continuous retraining pipeline triggered by new data  

---

## 🧠 Conclusions

This project successfully implements a **modern machine learning system** capable of predicting agricultural crop yields and supporting sustainability-focused decision-making.

Key outcomes:

- The **HistGradientBoostingRegressor** provided strong baseline performance with minimal preprocessing requirements.
- Cleaning and unifying datasets significantly improved model stability.
- The project establishes an excellent foundation for deploying a **real-world decision-support tool** using Streamlit.
- With additional data and improved tuning, the system can evolve into a fully fledged **AI-driven crop recommendation and yield optimization platform**.

The work done so far demonstrates that machine learning can meaningfully support agricultural planning, improve sustainability outcomes, and provide accessible decision tools for farmers and agronomists.


## 🙌 Acknowledgements
Thanks to the dataset providers, open-source libraries, and agricultural ML research community for enabling reproducible work.
