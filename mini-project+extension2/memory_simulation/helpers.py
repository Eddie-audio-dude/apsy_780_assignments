def clip01(prob):
    if prob > 1:
        prob = 1
    if prob < 0:
        prob = 0

    return prob