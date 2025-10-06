import numpy as np
from .helpers import clip01

class MemoryModel:
    def __init__(self, retrival_decay=0.1, encoding_error=0.1, noise = 0.05, penalty = 0.3, seed = None): # Class Constructor
        # Instance attributes: depends on the lenth of things stored in memory (list_length).
        self.retrival_decay = retrival_decay 
        self.encoding_error = encoding_error
        self.rng = np.random.default_rng(seed)
        self.noise = noise # This noise attribute determines the var. in prob of recall from trial to trial.
        self.penalty = penalty

        # Here is creation of the list within "memory"
        self.memory = []

    # Here I write a method that stores the input items into memory
    # The method with return the items that are stored in memory so you can see what is stored when this method is called.
    def store(self, items):
        self.memory = []
        stored_items = []

        p_store = (1 - self.encoding_error)
        p_store += self.rng.normal(0.0, self.noise)

        p_store = clip01(p_store)

        for item in items:
            if p_store > self.rng.random():
                self.memory.append(item)
                stored_items.append(item)

        return stored_items
    
    def interference(self):  # Pretend if the participant is hit with a hammer.
        memory = self.memory # Call memory to be an object before its lost.
        self.memory = [] # A reset of memory, hammer did a number on them.
        items_lost = [] # Here is a list to track what was list

        p_interference = (1 - self.penalty)
        p_interference = clip01(p_interference)

        for item in memory:
            if p_interference < self.rng.random():
                items_lost.append(item)
            else:
                self.memory.append(item)
        
        return items_lost

    def retrieve(self, list_length):
        memory = self.memory

        retrieved_items = []

        p_retrival = 1 - (self.retrival_decay * list_length)
        p_retrival += self.rng.normal(0.0, self.noise)

        p_retrival = clip01(p_retrival)

        for item in memory:
            if p_retrival > self.rng.random():
                retrieved_items.append(item)
        
        return retrieved_items
    
    def simulate_trial(self, list_length, condition):
       
        possible_items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                            'u', 'v', 'w', 'x', 'y', 'z']
        
        self.rng.shuffle(possible_items)

        items = possible_items[0:list_length]
        
        stored = self.store(items)

        if condition == "interference":
            lost = self.interference()

        retrieved = self.retrieve(list_length)

        if retrieved == stored:
            accuracy = 1
        else:
            accuracy = 0
       
        return accuracy