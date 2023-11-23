def sum_list(my_list):
    if my_list == []:
        return (None)
    else:
        risultato=0
        for item in my_list:
            risultato=risultato+item
        return (risultato)
        