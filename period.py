import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load and prepare data
data = pd.read_csv('period.csv')
col = data.columns
label_encoder = LabelEncoder()

# Encode categorical columns
for column in col:
    if data[column].dtype == 'object':
        data[column] = label_encoder.fit_transform(data[column])

# Define feature columns (added MensesScoreDayFive)
feature_columns = ['ReproductiveCategory', 'LengthofCycle', 'MeanCycleLength', 'LengthofMenses', 
                    'MensesScoreDayOne', 'MensesScoreDayTwo', 'MensesScoreDayThree', 'MensesScoreDayFour', 'MensesScoreDayFive']

X = data[feature_columns]
y = data['EstimatedDayofOvulation']

# Split the data and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

def predict_period(reproductive_phase, length_of_cycle, mean_cycle_length, length_of_menses,
                   day1, day2, day3, day4, day5):
    # Create a DataFrame for the new data with the same columns as training data
    new_data = pd.DataFrame({
        'ReproductiveCategory': [reproductive_phase],
        'LengthofCycle': [length_of_cycle],
        'MeanCycleLength': [mean_cycle_length],
        'LengthofMenses': [length_of_menses],
        'MensesScoreDayOne': [day1],
        'MensesScoreDayTwo': [day2],
        'MensesScoreDayThree': [day3],
        'MensesScoreDayFour': [day4],
        'MensesScoreDayFive': [day5]
    })

    # Ensure the DataFrame has all columns used during training
    for column in feature_columns:
        if column not in new_data.columns:
            new_data[column] = [0]  # Add missing columns with default values

    # Make prediction
    prediction = rf_classifier.predict(new_data)[0]
    return prediction
