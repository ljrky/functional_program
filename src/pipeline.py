bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def format_band(bands):
    for band in bands:
        band['country'] = 'Canada'
        band['name'] = band['name'].replace('.', '')
        band['name'] = band['name'].title()


format_band(bands)

print bands

# Pipeline version
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


def copy_helper(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d


def call(function, key):
    def apply_function(record):
        return copy_helper(record, key, function(record.get(key)))

    return apply_function


def pipeline_each(data, function):
    return reduce(lambda a, x: map(x, a), function, data)


result = pipeline_each(bands, [call(lambda x: "Canada", 'country'),
                               call(lambda x: x.replace('.', ''), 'name'),
                               call(lambda x: x.title(), 'name')])
