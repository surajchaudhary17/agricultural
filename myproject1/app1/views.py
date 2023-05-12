from django.shortcuts import render
# from . import views
# from django.http import HttpRequest
from django.http import HttpResponse
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import csv
from threading import Thread

import pandas as pd

#for interactivity
from ipywidgets import interact
from django.shortcuts import render
from .forms import CropForm

# Create your views here.
#1. just return a message 
# def welcome(request):
#     return HttpResponse("Here you're")
# #2.take message and display  that message from html page    
# def holdHtmlMsg(request):
#     return render(request, 'index.html')
# def your(request):
#     return render(request, 'practice6.html')
# def showhum(request):
#     return render(request, 'wegot.html')
# def welcome(request):
#     return HttpResponse("<h1>Hello welcome vihaan></h1>")


def home(request):
    return render(request, 'home.html')


def result(request):
    model=joblib.load('model.joblib')
    list = []
    list.append(float(request.GET['N']))
    list.append(float(request.GET['P']))
    list.append(float(request.GET['K']))
    list.append(float(request.GET['TEMP']))
    list.append(float(request.GET['HUMIDITY']))
    list.append(float(request.GET['PH']))
    list.append(float(request.GET['RAINFALL']))
    # print(list)
    ans=model.predict((np.array([list])))[0]
    return render(request, 'result.html',{'ans':ans})


    #for graph
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')    
def graph1(request):
    
    # data = pd.read_csv('./../Notebooks/data.csv')
    # file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')
    # Check if the file exists
    if not os.path.exists(file_path):
        return HttpResponse('File not found')
    data = pd.read_csv(file_path)
    fig, ax = plt.subplots(figsize=(9, 7))
    fig.tight_layout(h_pad = 2)

    plt.subplot(2,4,1)
    sns.histplot(data['N'], color = 'red')
    plt.xlabel('Ratio of Nitrogen', fontsize=10)
    plt.grid()

    plt.subplot(2,4,2)
    sns.histplot(data['P'], color = 'lightblue')
    plt.xlabel('Ratio of Phosphorous', fontsize=10)
    plt.grid()

    plt.subplot(2,4,3)
    sns.histplot(data['K'], color = 'darkblue')
    plt.xlabel('Ratio of Potassium', fontsize=10)
    plt.grid()

    plt.subplot(2,4,4)
    sns.histplot(data['temperature'], color = 'black')
    plt.xlabel('Temperature', fontsize=10)
    plt.grid()

    plt.subplot(2,4,5)
    sns.histplot(data['rainfall'], color = 'grey')
    plt.xlabel('Rainfall', fontsize=10)
    plt.grid()

    plt.subplot(2,4,6)
    sns.histplot(data['humidity'], color = 'lightgreen')
    plt.xlabel('Humidity', fontsize=10)
    plt.grid()

    plt.subplot(2,4,7)
    sns.histplot(data['ph'], color = 'darkgreen')
    plt.xlabel('ph level', fontsize=10)
    plt.grid()
    fig.subplots_adjust(wspace=0.7)
    # Specify the full path to the image file
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static', 'my_graph.png')
    
    # Save the Matplotlib figure to the specified path
    fig.savefig(image_path,bbox_inches='tight')

    # Pass the full path to the image file to the HTML template
    return render(request, 'home.html', {'graph_path': '/static/my_graph.png'})


# def dropdown1(request):
#     file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')
    
#     # Check if the file exists
#     if not os.path.exists(file_path):
#         return HttpResponse('File not found')
#     data = pd.read_csv(file_path)

#     crops = list(data['label'].value_counts().index)
#     crop = request.GET.get('crop', crops[0])
#     x = data[data['label'] == crop]
#     summary_output = []

def summary(request):
    # file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return HttpResponse('File not found')
    data = pd.read_csv(file_path)

    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crops = form.cleaned_data['crops']
            x = data[data['label'] == crops]
            # print('vihaan')
            nitrogen_min = x['N'].min()
            nitrogen_avg = x['N'].mean()
            nitrogen_max = x['N'].max()
            phosphorous_min = x['P'].min()
            phosphorous_avg = x['P'].mean()
            phosphorous_max = x['P'].max()
            potassium_min = x['K'].min()
            potassium_avg = x['K'].mean()
            potassium_max = x['K'].max()
            temperature_min = x['temperature'].min()
            temperature_avg = x['temperature'].mean()
            temperature_max = x['temperature'].max()
            rainfall_min = x['rainfall'].min()
            rainfall_avg = x['rainfall'].mean()
            rainfall_max = x['rainfall'].max()
            humidity_min = x['humidity'].min()
            humidity_avg = x['humidity'].mean()
            humidity_max = x['humidity'].max()
            ph_min = x['ph'].min()
            ph_avg = x['ph'].mean()
            ph_max = x['ph'].max()
            
            return render(request, 'summary2.html', {'form': form, 'nitrogen_min': nitrogen_min, 'nitrogen_avg': nitrogen_avg, 'nitrogen_max': nitrogen_max, 'phosphorous_min': phosphorous_min, 'phosphorous_avg': phosphorous_avg, 'phosphorous_max': phosphorous_max, 'potassium_min': potassium_min, 'potassium_avg': potassium_avg, 'potassium_max': potassium_max, 'temperature_min': temperature_min, 'temperature_avg': temperature_avg, 'temperature_max': temperature_max, 'rainfall_min': rainfall_min, 'rainfall_avg': rainfall_avg, 'rainfall_max': rainfall_max, 'humidity_min': humidity_min, 'humidity_avg': humidity_avg, 'humidity_max': humidity_max, 'ph_min': ph_min, 'ph_avg': ph_avg, 'ph_max': ph_max})
    else:
        form = CropForm()
        return render(request, 'summary2.html', {'form': form})  



