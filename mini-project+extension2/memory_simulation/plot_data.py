import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def create_myPlot(data_path):
    data = pd.read_csv(data_path)

    sns.lineplot(data = data, x="list_length", y="acc", hue="group")
    plt.savefig(f"./{datetime.datetime.now().strftime('%Y%m%d')}_forgetting-curves.png")
    plt.show()
