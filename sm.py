import pandas as pd
from flask import render_template, redirect
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#fancy
sns.set(style="white" color_codes=True)
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import json, ast
import matplotlib.colors as colors
import matplotlib.cm as cm

#columns =["HostStarMassSlrMass", "HostStarMetallicity", "HostStarTempK","HostStarRadiusSlrRad", "Eccentricity", "DiscoveryYear", "DiscoveryMethod", "PeriodDays", "PlanetaryMass", "RadiusJpt", "PlanetIdentifier", "SemiMajorAxisAU"]
columnsDate = ["Year", "Month", "Day"]
Columns= ["Date", "Extent", "hemisphere"]
norm= color.Normalize(vmin= color.min(), vmax= color.max())
cmap= cm.coolwarm

def parseAndWrite(cl, db, droppable):
    #Let's parse the data
    jo=pd.read_csv(filename)
    #Preprocessing
    jo.dropna(axis=1, how='any')
    #drop any column with missing values
    jo['Date']=pd.to_datetime(jo[columnsDate])
    jo.index=jo['Date'].vaues
    filterJO = jo.drop(droppable, axis=1, inplace=True)   #remove unnecessary columns
    filterJO = json.loads(filterJO.to_json(orient = 'records'))
    data = ast.literal_eval(json.dumps(filterJO))
                          
    db.insert(data)
    print("\nInserted\n")
                          
    return render_template("index.html")
                          

def suisight(db, filename):
    plt.style.use('ggplot')
    data=filename
    data.dropna(axis=1, how='any')
    data['State', 'Year', 'Type','Type_Code', 'Gender','Total'].dropna(axis=1, inplace=True)
    eduData=data[data['Type_Code']=='Education_Status']
    SocData=data[data['Type_Code']=='Social_Status']
    genderCnt=eduData.groupby(['Gender']['Total']).sum()
    
    #plotting
    plsowrk= lambda x: for x in range(0,4):
                            fig,(x)=plt.subplots(4,1,figsize=20,40)
                            for j in range(0,4):
                                sns.countplot(x=data[j]), data=data, ax=x)
    
    return plsowrk




                          



