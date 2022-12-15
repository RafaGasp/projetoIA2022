from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import os
from serverprocess import processar

from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredosegredoso12325'
app.config['UPLOAD_FOLDER'] = 'static/files'

ALLOWED_EXTENSIONS = set(['csv','xlsx', 'txt'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Enviar Arquivo")

@app.route("/", methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    if request.method == 'POST':
        file = request.files['file']
        dado = request.form['dado']
        print(dado)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_local = os.path.join('static',filename)
            file.save(save_local)
            output = processar(save_local, dado)
            return redirect(url_for('resultado'))

    
    return render_template('app.html')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html', )
if __name__ == '__main__':
    app.run(debug=True)