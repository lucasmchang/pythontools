def topn(listlike, n):
    indices = sorted(range(len(listlike)), key=lambda i: listlike[i], reverse=True)[:n]
    values = [listlike[i] for i in indices]
    return indices, values

def bottomn(listlike, n):
    indices = sorted(range(len(listlike)), key=lambda i: listlike[i], reverse=False)[:n]
    values = [listlike[i] for i in indices]
    return indices, values

def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def indexify(listlike):
    item2ix = { item:i for i,item in enumerate(listlike) }
    ix2item = { i:item for i,item in enumerate(listlike) }
    return item2ix, ix2item