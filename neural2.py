#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 10:23:18 2022

@author: yabsera
"""
tr=pd.read_csv('train.csv').replace({"male":1,"female":2})
y=tr['Survived'].loc[0:400]
features=['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare']
X=tr[features].fillna(0).astype('int64').loc[0:400]
result=[0,0,0,0,0]
while i<5:
  result[i]=y[i]
  i+=1
modeal=DecisionTreeRegressor(random_state=1)
modeal.fit(X,y)
prediction=modeal.predict(X)
i=0
truth={"TRUE":0,"False":0}
while i<len(y):
  if(y[i]==prediction[i]):
    truth["TRUE"]+=1
  else:
    truth["False"]+=1
  i+=1
print(truth)
print(y[0:5])
print(prediction[0:5])