# 🫀 Heart Disease Prediction System

This project presents a Machine Learning pipeline that predicts the likelihood of heart disease in a patient based on various medical attributes. The system uses well-established classification models and preprocessing techniques, aiming to assist in early detection and preventive healthcare.

## 📁 Dataset

- **Source**: [Kaggle - Heart Disease Dataset](https://www.kaggle.com/)
- **Samples**: 918 entries with 12 features
- **Target Variable**: `HeartDisease` (1 = disease present, 0 = absent)

## 🔍 Exploratory Data Analysis (EDA)

- Verified null and duplicate values (none found)
- Separated categorical and numerical features
- Visualized distributions using histograms and boxplots
- Used correlation heatmaps to identify strong predictors
- Categorical feature relationships explored via bar plots

### Key Insights:
- `Oldpeak`, `ST_Slope`, `ChestPainType`, and `ExerciseAngina` showed strong correlation with heart disease.
- Data was well-balanced: ~55% positive and ~45% negative cases.
- Detected some outliers in `Cholesterol` and `RestingBP`.

## 🧹 Data Preprocessing

- **Numerical Columns**: Imputed using median strategy and scaled using `StandardScaler`
- **Categorical Columns**: Imputed using most frequent strategy and encoded via `OneHotEncoder`
- Combined pipelines using `ColumnTransformer`
- Final shape after preprocessing: 734 rows × 20 features

## 🤖 Models Implemented

| Model                 | Train Accuracy | Cross-Validation Accuracy |
|----------------------|----------------|----------------------------|
| Logistic Regression  | 85.96%         | 84.85%                     |
| Random Forest        | 100% (overfit) | 85.55%                     |

✅ **Random Forest Classifier** outperformed Logistic Regression in cross-validation and was chosen as the base model for tuning.

## 🔧 Hyperparameter Tuning

- Used `RandomizedSearchCV` and `GridSearchCV` for both models
- Final model selected: **Random Forest Classifier with tuned hyperparameters**

### 📊 Feature Importance

Top 5 influential features:
1. `ST_Slope_Up`
2. `ST_Slope_Flat`
3. `ChestPainType_ASY`
4. `Oldpeak`
5. `MaxHR`

These features had the highest contribution to the model's prediction decisions.

## ✅ Final Evaluation on Test Set

- Final model evaluated on untouched test set (20% of data)
- **Test Accuracy**: **89.67%**
- Demonstrated good generalization and no overfitting

## 💾 Model Saving and Deployment

- Final model saved using `joblib` as `final_model.pkl`
- Ready for deployment using:
  - Web framework: `Streamlit`, `Flask`, or `FastAPI`
  - Hosting platforms: `Render`, `Streamlit Cloud`, or `Heroku`

## 🛠️ Technologies Used

- Python 3
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-Learn
- Jupyter Notebook / Google Colab

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/heart-disease-prediction.git
   
2. Upload the dataset heart.csv to the working directory

3. Run the notebook in Google Colab or Jupyter
 
4. To use the saved model:

import joblib
model = joblib.load('final_model.pkl')


📌 Future Enhancements

Add Streamlit frontend for interactive predictions

Integrate SHAP or LIME for model explainability

Incorporate more real-world features (e.g., lifestyle, genetic history)


📜 License
This project is for educational purposes only and not intended for medical use without professional verification.


🙏 Acknowledgements
Thanks to:

Kaggle for the dataset

The Scikit-Learn team for the robust ML tools

Google Colab for providing a free computation platform
