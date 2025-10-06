import argparse
from .models import MemoryModel #, InterferenceMemoryModel
from .sim_group import simulate_group
from .plot_data import create_myPlot

if __name__ == '__main__': ### This has to be like this no matter what. The __init__.py also needs to be in the current file directory.
    parser = argparse.ArgumentParser()
    parser.add_argument('--list_length', type=int, nargs='+', default = [4, 6, 8])
    parser.add_argument('--num_trials', type=int, default=20)
    parser.add_argument('--num_participants', type=int, default=16)
    all_my_argus = parser.parse_args()

    print(simulate_group(num_participants=all_my_argus.num_participants, list_length=all_my_argus.list_length, num_trials=all_my_argus.num_trials))

    create_myPlot("./letter_memory_in-process.csv")
    

