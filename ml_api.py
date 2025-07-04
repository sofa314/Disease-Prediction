# Activate ML environment first:
# source activate ml
# python3 ml_api.py


from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib
import numpy as np


app = Flask(__name__)
CORS(app)


# تحميل الموديلات
heart_model = joblib.load("ml_models/gradient_boosting_model.pkl")  # قلب
breast_model = joblib.load("ml_models/decision_tree_model.pkl")  # سرطان
scaler = joblib.load("ml_models/scaler.pkl")  # لو محتاجه

# Route لتوقع مرض القلب
@app.route('/predict-heart', methods=['POST'])
def predict_heart():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    features = scaler.transform(features)  # scaling لو الموديل محتاجه
    prediction = heart_model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

# Route لتوقع سرطان الثدي
@app.route('/predict-breast', methods=['POST'])
def predict_breast():
    data = request.get_json()

    # استخرج القيم واحدة واحدة
    clump_thickness = data['clump_thickness']
    uniformity_cell_size = data['uniformity_cell_size']
    uniformity_cell_shape = data['uniformity_cell_shape']
    marginal_adhesion = data['marginal_adhesion']
    single_epithelial_cell_size = data['single_epithelial_cell_size']
    bare_nuclei = data['bare_nuclei']
    bland_chromatin = data['bland_chromatin']
    normal_nucleoli = data['normal_nucleoli']
    mitoses = data['mitoses']

    features = np.array([
        clump_thickness,
        uniformity_cell_size,
        uniformity_cell_shape,
        marginal_adhesion,
        single_epithelial_cell_size,
        bare_nuclei,
        bland_chromatin,
        normal_nucleoli,
        mitoses
    ]).reshape(1, -1)

    prediction = breast_model.predict(features)[0]
    result = "Malignant" if prediction == 4 else "Benign"
    return jsonify({"prediction": result})

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)