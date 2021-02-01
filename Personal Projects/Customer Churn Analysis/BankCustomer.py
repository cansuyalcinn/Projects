# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:31:23 2019

@author: cansu yalçın
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Veri Yukleme
veriler = pd.read_csv('BankCustomerChurn.csv')
print(veriler)

Geography=veriler.iloc[:,4:5].values
Gender=veriler.iloc[:,5:6].values
ilkveriler=veriler.iloc[:,3:4].values
sonveriler=veriler.iloc[:,6:13].values
existed=veriler.iloc[:,-1].values

#veri ön işleme
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
Geography[:,0]=le.fit_transform(Geography[:,0])
print(Geography)
  
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features="all") 
Geography=ohe.fit_transform(Geography).toarray()
Gender=ohe.fit_transform(Gender).toarray()
print(Geography)
print(Gender)

#dataframe olusturma
sonucgeo=pd.DataFrame(data=Geography, index=range(10000), columns=["France","Germany","Spain"])
print(sonucgeo)

sonucgen=pd.DataFrame(data=Gender, index=range(10000), columns=["Female","Male"])
print(sonucgen)

sonucilkveriler=pd.DataFrame(data=ilkveriler, index=range(10000), columns=["CreditScore"])
print(sonucilkveriler)

sonucsonveriler=pd.DataFrame(data=sonveriler, index=range(10000), columns=["Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary"])
print(sonucsonveriler)

sonucexisted=pd.DataFrame(data=existed, index=range(10000), columns=["Existed"])
print(sonucexisted)

birlestirme=pd.concat([sonucilkveriler,sonucgeo,sonucgen,sonucsonveriler],axis=1)
print(birlestirme)

#modelin ayrılması
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(birlestirme,sonucexisted,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)

from sklearn.metrics import confusion_matrix

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=10, criterion = 'entropy')
rfc.fit(X_train,y_train)

#tahmin yapilmasi
y_pred = rfc.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
print('RFC')
print(cm)
from sklearn.metrics import classification_report
print('Report' , classification_report(y_test,y_pred))

#k-fold cross validation:
from sklearn.model_selection import cross_val_score
basari=cross_val_score(estimator=rfc,X=X_train,y=y_train,cv=4)
print(basari.mean()) #0.8489557046845906
print(basari.std()) #0.0024625168985655784 


'''
RFC
[[2499  118]
 [ 377  306]] ----gini 2805
RFC
[[2506  111]
 [ 380  303]] ----entropy 2809
'''
