import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pandas.plotting import autocorrelation_plot
from io import StringIO

data = StringIO("""
Month,Passengers
1949-01,112
1949-02,118
1949-03,132
1949-04,129
1949-05,121
1949-06,135
1949-07,148
1949-08,148
1949-09,136
1949-10,119
1949-11,104
1949-12,118
1950-01,115
1950-02,126
1950-03,141
1950-04,135
1950-05,125
1950-06,149
1950-07,170
1950-08,170
1950-09,158
1950-10,133
1950-11,114
1950-12,140
""")

df = pd.read_csv(data)
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)

print(df.describe())
df.plot(title='Original Time Series', figsize=(10, 4))
plt.grid()
plt.show()

decomposition = seasonal_decompose(df, model='additive', period=12)
decomposition.plot()
plt.tight_layout()
plt.show()

autocorrelation_plot(df)
plt.title("Autocorrelation Plot")
plt.show()

rolling_mean = df.rolling(window=12).mean()
rolling_std = df.rolling(window=12).std()

plt.figure(figsize=(10, 4))
plt.plot(df, label='Original')
plt.plot(rolling_mean, label='Rolling Mean', color='red')
plt.plot(rolling_std, label='Rolling Std Dev', color='black')
plt.legend()
plt.title("Rolling Mean & Standard Deviation")
plt.grid()
plt.show()

