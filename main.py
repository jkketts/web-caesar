import caesar
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        text = request.form.get("text")
        rot = request.form.get("rot")
        rot_text = caesar.encrypt(text,int(rot))
        return render_template('index.html', rot = rot, rot_text = rot_text)
    else:
        return render_template('index.html')

app.run()