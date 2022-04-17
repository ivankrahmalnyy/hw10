import json

from flask import Flask

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:  # открывает файл для чтения
    candidates = json.loads(file.read())  # переменная хранит файл в виде словаря


@app.route('/')  # '/' это означает первая(стартовая) страница
def page_index():
    d = ""
    for i in range(len(candidates)):  # проходя по всем ключам
        n = candidates[i]['name']  # запись имени в список
        p = candidates[i]['position']  # запись позиции в список
        s = candidates[i]['skills']  # запись навыков в список
        d += f'{n} - \n{p}\n{s}\n\n'

    return f"<h1><pre>{d}<pre><h1>"


@app.route('/candidates/<name>')  # <....> это скобки аргумента, т.е. конкретно
def page_candidates(name: str):
    d = ""
    for i in range(len(candidates)):  # проходя по всем ключам
        if name.lower() == candidates[i]['name'].lower():
            n = candidates[i]['name']  # запись имени в список
            p = candidates[i]['position']  # запись позиции в список
            s = candidates[i]['skills']  # запись навыков в список
            a = candidates[i]['picture']
            d += f'<img src={a}>\n{n} - \n{p}\n{s}\n\n'

    return f"<h1><pre>{d}<pre><h1>"


@app.route('/skills/<skill>')
def page_skills(skill: str):
    d = ""
    for i in range(len(candidates)):  # проходя по всем ключам
        if skill.lower() in candidates[i]['skills'].lower():
            n = candidates[i]['name']  # запись имени в список
            p = candidates[i]['position']  # запись позиции в список
            s = candidates[i]['skills']  # запись навыков в список
            d += f'{n} - \n{p}\n{s}\n\n'

    return f"<h1><pre>{d}<pre><h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
