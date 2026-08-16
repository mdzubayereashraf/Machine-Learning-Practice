import pandas as pd
from sklearn.linear_model import LogisticRegression
df = pd.DataFrame(
    {
        "Hours" : [2, 3, 4, 5, 6],
        "Result" : [0,0,1,1,1]
    }
)
model = LogisticRegression()
model.fit(df[["Hours"]],df["Result"])
while True :
    hour = float(input("Enter your study hours: "))
    input_data = pd.DataFrame([[hour]], columns=["Hours"])
    predict_result = model.predict(input_data)[0]

    if predict_result == 1:
       print("You're likely to Pass")
    else:
        print("You're likely to Fail")