from flask import Flask, request, render_template
import period  
import pcos  
import mood  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/period_predictor')
def period_predictor():
    return render_template('period_predictor.html')

@app.route('/pcos_predictor')
def pcos_predictor():
    return render_template('pcos_predictor.html')

@app.route('/mood_tracker')
def mood_tracker_page():
    return render_template('mood_tracker.html')

@app.route('/predict_period', methods=['POST'])
def predict_period_route():
    reproductive_phase = int(request.form['reproductive_phase'])
    length_of_cycle = int(request.form['length_of_cycle'])
    mean_cycle_length = float(request.form['mean_cycle_length'])
    length_of_menses = int(request.form['length_of_menses'])
    day1 = int(request.form['day1'])
    day2 = int(request.form['day2'])
    day3 = int(request.form['day3'])
    day4 = int(request.form['day4'])
    day5 = int(request.form['day5'])
    prediction = period.predict_period(
        reproductive_phase, length_of_cycle, mean_cycle_length,
        length_of_menses, day1, day2, day3, day4, day5
    )

    return render_template('result.html', prediction=prediction)

@app.route('/predict_pcos', methods=['POST'])
def predict_pcos():
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = float(request.form['bmi'])
    insulin_level = float(request.form['insulin_level'])
    glucose_level = float(request.form['glucose_level'])
    androgen_level = float(request.form['androgen_level'])
    menstrual_irregularities = int(request.form['menstrual_irregularities'])

    prediction = pcos.predict_pcos(
        age, weight, height, bmi, insulin_level, glucose_level,
        androgen_level, menstrual_irregularities
    )

    return render_template('result.html', prediction=prediction)

@app.route('/predict_mood', methods=['POST'])
def predict_mood():
    sleep_hours = float(request.form['sleep_hours'])
    exercise_hours = float(request.form['exercise_hours'])
    diet_quality = int(request.form['diet_quality'])
    stress_level = int(request.form['stress_level'])
    mood_score = int(request.form['mood_score'])

    prediction = mood.predict_mood(
        sleep_hours, exercise_hours, diet_quality, stress_level, mood_score
    )

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)