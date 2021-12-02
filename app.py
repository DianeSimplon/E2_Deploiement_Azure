from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='../templates')



@app.route('/', methods=['GET','POST'])
def predict():
    return render_template('indexEtienne.html')

if __name__ == '__main__':
    app.debug = True
    app.run()