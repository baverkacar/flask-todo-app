from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/baverkacar/Desktop/baverToDoApp/todoapp.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    status = db.Column(db.Boolean)

@app.route("/")
def main():
    todos = Todo.query.all()
    return render_template("main.html", todos = todos)

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for("main"))
    
@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main"))



@app.route("/add", methods =["POST"])
def addTodo():
    title = request.form.get("title")
    newTodo = Todo(name = title, status = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("main"))




if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
    







