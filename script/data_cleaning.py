import pandas as pd
import numpy as ny
from IPython.display import display



df = pd.read_csv('~/Documents/Capstone/Data-Collisions.csv')

display(df["WEATHER"].value_counts())
