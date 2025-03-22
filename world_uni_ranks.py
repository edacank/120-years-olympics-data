import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings

#plotly
#from plotly.offline import init_notebook_mode,iplot, matplotlib

#init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.io as pio
import plotly.figure_factory as ff
warnings.filterwarnings("ignore")
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[10, 20, 30], mode="lines+markers")])
pio.show(fig)


timesData = pd.read_csv("../input/world-university-rankings/timesData.csv")
timesData.info()