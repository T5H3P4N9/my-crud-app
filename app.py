#imports
from flask import Flask, render_template, redirect, request       #note these imports
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#my App
app = Flask(__name__)#note how we use app to start or create things in flask


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


#data class
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String[100], nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"Task {self.id}"

with app.app_context():
    db.create_all()

#home page
@app.route("/",methods=["POST","GET"])#creating a route here AND ADDED OUR GET AND  POST METHODS
def index():
    #add a Task(logic to add a task on our home page)
    if request.method == "POST":
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    #See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()#getting  your tasks by order of dates variable "created" in class MyTask  belongs to datetime 
        return render_template('index.html',tasks=tasks)

#delete an Item
@app.route("/delete/<int:id>")
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"ERROR: {e}"
    

#edit an item
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR: {e}"
    else:
        return render_template('edit.html',task=task)

    


#runner and debugger
if __name__ == "__main__":
    app.run(debug=True)