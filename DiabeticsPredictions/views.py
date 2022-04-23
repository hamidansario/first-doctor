from urllib import request

from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import wikipedia
import webbrowser
import pickle
import nltk
from newspaper import Article
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def Home(request):
    return render(request, 'Home.html')


def Diabetics(request):
    return render(request, 'Diabetics.html')


def DiaPredict(request):
    return render(request, 'DiaPredict.html')


def Depression(request):
    return render(request, 'Depression.html')


def DepPredict(request):
    return render(request, 'DepPredict.html')


def Heart(request):
    return render(request, 'Heart.html')


def HeaPrediction(request):
    return render(request, 'HeaPrediction.html')


def result(request):
    diabetes_data = pd.read_csv(r'C:\Users\hamid\Downloads\diabetes.csv')

    x = diabetes_data.drop("Outcome", axis=1)
    y = diabetes_data["Outcome"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"

    return render(request, 'DiaPredict.html', {"result2": result1})


def outcome(request):
    heart_data = pd.read_csv(r'C:\Users\hamid\Downloads\heart.csv')

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    value1 = float(request.GET['x1'])
    value2 = float(request.GET['x2'])
    value3 = float(request.GET['x3'])
    value4 = float(request.GET['x4'])
    value5 = float(request.GET['x5'])
    value6 = float(request.GET['x6'])
    value7 = float(request.GET['x7'])
    value8 = float(request.GET['x8'])
    value9 = float(request.GET['x9'])
    value10 = float(request.GET['x10'])
    value11 = float(request.GET['x11'])
    value12 = float(request.GET['x12'])
    value13 = float(request.GET['x13'])

    prediction = model.predict(
        [[value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13]])

    outcome1 = ""
    if prediction == [1]:
        outcome1 = "You Have Heart Diseases"
    else:
        outcome1 = "You Don't Have Heart Diseases"

    return render(request, 'HeaPrediction.html', {"outcome2": outcome1})


def chatbot(request):
    return render(request, 'chatbot.html')


def botsearch(request):
    question = request.GET.get('question')

    try:
        ans = wikipedia.summary(question, sentences=10)
        return render(request, 'chatbot.html', {'ans': ans, 'question': question})


    except Exception:
        ans = "FOUND NOTHING"
        return render(request, 'chatbot.html', {'ans': ans, 'question': question})
