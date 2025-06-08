from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# تحميل الموديلات
heart_model = joblib.load("ml_models/gradin_boost_model.pkl")  # قلب
breast_model = joblib.load("ml_models/decision_tree_model.pkl")  # سرطان
scaler = joblib.load("ml_models/scaler (1).pkl")  # فقط للقلب

# Route لتوقع مرض القلب
@app.route('/predict-heart', methods=['POST'])
def predict_heart():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    features = scaler.transform(features)  # استخدم السكالر هنا فقط
    prediction = heart_model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

# Route لتوقع سرطان الثدي
@app.route('/predict-breast', methods=['POST'])
def predict_breast():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = breast_model.predict(features)[0]
    print("Breast prediction raw value:", prediction)  # Debug print
    result = "Breast Cancer Detected" if prediction == 4 else "No Breast Cancer"
    return jsonify({"prediction": result})

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501, debug=True)