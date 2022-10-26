from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

clf = pickle.load(open('model.pkl','rb'))


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    cgpa = float(request.form.get('cgpa'))
    iq = float(request.form.get('iq'))

    result = clf.predict([[cgpa,iq]])[0]

    if result==1:
        return render_template('index.html', label = "WILL GET THE PLACEMENT")
    else:
        return render_template('index.html', label = "WILL NOT GET THE PLACEMENT")






if __name__ == '__main__':
    app.run(debug=True)