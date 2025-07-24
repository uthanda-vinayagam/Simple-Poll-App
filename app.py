from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


polls = []


@app.route('/')
def index():
    return render_template('index.html', polls=polls)  


@app.route('/create', methods=['POST'])
def create():
    question = request.form.get('question')
    options = [request.form.get(f'option{i}') for i in range(1, 6)]
    options = [opt for opt in options if opt]

    if question and options:
        poll = {
            'id': len(polls),
            'question': question,
            'options': options,
            'votes': [0] * len(options)
        }
        polls.append(poll)
        print("Polls list:", polls)  

        return redirect(url_for('view_polls'))
    else:
        return redirect(url_for('index'))


@app.route('/vote/<int:poll_id>')
def vote(poll_id):
    poll = polls[poll_id]
    return render_template('vote.html', poll=poll, poll_id=poll_id)


@app.route('/submit_vote/<int:poll_id>', methods=['POST'])
def submit_vote(poll_id):
    selected = int(request.form['option'])
    polls[poll_id]['votes'][selected] += 1
    return redirect(url_for('results', poll_id=poll_id))


@app.route('/results/<int:poll_id>')
def results(poll_id):
    poll = polls[poll_id]
    return render_template('results.html', poll=poll, zip=zip)


@app.route('/polls')
def view_polls():
    return render_template('polls.html', polls=polls)  


if __name__ == '__main__':
    app.run(debug=True)
