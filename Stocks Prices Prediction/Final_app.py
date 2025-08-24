import joblib
load=joblib.load('linear_regression_model.joblib')
t=int(input("Enter time in formate hours.min: "))
a=load.predict(t)
print(a)
