#1. Import Libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#2. Load Dataset
df = pd.read_csv("IMDb Movies India.csv", encoding="latin1")

print(df.head())
print(df.info())
#3. Data Cleaning
#Year
df["Year"] = df["Year"].str.extract(r'(\d{4})')
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
#Duration
df["Duration"] = df["Duration"].str.replace(" min","",regex=False)
df["Duration"] = pd.to_numeric(df["Duration"],errors="coerce")
#Votes
df["Votes"] = df["Votes"].astype(str).str.replace(",","")
df["Votes"] = pd.to_numeric(df["Votes"],errors="coerce")
#Rating
df["Rating"] = pd.to_numeric(df["Rating"],errors="coerce")
#4. Remove Missing Values in Target
df = df.dropna(subset=["Rating"])
#5. Fill Missing Values
df["Genre"] = df["Genre"].fillna("Unknown")
df["Director"] = df["Director"].fillna("Unknown")

df["Actor 1"] = df["Actor 1"].fillna("Unknown")
df["Actor 2"] = df["Actor 2"].fillna("Unknown")
df["Actor 3"] = df["Actor 3"].fillna("Unknown")
#6. Exploratory Data Analysis
#Dataset Shape
print(df.shape)
#Missing Values
print(df.isnull().sum())
#Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Rating"],bins=20,kde=True)
plt.title("Distribution of Movie Ratings")
plt.show()
#Top Genres
plt.figure(figsize=(10,6))
df["Genre"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres")
plt.show()
#Correlation
plt.figure(figsize=(6,4))

numeric = df[["Year","Duration","Votes","Rating"]]

sns.heatmap(numeric.corr(),annot=True,cmap="Blues")

plt.show()
#7. Select Features
features = [
    "Genre",
    "Director",
    "Actor 1",
    "Actor 2",
    "Actor 3",
    "Year",
    "Duration",
    "Votes"
]

X = df[features]
y = df["Rating"]
#8. Numerical & Categorical Columns
categorical = [
    "Genre",
    "Director",
    "Actor 1",
    "Actor 2",
    "Actor 3"
]

numerical = [
    "Year",
    "Duration",
    "Votes"
]
#9. Preprocessing
preprocessor = ColumnTransformer(

    transformers=[

        (
            "num",

            SimpleImputer(strategy="median"),

            numerical
        ),

        (
            "cat",

            Pipeline([

                ("imputer",SimpleImputer(strategy="most_frequent")),

                ("encoder",OneHotEncoder(handle_unknown="ignore"))

            ]),

            categorical
        )
    ]
)
#10. Train-Test Split
X_train,X_test,y_train,y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42
)
#11. Random Forest Model
model = Pipeline([

    ("preprocessor",preprocessor),

    ("model",RandomForestRegressor(

        n_estimators=200,

        random_state=42
    ))
])
#12. Train Model
model.fit(X_train,y_train)
#13. Prediction
prediction = model.predict(X_test)
#14. Evaluation
mae = mean_absolute_error(y_test,prediction)

rmse = np.sqrt(mean_squared_error(y_test,prediction))

r2 = r2_score(y_test,prediction)

print("MAE :",mae)

print("RMSE :",rmse)

print("R2 Score :",r2)
#15. Predict New Movie
new_movie = pd.DataFrame({

    "Genre":["Drama"],

    "Director":["Sanjay Leela Bhansali"],

    "Actor 1":["Shah Rukh Khan"],

    "Actor 2":["Kajol"],

    "Actor 3":["Amrish Puri"],

    "Year":[2025],

    "Duration":[150],

    "Votes":[250000]

})

rating = model.predict(new_movie)

print("Predicted Rating :",rating[0])
#Bonus (Model Save)
import joblib

joblib.dump(model,"movie_rating_model.pkl")