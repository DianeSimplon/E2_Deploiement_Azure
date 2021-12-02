#import utils_pytoch
from flask import Flask, request, jsonify, render_template, flash

from utils_pytoch import transform_image, get_prediction

app = Flask(__name__, template_folder='../templates')

app.config['SECRET_KEY']  = "gh"
#route initiale
@app.route('/')
#Atteche templete avec ma fonction "home"
def index():
    #Pour la route initiale
    flash('Allowed image types are -> png, jpg, jpeg, gif')
    return render_template('indexEtienne.html')


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST', 'GET'])
def predict():
    # 1 load image
    # 2 image -> tensor
    # 3 prediction
    # 4 return json

    if request.method == 'POST':

        file = request.files.get('file')
        
        if file is None or file.filename == "":
            # 4 return json
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            # 4 return json
            return jsonify({'error': 'format not supported'})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            #equivalent à ajouter une variable dans le templete
            #flash("prediction")
            flash(prediction)
            # 4 return json
            return render_template('indexEtienne.html', prediction= prediction)
            
        except:
            # 4 return json
            return jsonify({'error': 'error during prediction'})

if __name__ == "__main__":
    app.run(debug=True)