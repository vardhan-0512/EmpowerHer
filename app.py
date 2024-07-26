from flask import Flask, request, render_template, redirect, url_for
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

@app.route('/doctor_appointment')
def doctor_appointment():
    return render_template('doctor_appointment.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    full_name = request.form['full_name']
    age = request.form['age']
    email = request.form['email']
    appointment_date = request.form['date']
    appointment_time = request.form['time']
    problem = request.form['problem']

    return redirect(url_for('appointment_response', name=full_name, date=appointment_date, time=appointment_time, email=email))

@app.route('/appointment_response')
def appointment_response():
    name = request.args.get('name')
    appointment_date = request.args.get('date')
    appointment_time = request.args.get('time')
    email = request.args.get('email')
    return render_template('response.html', name=name, appointment_date=appointment_date, appointment_time=appointment_time, email=email)

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
    responses = {
        "irregular_periods": request.form.get("irregular_periods"),
        "excessive_hair_growth": request.form.get("excessive_hair_growth"),
        "acne_oily_skin": request.form.get("acne_oily_skin"),
        "weight_gain": request.form.get("weight_gain"),
        "hair_loss": request.form.get("hair_loss"),
        "dark_patches": request.form.get("dark_patches"),
        "mood_changes": request.form.get("mood_changes")
    }

    likelihood_percentage = pcos.calculate_pcos_likelihood(responses)

    return render_template('pcos_result.html', prediction=likelihood_percentage)

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
