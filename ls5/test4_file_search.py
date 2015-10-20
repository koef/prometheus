#!/usr/bin/env python
def file_search(folder, filename):
    if str(folder).find(filename) == -1:
        return False

    path = folder[0] + "/"
    arr_to_srch = folder[1:]

    for element in arr_to_srch:
        if isinstance(element, list):
            temp_var = file_search(element, filename)
            if temp_var:
                return path + temp_var
        if element == filename:
            return path + element

    return False


print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')