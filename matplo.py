import matplotlib.pyplot as plt
import pandas as pd
#smartplotlib inline

sales = pd.read_csv(r'\Users\encam\vstoolbox\Rmotr\sales_data.csv', parse_dates=['Date'])

sales.head()

sales.info()

sales.shape()
