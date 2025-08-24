import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,mean_squared_error 
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import joblib
df=pd.read_csv("a1.csv")
print(df.head())

set_train,set_test=train_test_split(df,test_size=0.2,random_state=42)
train=set_train["0"].copy().values.reshape(-1,1)
train_label=set_train["2"].copy().values.reshape(-1,1)
#my_pipline=Pipeline([('std_scaler',StandardScaler()),])

#train_1=my_pipline.fit_transform(train)
model=LinearRegression()
model.fit(train,train_label)
model_p=model.predict(train)
mse=mean_squared_error(train_label,model_p)
rmse=np.sqrt(mse)
print(rmse)
score=cross_val_score(model,train,train_label,scoring="neg_mean_squared_error",cv=10)
rmse=np.sqrt(-score)
print(rmse)
test=set_test["0"].copy().values.reshape(-1,1)   

test_label=set_test["2"].copy().values.reshape(-1,1)
print(test[1])
#test_1=my_pipline.transform(test)

model_p=model.predict(test)
mse=mean_squared_error(test_label,model_p)
rmse=np.sqrt(mse)
print(rmse)
print(model.predict([[9.10]]))
model_filename='linear_regression_model.joblib'
joblib.dump(model, model_filename)
