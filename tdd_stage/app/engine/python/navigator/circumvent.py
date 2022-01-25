

from collections import Iterable


def circumvent(data: dict, keys=None):
    
    '''
    dribbler that retrieves elements from a nested dictionary

    :param data: playground for the dribbler
    :param keys: pin points that the dribbler must follow
    '''
    
    result = []
    
    if isinstance(data, dict):
        if keys is None:
            data = data.values()
        else:
            data = dict(filter(lambda t: t[0] in keys, data.items())).values()
    
    for el in data:
        if isinstance(el, Iterable) and not isinstance(el, str):
            result.extend(circumvent(el, keys))
        else:
            result.append(el)
    
    return result