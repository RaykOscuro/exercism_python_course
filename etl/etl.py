def transform(legacy_data):
    data = dict()
    for key in legacy_data:
        for value in legacy_data[key]:
            data[value.lower()]=key
    return data
