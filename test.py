import requests
body_request = {
    'valid_two_order_field_email_date': {
        'order_email': 'ivanov@mail.ru',
        'order_date': '2024-12-14'
    },
    'valid_two_user_field_email_date': {
        'user_email': 'fedorov@mail.ru',
        'user_date': '2024-10-20'
    },
    'valid_two_order_field_email_phone': {
        'order_email': 'sidorov@mail.ru',
        'order_phone': '+7 777 555 90 80'
    },
    'valid_two_user_field_email_phone': {
        'user_email': 'petrov@mail.ru',
        'user_phone': '+7 999 666 90 80'
    },
    'valid_three_order_field_email_phone_date': {
        'order_email': 'ivanov@mail.ru',
        'order_phone': '+7 444 111 90 80',
        'order_date': '2024-06-20'
    },
    'valid_three_user_field_email_phone_date': {
        'user_email': 'sidorov@mail.ru',
        'user_phone': '+7 777 555 90 80',
        'user_date': '2024-06-20'
    },
    'valid_one_order_field_email': {
        'order_email': 'lebedev@mail.ru'
    },
    'valid_one_user_field_email': {
        'user_email': 'kuznecov@mail.ru'
    },
    'valid_one_order_field_text': {
        'order_text': 'text__text'
    },
    'valid_one_user_field_text': {
        'user_text': 'text__text__text'
    },
    'invalid_type_three_order_field_email_phone_date': {
        'order_email': 'ivanov@mail',
        'order_phone': '+7 (444) xxx 90 80',
        'order_date': '20-06-2024'
    },
    'non-existent_fields_three_order_field_email_phone_date': {
        'non-existent_email': 'ivanov@mail',
        'non-existent_phone': '+7 444 888 90 80',
        'non-existent_date': '2024-06-20'
    },
    'invalid_type_one_order_field_email': {
        'order_email': ''
    },
}
for body_name, body in body_request.items():
    response = requests.post('http://localhost:8000/get_form', json=body)
    print(f'REQUEST: {body_name}, RESPONSE: {response.json()}')
