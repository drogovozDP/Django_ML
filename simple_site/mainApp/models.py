from django.db import models
import pickle

with open("C:/Users/user/anaconda notebooks/data/models/lin_reg.pkl", 'rb') as file:
    lin_reg = pickle.load(file)

def model(x):
    query = [[x['day']] + [0 for i in range(24)]]
    query[0][x['hour'] + 1] = 1
    return round(lin_reg.predict(query)[0], 2)