def summary3(request, crops=None):
    # file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')
    
    # Check if the file exists
    if not os.path.exists(file_path):
        return HttpResponse('File not found')
    data = pd.read_csv(file_path)
    if crops is None:
        crops = list(data['label'].value_counts().index)
    x=data[data['label'].isin(crops)]
    nitrogen_min = x['N'].min()
    nitrogen_avg = x['N'].mean()
    nitrogen_max = x['N'].max()
    phosphorous_min = x['P'].min()
    phosphorous_avg = x['P'].mean()
    phosphorous_max = x['P'].max()
    potassium_min = x['K'].min()
    potassium_avg = x['K'].mean()
    potassium_max = x['K'].max()
    temperature_min = x['temperature'].min()
    temperature_avg = x['temperature'].mean()
    temperature_max = x['temperature'].max()
    rainfall_min = x['rainfall'].min()
    rainfall_avg = x['rainfall'].mean()
    rainfall_max = x['rainfall'].max()
    humidity_min = x['humidity'].min()
    humidity_avg = x['humidity'].mean()
    humidity_max = x['humidity'].max()
    ph_min = x['ph'].min()
    ph_avg = x['ph'].mean()
    ph_max = x['ph'].max()
    context = {
        'nitrogen_min': nitrogen_min,
        'nitrogen_avg': nitrogen_avg,
        'nitrogen_max': nitrogen_max,
        'phosphorous_min': phosphorous_min,
        'phosphorous_avg': phosphorous_avg,
        'phosphorous_max': phosphorous_max,
        'potassium_min': potassium_min,
        'potassium_avg': potassium_avg,
        'potassium_max': potassium_max,
        'temperature_min': temperature_min,
        'temperature_avg': temperature_avg,
        'temperature_max': temperature_max,
        'rainfall_min': rainfall_min,
        'rainfall_avg': rainfall_avg,
        'rainfall_max': rainfall_max,
        'humidity_min': humidity_min,
        'humidity_avg': humidity_avg,
        'humidity_max': humidity_max,
        'ph_min': ph_min,
        'ph_avg': ph_avg,
        'ph_max': ph_max,
    }
    return render(request, 'summary3.html', context)



# Load the data
# file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Notebooks', 'data.csv')
    
    

# from .forms import ConditionForm
# from .import views

def nutrients(request):
    conditions = ['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']
    if not os.path.exists(file_path):
        return HttpResponse('File not found')
    data = pd.read_csv(file_path)
    condition = request.POST.get('condition', '')
    selected_condition = None  # initialize to None
    crops_greater = []
    crops_less = []
    if condition:  # check if condition is not empty
        selected_condition = condition
        crops_greater = data[data[selected_condition] > data[selected_condition].mean()]['label'].unique()
        crops_less = data[data[selected_condition] <= data[selected_condition].mean()]['label'].unique()
    context = {'conditions': conditions, 'selected_condition': selected_condition, 'crops_greater': crops_greater, 'crops_less': crops_less}
    return render(request, 'compare1.html', context)

    # else:
    #     form = ConditionForm()
    # context = {'conditions': conditions, 'form': form}
    # return render(request, 'compare1.html', context)




    # return render(request, 'summary4.html', {'crops': crops, 'crop_selected':crop ,'nitrogen_min': nitrogen_min, 'nitrogen_avg': nitrogen_avg, 'nitrogen_max': nitrogen_max, 'phosphorous_min': phosphorous_min, 'phosphorous_avg': phosphorous_avg, 'phosphorous_max': phosphorous_max, 'potassium_min': potassium_min, 'potassium_avg': potassium_avg, 'potassium_max': potassium_max, 'temperature_min': temperature_min, 'temperature_avg': temperature_avg, 'temperature_max': temperature_max, 'rainfall_min': rainfall_min, 'rainfall_avg': rainfall_avg, 'rainfall_max': rainfall_max, 'humidity_min': humidity_min, 'humidity_avg': humidity_avg, 'humidity_max': humidity_max, 'ph_min': ph_min, 'ph_avg': ph_avg, 'ph_max': ph_max})
