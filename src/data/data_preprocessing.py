import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/titanic.csv")
df_dropped = df.drop(columns=(["Ticket","Embarked"]),axis=1)

df_dropped.to_csv("data/processed/titanic_preprocessed.csv")

