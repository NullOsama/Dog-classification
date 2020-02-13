from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import os
from util import load_model, predict

model = load_model()

app = Flask(__name__)
uploads_dir = 'static/images'
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/')
def home():
    return redirect(url_for('upload'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    # save the single "profile" file
    if request.method == 'POST':
        profile = request.files['file']
        save_at = os.path.join(uploads_dir, profile.filename)
        profile.save(save_at)
        pred = predict(model, save_at)
        return render_template('upload.html', img_src=profile.filename, prediction=pred)

if __name__ == '__main__':
   app.run(debug = True)



