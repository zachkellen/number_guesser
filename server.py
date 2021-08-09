from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Hello World'

@app.route('/')
def startGame():
    if 'numberTarget' not in session:
        session['numberTarget'] = random.randint(1,100)
    if 'helper' not in session:
        session['helper'] = None
    if 'isCorrect' not in session:
        session['isCorrect'] = False

    return render_template('index.html', numberTarget = session['numberTarget'], helper = session['helper'], isCorrect = session['isCorrect'])

@app.route('/guess', methods=['POST'])
def guessNum():
    hint = ""
    # helper = None
    # isCorrect = False
    if 'numberTarget' in session:
        if(int(request.form['customGuess']) > session['numberTarget']):
            hint = f"{request.form['customGuess']} is too high!"
            session['helper'] = 1
        if(int(request.form['customGuess']) < session['numberTarget']):
            hint = f"{request.form['customGuess']} is too low!"
            session['helper'] = 2
        if(int(request.form['customGuess']) == session['numberTarget']):
            hint = f"{request.form['customGuess']} is correct!!!"
            session['isCorrect'] = True
            session['helper'] = None

    return redirect('/')



@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)