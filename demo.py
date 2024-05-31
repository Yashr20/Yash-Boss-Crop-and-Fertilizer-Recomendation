from flask import Flask,request,render_template

import numpy
import pandas
import sklearn
import pickle
app=Flask(__name__)
#importing model
model=pickle.load(open('model.pkl','rb'))
ferti=pickle.load(open('model1.pkl','rb'))
#creating flask app


@app.route('/')
def index():
    return render_template('index.html')
# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('crop.html')

# render fertilizer recommendation form page


@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Harvestify - Fertilizer Suggestion'

    return render_template('fertilizer.html')
# RENDER PREDICTION PAGES
# render crop recommendation result page


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('crop-result.html', prediction=final_prediction, title=title)



# render fertilizer recommendation result page


@ app.route('/fertilizer-predict', methods=['POST'])
def fert_recommend():
    title = 'Harvestify - Fertilizer Suggestion'

    if request.method == 'POST':
        temp = request.form.get('temp')
        humi = request.form.get('humid')
        mois = request.form.get('mois')
        soil = request.form.get('soil')
        crop = request.form.get('crop')
        nitro = request.form.get('nitro')
        pota = request.form.get('pota')
        phosp = request.form.get('phos')
        input = [int(temp), int(humi), int(mois), int(soil), int(crop), int(nitro), int(pota), int(phosp)]

        res = ferti.classes_[model.predict([input])]

        return render_template('index.html', x=('Predicted Fertilizer is {}'.format(res)))








#python main
if __name__=="__main__":
    app.run(debug=False)