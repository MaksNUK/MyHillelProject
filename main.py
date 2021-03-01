from flask import Flask, render_template, request
from faker import Faker
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/requirements/')
def requirements():
    with open('requirements.txt') as rq:
        data = rq.readlines()
        data = [x for x in data]
        return render_template(
            'requirements.html', **{
                'requirements': data,
                'query': request.values
            })

@app.route('/generate-users/', methods=['GET', 'POST'])
def generate_users():
    fake = Faker()
    users = {}
    if request.method == 'POST' and request.form.get("count"):
        count_users = int(request.form.get("count"))
    elif request.args.get('count_users'):
        count_users = int(request.args.get('count_users'))
    else:
        count_users = 100
    for _ in range(count_users):
        users[fake.unique.first_name()] = fake.unique.email()
    return render_template(
        'generate_users.html', **{
            'users': users
        })


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()
    number = data['number']
    names_l = [astronaut['name'] for astronaut in data['people']]
    return render_template(
        'space.html', **{
            'number': number,
            'names': names_l
        })

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5555,
        debug=False
    )
