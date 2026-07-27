🎬 Movie Rating Prediction with Python

📌 Overview

Movie Rating Prediction with Python is a machine learning project that predicts movie ratings based on features such as genre, director, actors, duration, release year, and user votes. The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and prediction.

Using the IMDb Movies India dataset, this project applies regression techniques to estimate movie ratings and identify the factors that influence audience and critic ratings.

🎯 Objectives

* Analyze historical movie data.
* Perform data cleaning and preprocessing.
* Explore the dataset using visualizations.
* Build a regression model to predict movie ratings.
* Evaluate model performance using standard regression metrics.
* Predict ratings for new movie data.

 📂 Dataset

The dataset contains information about Indian movies, including:

* Movie Name
* Release Year
* Duration
* Genre
* Director
* Actors
* Number of Votes
* IMDb Rating (Target Variable)

🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Missing Value Analysis
* Rating Distribution
* Genre Distribution
* Correlation Heatmap
* Data Cleaning and Feature Exploration

 🤖 Machine Learning

This project uses **Random Forest Regressor** to predict movie ratings.

 Workflow

* Import Dataset
* Data Cleaning
* Handle Missing Values
* Feature Engineering
* One-Hot Encoding
* Train-Test Split
* Model Training
* Model Evaluation
* Rating Prediction

 📈 Evaluation Metrics

The model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics help measure the accuracy and performance of the regression model.

🚀 Project Structure

```text
Movie-Rating-Prediction/
│
├── IMDb Movies India.csv
├── main.py
├── movie_rating_model.pkl
├── README.md
└── requirements.txt
```

▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Movie-Rating-Prediction.git
```

Move to the project directory:

```bash
cd Movie-Rating-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

📌 Features

* Data Cleaning and Preprocessing
* Missing Value Handling
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Categorical Feature Encoding
* Random Forest Regression Model
* Model Evaluation
* Movie Rating Prediction
* Save Trained Model using Joblib

📚 Learning Outcomes

This project helped in understanding:

* Data Preprocessing Techniques
* Exploratory Data Analysis
* Regression Algorithms
* Feature Engineering
* Machine Learning Model Evaluation
* Python for Data Science
* Building End-to-End Machine Learning Pipelines

🔮 Future Improvements

* Compare multiple regression models such as Linear Regression, Gradient Boosting, and XGBoost.
* Perform Hyperparameter Tuning.
* Deploy the model using Streamlit or Flask.
* Build an interactive web application for real-time movie rating prediction.

👩‍💻 Author

**Sangeeta Sharma**

B.Tech – Artificial Intelligence & Data Science

Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer

-⭐ Acknowledgements

* IMDb Movies India Dataset
* Scikit-learn Documentation
* Pandas Documentation
* Matplotlib & Seaborn Libraries

---

If you found this project useful, consider giving the repository a ⭐ Star.
