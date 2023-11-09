# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:25:19 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_frame1 = pd.read_csv('New data_2.csv')
print(data_frame1)

"""Line plot"""
"""here I just extracted data from file of every country"""
AFG = data_frame1[data_frame1["Country"] == "Afghanistan"]
CHI = data_frame1[data_frame1["Country"] == "China"]
BRA = data_frame1[data_frame1["Country"] == "Brazil"]
COL = data_frame1[data_frame1["Country"] == "Colombia"]
USA = data_frame1[data_frame1["Country"] == "United State America"]
FRA = data_frame1[data_frame1["Country"] == "France"]             



# """I ploted every country dath with respect to year"""

fig, ax = plt.subplots(figsize=(12, 8))
plt.plot(AFG['Period'].astype("str"), AFG['New_deaths'],marker = 'o',
         label = "Afganistan")
plt.plot(CHI['Period'].astype("str"), CHI['New_deaths'],marker = 'o',
         label = "China")
plt.plot(FRA['Period'].astype("str"), FRA['New_deaths'],marker = 'o',
         label = "France")
plt.plot(USA['Period'].astype("str"), USA['New_deaths'],marker = 'o',
         label = "USA")
plt.plot(COL['Period'].astype("str"), COL['New_deaths'],marker = 'o',
         label = "Colombia")
ax.legend()
ax.set(xlabel="Years", ylabel="Death")
plt.margins(x=0)

ax.grid(True)

plt.show()
plt.savefig("LINEPLOT.png") 
   

"creating pi chart for cases"

d2020 = data_frame1[data_frame1["Period"] == 2020]
#print(d2020)
arr2020 = np.array(d2020["Cumulative_deaths"])
#print(arr2020)
plt.figure(figsize=(12,10))
plt.pie(arr2020, labels=['Afghanistan', 'Brazil', 'China', 'Colombia', 
                         'France', 'USA'])

plt.show()
plt.savefig("pie-Chart.png")

"Creating Bar graph for "
plt.figure(figsize=(12,8))
plt.subplot(3,2,1)
plt.hist(AFG["New_deaths"], label="Afghanistan", density = True)
plt.legend()
plt.subplot(3,2,2)
plt.hist(BRA["New_deaths"], label="Brazil",density = True)
plt.legend()
plt.subplot(3,2,3)
plt.hist(CHI["New_deaths"], label="China", density = True)
plt.legend()
plt.subplot(3,2,4)
plt.hist(COL["New_deaths"], label="Colombia", density = True)
plt.legend()
plt.subplot(3,2,5)
plt.hist(FRA["New_deaths"], label="France",density = True)
plt.legend()
plt.subplot(3,2,6)
plt.hist(USA["New_deaths"], label="USA",density = True)
plt.legend()
plt.show()
plt.savefig("Histogram.png")


