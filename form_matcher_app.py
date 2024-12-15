import uvicorn
from tinydb import TinyDB, Query
from fastapi import FastAPI, Request
import re

app = FastAPI()


@app.get('/')
async def root():
    return 'Welcome to FastAPI!'

regular_exp = {
    'date': r'^\d{2}\.\d{2}\.\d{4}$|^\d{4}-\d{2}-\d{2}$',
    'phone': r'^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$',
    'email': r'^[\w\.-]+@[\w\.-]+\.\w+$',
    'text': r'.+'
}


@app.post('/get_form')
async def get_form(request: Request):
    """
    Возвращает имена шаблонов форм, все поля которых (кроме 'name')
    входят в список полей в запросе и значения полей в запросе
    соответствуют типам данных соответствующих полей в шаблонах.
    Если шаблоны не найдены, то возвращает поля запроса и тип данных
    их значений.
    """
    db = TinyDB('db.json')
    Template = Query()
    request_data = await request.json()
    matching_templates = {}

    for field_name, field_value in request_data.items():
        # Поиск шаблонов, в которых есть поля указанные в запросе.
        templates = db.search(getattr(Template, field_name).exists())
        for template in templates:
            name_tmplt = template.pop('name', None)
            if all(field_name in request_data for field_name in template):
                # Если все поля шаблона совпадают с полями в запросе,
                # то проверяем соответствие значений полей в запросе
                # типам данных соответствующих полей в шаблонах.
                validation_results = []
                for fld_name, fld_type in template.items():
                    reg_exp = regular_exp.get(fld_type)
                    value = request_data.get(fld_name)
                    value_is_valid = re.fullmatch(reg_exp, value)
                    validation_results.append(value_is_valid)
                if all(validation_results):
                    matching_templates[name_tmplt] = len(validation_results)

    if not matching_templates:
        # Вывод типов данных для значений полей запроса, для которого
        # нет шаблонов
        field_types = {}
        field_type = 'FIELD_TYPE_ERROR'
        for field_name, field_value in request_data.items():
            for type_key in ['date', 'phone', 'email', 'text']:
                reg_exp = regular_exp[type_key]
                if re.fullmatch(reg_exp, field_value):
                    field_type = type_key
                    break
            field_types[field_name] = field_type

        return field_types

    # Выбор наиболее подходящих шаблонов (больше всего совпадающих полей)
    most_matching_templates = [
        key for key, value in matching_templates.items()
        if value == max(matching_templates.values())
    ]
    return most_matching_templates

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
