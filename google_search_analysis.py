# -*- coding: utf-8 -*-
"""Google Search Analysis.ipynb

Automatically generated by Colaboratory.

"""

!pip install pytrends

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

trends.build_payload(kw_list = ["Machine Learning"])  
df = trends.interest_by_region()    #countries
df = df.sort_values(by = "Machine Learning",ascending = False)
df = df.head(10)  #top 10 countries
print(df)

df.reset_index().plot(x="geoName",y="Machine Learning",figsize = (12,10),kind = "bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US',tz=360)
data.build_payload(kw_list = ["Machine Learning"])
data = data.interest_over_time()
fig,ax = plt.subplots(figsize = (12,10))
data['Machine Learning'].plot()
plt.title('Total Google Searches for Machine Learning', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Count')
plt.style.use('fivethirtyeight')
plt.show()

