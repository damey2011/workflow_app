import json


def find_display_of_selected_in_value(user_data, values):
    for index, data in enumerate(user_data):
        for val in values:
            if data == val['value']:
                user_data[index] = val['label']
    return user_data


def get_readable_form_data(data):
    new_data = dict()
    for entry in json.loads(data[0]):
        if entry.get('values'):
            new_data[entry['label']] = find_display_of_selected_in_value(entry['userData'], entry['values'])
        else:
            new_data[entry['label']] = entry['userData']
    return new_data or data


def compare_form_and_response(form, response):
    for index, field in enumerate(form):
        for f in response:
            if field['name'] == f['name']:
                form[index]['userData'] = f['userData']
                break
    return form
