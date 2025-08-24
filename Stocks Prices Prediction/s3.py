import joblib
load=joblib.load('linear_regression_model.joblib')
a=load.predict([[9.10],[15.10]])
print(a)
