import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel(r"Sales Dataset.xlsx")
df.head() #see dataset sample

df.info()

df.describe()