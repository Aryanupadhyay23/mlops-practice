import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/sklearn/datasets/data/iris.csv"
df = pd.read_csv(url)

df.to_csv("data/raw/iris.csv", index=False)
