from flask import Flask, render_template, request, jsonify
import time
import os

app = Flask(__name__)

def predict_koa_grade(age, bmi, pain_score, stiffness_score):
    score = (pain_score * 4) + (stiffness_score * 3) + ((bmi - 18) * 1.5) + ((age - 30) * 0.8)
    if score < 20:
        return 0, "Normal", "Low", 92
    elif score < 40:
        return 1, "Doubtful OA", "Low", 78
    elif score < 60:
        return 2, "Mild OA", "Moderate", 58
    elif score < 80:
        return 3, "Moderate OA", "High", 40
    else:
        return 4, "Severe OA", "Very High", 22

def predict_progression(grade, exercise_days, walking_minutes, bmi):
    base_months = {0: 60, 1: 48, 2: 36, 3: 24, 4: 12}
    base = base_months.get(grade, 24)
    improvement = (exercise_days * 1.5) + (walking_minutes * 0.3) - ((bmi - 22) * 0.8)
    improved = base + improvement
    return round(base, 1), round(max(improved, base + 2), 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    age = int(data.get('age', 45))
    bmi = float(data.get('bmi', 25))
    pain = int(data.get('pain', 5))
    stiffness = int(data.get('stiffness', 5))

    time.sleep(1.5)

    grade, label, risk, health_score = predict_koa_grade(age, bmi, pain, stiffness)
    baseline, improved = predict_progression(grade, 3, 20, bmi)

    return jsonify({
        'grade': grade,
        'label': label,
        'risk': risk,
        'health_score': health_score,
        'baseline_months': baseline,
        'improved_months': improved
    })

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    grade = int(data.get('grade', 2))
    exercise_days = int(data.get('exercise_days', 3))
    walking_minutes = int(data.get('walking_minutes', 20))
    bmi = float(data.get('bmi', 25))

    time.sleep(0.8)

    baseline, improved = predict_progression(grade, exercise_days, walking_minutes, bmi)

    return jsonify({
        'baseline_months': baseline,
        'improved_months': improved,
        'improvement_percent': round(((improved - baseline) / baseline) * 100, 1)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
