# Importing necessary modules
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

# Creating flask application and creating database connection to ORM with SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/baverkacar/Desktop/baverToDoApp/todoapp.db'
db = SQLAlchemy(app)


# Creating database model with SQLAlchemy
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    status = db.Column(db.Boolean)

# This function is main function. It shows us to main screen. 
@app.route("/")
def main():

    todos = Todo.query.all() # Todos sorted from top to bottom by date.
    return render_template("main.html", todos = todos) # sending todos to main.html


# This function is static flask function. This function completes todo which given id in database.
@app.route("/complete/<string:id>")
def completeTodo(id):

    todo = Todo.query.filter_by(id = id).first() # Receiving todo in database with using it's id.
    todo.status = not todo.status # Changing todo's status.
    db.session.commit()
    return redirect(url_for("main")) 
    

# This function is static flask function. This function deletes todo which given id in database.
@app.route("/delete/<string:id>")
def deleteTodo(id):

    todo = Todo.query.filter_by(id = id).first() # Receiving todo in database with using it's id.
    db.session.delete(todo) 
    db.session.commit()
    return redirect(url_for("main"))


# This function works when http request is equal to POST. It creates todo in database.
@app.route("/add", methods =["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(name = title, status = False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("main"))


if __name__ == "__main__":
    db.create_all() # Activating database.
    app.run(debug = True)  
