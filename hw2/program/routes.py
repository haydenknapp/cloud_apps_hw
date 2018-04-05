from program import program

from flask import render_template

@program.route('/')
@program.route('/index')
def index():
    return render_template('index.html')


@program.route('/people')
def people():
    people = [ { "name" : "hayden", "age" : "21", "major" : "Computer Science" } ]
    people.append({ "name" : "john", "age" : "45", "major" : "Physics" } )
    people.append({ "name" : "jake", "age" : "23", "major" : "Psychology" } )
    return render_template('people.html', people = people)
