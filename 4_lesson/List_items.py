# Task 29: Looping over a dict
film = {'name':'Forrest Gump',
        'made':1994,
        'director':'Robert Zemeckis',
        'soundtrack':'Multiple',
        'starring':'Tom Hanks',
        'fun_fact':'''The house used in Forrest Gump
                    is the same house used in The Patriot (2000).
                    Some paneling was changed forinterior shots
                    in the latter film.'''}

while film:
    info = film.popitem()
    print('Key: ' + str(info[0]) + ' | Value: ' + str(info[1]))