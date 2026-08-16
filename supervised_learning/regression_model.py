import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.DataFrame(
    {
        "Hours" : [2, 3, 4, 5, 6],
        "Marks" : [30,45,55,65,75]
    }
)
model = LinearRegression()
model.fit(df[["Hours"]],df["Marks"])
while True :
    hour = float(input("Enter your study hours:"))

    predict_marks = model.predict([[hour]])
    print(predict_marks)