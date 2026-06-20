from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = ["task1", 'task2', "task3"]


@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)



@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form['task']
    tasks.append(new_task)
    return redirect('/')

@app.route('/delete/<int:task_id>/')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)










