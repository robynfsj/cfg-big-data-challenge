import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# Import the data
df = pd.read_excel('Data\data_to_model_adj.xls', '2.2')

# Remove rows from year 2020
df.drop(305, axis=0,inplace=True)
df.drop(304, axis=0,inplace=True)
df.drop(303, axis=0,inplace=True)
df.drop(302, axis=0,inplace=True)
df.drop(301, axis=0,inplace=True)
df.drop(300, axis=0,inplace=True)

# Create column that combines year and month
df['year_month'] = df['year'].astype(str) + '-' + df['month'].astype(str)

# Convert to datetime
df['year_month'] = pd.to_datetime(df['year_month'])

# Set date column as index
df.set_index('year_month',inplace=True)

# Remove no longer required columns
df = df.drop(columns=['year', 'month'])

# Optional - print the descriptive statistics
#print(df.describe())

# Optional - view the historic data plot
#plt.plot(df)
#plt.show()

### Testing For Stationarity
from statsmodels.tsa.stattools import adfuller

test_result=adfuller(df['electricity_sold_total'])

#Ho: It is non stationary
#H1: It is stationary

def adfuller_test(electricity_sold_total):
    result=adfuller(electricity_sold_total)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")


adfuller_test(df['electricity_sold_total'])

### Differencing

print(df['electricity_sold_total'].head())

df['electricity_sold_total First Difference'] = df['electricity_sold_total'] - df['electricity_sold_total'].shift(1)

print(df['electricity_sold_total'].shift(1))

df['Seasonal First Difference']=df['electricity_sold_total']-df['electricity_sold_total'].shift(12)

print(df.head(14))

## Again test Dickey Fuller test
adfuller_test(df['Seasonal First Difference'].dropna())

#plt.plot(df['Seasonal First Difference'])
#plt.show()

# Correlations
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df['electricity_sold_total'])
#plt.show()

from statsmodels.graphics.tsaplots import plot_acf,plot_pacf

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = plot_acf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax1)

#plt.show()

ax2 = fig.add_subplot(212)
fig = plot_pacf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax2)

#plt.show()

# For non-seasonal data
#p=1, d=1, q=0 or 1
from statsmodels.tsa.arima_model import ARIMA

model=ARIMA(df['electricity_sold_total'],order=(1,1,1))
model_fit=model.fit()

model_fit.summary()

df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
df[['electricity_sold_total','forecast']].plot(figsize=(12,8))

#plt.show()

import statsmodels.api as sm

model=sm.tsa.statespace.SARIMAX(df['electricity_sold_total'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
results=model.fit()

df['forecast']=results.predict(start=90,end=103,dynamic=True)
df[['electricity_sold_total','forecast']].plot(figsize=(12,8))

#plt.show()

from pandas.tseries.offsets import DateOffset
future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]

future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)

#print(future_datest_df.tail())

future_df=pd.concat([df,future_datest_df])

# Set the start and end points of the prediction
future_df['forecast'] = results.predict(start = 295, end = 700, dynamic= True)
future_df[['electricity_sold_total', 'forecast']].plot(figsize=(12, 8))

# Plot the forecast
plt.show()
plt.savefig('electricity_sold_total.png')