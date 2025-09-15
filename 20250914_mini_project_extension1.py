# Simulate Stroop task and RTs
# Here I simulate across multiple participants and investigate within-subject var.
# Group-level effects are also investigated via a boxplot.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import datetime

# Here I simulate each stroop trials. I used the gamma distrubution because that's been a fav for modeling time related data.
def generate_rts(n_trials): 
    condition = ['congruent', 'incongruent']
    trial_decider = np.random.choice(a = condition, size = n_trials, replace = True, p = [0.5, 0.5])

    all_rts = []

    for trial in trial_decider:
        if trial == 'congruent':
            trial_rt = np.random.gamma(40, 10, 1).astype(int)[0]
            condition = "incongruent"
        else:
            trial_rt = np.random.gamma(55, 10, 1).astype(int)[0]
            condition = "incongruent"

        all_rts.append(trial_rt)

    results = {"trial":np.arange(1,n_trials+1),
               "condition": trial_decider,
               "rt": all_rts}
    
    results_df = pd.DataFrame(results)

    return results_df

# Function to simulate participants, arguments selects the amount of participants.
def simulate_participants(participants = 10): 
    IDs = np.arange(1, participants+1)
    
    all_participants = []
    
    for ID in IDs:
        data = generate_rts(100)
          
        ID = ID
        
        results = data.assign(ID = ID)
        
        results_clean = results[results["trial"] > 10] # This will remove the first 10 trials
        
        all_participants.append(results_clean)
        
    df = pd.concat(all_participants)
       
    return df

# Here I packaged all of the analyses I want to investigate.
def analyze_rts(data):
    mean_congruent = data[data['condition'] == 'congruent'].rt.mean()
    mean_incongruent = data[data['condition'] == 'incongruent'].rt.mean()

    print(f"Congruent Mean: {mean_congruent}")
    print(f"Incongruent Mean: {mean_incongruent}")
    
    sns.boxplot(data, x='condition', y='rt')
    plt.savefig(f"./{datetime.datetime.now().strftime('%Y%m%d')}_group_level_effects_plot.png")
    plt.show()
    
    sns.boxplot(data, x="condition", y="rt", hue = "ID", legend="auto")
    plt.savefig(f"./{datetime.datetime.now().strftime('%Y%m%d')}_within-participant_variability_plot.png")
    plt.show()

# Now I have to run all the functions. I also save a CSV to keep a copy.
results = simulate_participants(participants=25)

results.to_csv(f"./{datetime.datetime.now().strftime('%Y%m%d')}_stroop_data.csv")

# Plots and analysis are all packaged together to help do some EDA.
analyze_rts(results)

