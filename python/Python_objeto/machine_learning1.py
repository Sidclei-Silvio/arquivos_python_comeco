# Importando bibliotecas
pip -q install plotly --upgrade
pip -q install yellowbrick
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
base_credit = pd.read_csv('/content/sample_data/credit_data.csv')

base_credit[base_credit['loan']>=2000]
