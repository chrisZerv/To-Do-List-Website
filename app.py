from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample tasks for demonstration
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=sorted(tasks, key=lambda x: (-x['starred'], x['position'])))

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    due_date = request.form.get('due_date')
    if task_content:
        tasks.append({
            'content': task_content,
            'done': False,
            'due_date': due_date,
            'starred': False,
            'position': len(tasks)
        })
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        # Reassign positions
        for i, task in enumerate(tasks):
            task['position'] = i
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = not tasks[task_id]['done']
    return redirect(url_for('index'))

@app.route('/star/<int:task_id>')
def star_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['starred'] = not tasks[task_id]['starred']
    return redirect(url_for('index'))

@app.route('/reorder', methods=['POST'])
def reorder_tasks():
    order = request.form.getlist('order[]')
    ordered_tasks = []
    for index in order:
        ordered_tasks.append(tasks[int(index)])
    for i, task in enumerate(ordered_tasks):
        task['position'] = i
    tasks[:] = ordered_tasks  # Replace original list with reordered list
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
