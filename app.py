from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here you would add logic to verify the email and password
        # For demonstration, we will just redirect to a success page
        return redirect(url_for('success'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=2800, debug=True)