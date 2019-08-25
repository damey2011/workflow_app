import json

from django.utils.safestring import mark_safe


def find_display_of_selected_in_value(user_data, values):
    for index, data in enumerate(user_data):
        for val in values:
            if data == val.get('value'):
                user_data[index] = val.get('label')
    return user_data


def get_readable_form_data(data):
    new_data = dict()
    for entry in json.loads(data[0]):
        if entry.get('values'):
            new_data[mark_safe(entry.get('label'))] = find_display_of_selected_in_value(
                entry['userData'], entry['values']
            )
        else:
            new_data[mark_safe(entry.get('label'))] = entry.get('userData')
    return new_data or data


def compare_form_and_response(form, response):
    if len(response) > 0 and isinstance(response[0], str):
        response = json.loads(response[0])
    for index, field in enumerate(form):
        for f in response:
            if field.get('name') == f.get('name'):
                form[index]['userData'] = f.get('userData')
                break
    return form
