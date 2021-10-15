import pandas
import matplotlib.pyplot as plt
import seaborn as sns

def draw_lineplots(df, cols, target):
    for col in cols:
        plt.figure(figsize=(16,4))
        tmp =  df.groupby(col)[target].mean()
        sns.lineplot(data=tmp).set(title=f'{col} vs {target}')
    plt.show()

