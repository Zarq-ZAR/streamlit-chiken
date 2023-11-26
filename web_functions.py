# import modul yang akan digunakan
import numpy as np
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
import streamlit as st 
import os

#fungsi untuk load data
@st.cache_data()
def load_data():

    # load dataset 1
    df = pd.read_csv('broiler_bersih.csv')
    x = df[["Populasi 2017","Populasi 2018","Produksi 2017","Produksi 2018"]]
    y = df[['Skala Produksi']]

    # Load dataset 2
    # file_path = os.path.abspath('Poultry-Pedaging.csv')
    # df2 = pd.read_csv(file_path)
    # x2 = df2[["Populasi 2017","Populasi 2018","Produksi 2017","Produksi 2018"]]
    # y2 = df2[['Skala Produksi']]

    return df, x, y

#fungsi untuk model decision tree
@st.cache_resource()
def train_model(x, y):
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )

    model.fit(x, y)

    score = model.score(x, y)

    return model, score

#fungsi untuk predict
def predict(x, y, features):
    model, score = train_model(x, y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score 

