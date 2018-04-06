def lonelyinteger(a):
    # Complete this function
    for i in a:
        if a.count(i) == 1:
            return i

    return None
