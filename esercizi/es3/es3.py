var='ciao'
try:
    var=float(var)

except Exception as e:
    print ('{} non è un numero valido'.format(var))
    print('L\'errore è {}'.format (e))
