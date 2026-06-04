def enough(cap, on, wait):
    if wait < (cap - on):
        return 0
    else:
        return wait - (cap - on)