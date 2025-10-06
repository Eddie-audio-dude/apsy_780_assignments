import argparse
from .models import MemoryModel
import numpy as np
import pandas as pd
import datetime

def simulate_group(num_participants, list_length, num_trials):
    print(list_length)
    data = []

    for participant in range(num_participants):
        someones_memory=MemoryModel()
        if np.random.random() < 0.5: 
            condition = "simple"
        else:
            condition = "interference"
        
        for length in list_length:
            for t in range(num_trials):
                acc = someones_memory.simulate_trial(list_length=length, condition=condition)
                data.append({"ID":participant+1, "trial":t + 1, "group":condition, "acc": acc, "list_length": length})

    df = pd.DataFrame(data)
        
    df.to_csv(f"./{datetime.datetime.now().strftime('%Y%m%d')}_list-length-effects.csv")
    df.to_csv("./letter_memory_in-process.csv")
    
    return df