def summary4(request):
    # Check if the file exists
    if not os.path.exists(file_path):
     return HttpResponse('File not found')
    data = pd.read_csv(file_path)
    # Get the selected crop from the form data
    crop = request.POST.get('crop', '')
    
    # If no crop is selected, show all crops
    # if crop =='':
    #     crops = list(data['label'].value_counts().index)
    if crop =='':
        crops = [''] + list(data['label'].value_counts().index)    
    else:
        crops = [crop]
       
    # Filter the data for the selected crop(s)
    x = data[data['label'].isin(crops)]
   
    
    
    # Calculate the statistics for each nutrient and environmental factor
    nitrogen_min = x['N'].min()
    nitrogen_avg = x['N'].mean()
    nitrogen_max = x['N'].max()
    
    phosphorous_min = x['P'].min()
    phosphorous_avg = x['P'].mean()
    phosphorous_max = x['P'].max()
    
    potassium_min = x['K'].min()
    potassium_avg = x['K'].mean()
    potassium_max = x['K'].max()
    
    temperature_min = x['temperature'].min()
    temperature_avg = x['temperature'].mean()
    temperature_max = x['temperature'].max()
    
    rainfall_min = x['rainfall'].min()
    rainfall_avg = x['rainfall'].mean()
    rainfall_max = x['rainfall'].max()
    
    humidity_min = x['humidity'].min()
    humidity_avg = x['humidity'].mean()
    humidity_max = x['humidity'].max()
    
    ph_min = x['ph'].min()
    ph_avg = x['ph'].mean()
    ph_max = x['ph'].max()

    context = {
        'crops': crops,
        'crop_selected':crop,
        'nitrogen_min': nitrogen_min,
        'nitrogen_avg': nitrogen_avg,
        'nitrogen_max': nitrogen_max,
        'phosphorous_min': phosphorous_min,
        'phosphorous_avg': phosphorous_avg,
        'phosphorous_max': phosphorous_max,
        'potassium_min': potassium_min,
        'potassium_avg': potassium_avg,
        'potassium_max': potassium_max,
        'temperature_min': temperature_min,
        'temperature_avg': temperature_avg,
        'temperature_max': temperature_max,
        'rainfall_min': rainfall_min,
        'rainfall_avg': rainfall_avg,
        'rainfall_max': rainfall_max,
        'humidity_min': humidity_min,
        'humidity_avg': humidity_avg,
        'humidity_max': humidity_max,
        'ph_min': ph_min,
        'ph_avg': ph_avg,
        'ph_max': ph_max,
    }
    
    # Pass the statistics to the template,both below are valid to pass the context,use any
    return render(request, 'summary4.html', context)
    # return render(request, 'summary4.html', {'crops': crops, 'crop_selected':crop ,'nitrogen_min': nitrogen_min, 'nitrogen_avg': nitrogen_avg, 'nitrogen_max': nitrogen_max, 'phosphorous_min': phosphorous_min, 'phosphorous_avg': phosphorous_avg, 'phosphorous_max': phosphorous_max, 'potassium_min': potassium_min, 'potassium_avg': potassium_avg, 'potassium_max': potassium_max, 'temperature_min': temperature_min, 'temperature_avg': temperature_avg, 'temperature_max': temperature_max, 'rainfall_min': rainfall_min, 'rainfall_avg': rainfall_avg, 'rainfall_max': rainfall_max, 'humidity_min': humidity_min, 'humidity_avg': humidity_avg, 'humidity_max': humidity_max, 'ph_min': ph_min, 'ph_avg': ph_avg, 'ph_max': ph_max})

from sklearn.cluster import KMeans        
def kmeanAlgo(request):
    if not os.path.exists(file_path):
     return HttpResponse('File not found')
    data = pd.read_csv(file_path)
    #removing the labels column
    x=data.drop(['label'],axis=1)

    #selecting all the values of the data
    x = x.values
    km = KMeans(n_clusters = 4, init = 'k-means++', max_iter = 500, n_init = 10, random_state = 0)
    y_means = km.fit_predict(x)

    #lets find out the results 
    a = data['label']
    y_means = pd.DataFrame(y_means)
    z = pd.concat([y_means,a], axis = 1)
    z = z.rename(columns = {0:'cluster'})
    #lets check the clusters of each crops
    # print("lets check the Results After Applying K means Clustering Analysis \n")
    # print("crops in first cluster:", z[z['cluster'] == 0]['label'].unique())
    # print("---------------------------------------------------------------")
    # print("crops in second cluster:", z[z['cluster'] == 2]['label'].unique())
    # print("---------------------------------------------------------------")
    # print("crops in third cluster:", z[z['cluster'] == 1]['label'].unique())
    # print("---------------------------------------------------------------")
    # print("crops in fourth cluster:", z[z['cluster'] == 3]['label'].unique())
    # print("---------------------------------------------------------------")

    cluster_results = {}
    for i in range(4):
        crops = z[z['cluster'] == i]['label'].unique()
        cluster_results[f'Cluster {i+1}'] = crops
    # print(cluster_results)
    context = {
        'cluster_results': cluster_results
    }
    
    # return HttpResponse('Mission successful')
    return render(request, 'kmeanalgo2.html', context)




  
