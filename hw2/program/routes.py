from program import program

from flask import render_template

@program.route('/')
@program.route('/index')
def index():
    return render_template('index.html')


@program.route('/people')
def people():
    people = [ { "name" : "hayden", "age" : "21", "major" : "Computer Science" } ]
    for person in people:
        print(person["name"])
    return render_template('people.html', people = people)
