"""
This module contains a Streamlit application for predicting whether it will rain tomorrow.
"""

import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import streamlit as st

# pylint: disable=invalid-name, too-many-locals, too-many-statements, too-many-arguments

def load_encoder():
    """Load the encoder from a pickle file."""
    with open('encoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    return encoder

@st.cache
def load_model():
    """Load the model from a pickle file."""
    with open('model.h5', 'rb') as file:
        model = pickle.load(file)
    return model

def load_model_columns():
    """Load the model columns from a pickle file."""
    with open('model_columns.pkl', 'rb') as file:
        columns = pickle.load(file)
    return columns

def load_scaler():
    """Load the scaler from a pickle file."""
    with open('scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return scaler

def process_input(data, encoder, features, scaler):
    """Process the input data for the model."""
    data_binary_encoded = encoder.transform(data)

    categorical_columns = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm']
    data_one_hot_encoded = pd.get_dummies(data_binary_encoded[categorical_columns])

    data_combined = pd.concat([data.drop(['RainToday'] + categorical_columns, axis=1), data_one_hot_encoded], axis=1)

    for col in features:
        if col not in data_combined.columns:
            data_combined[col] = 0.5
    data_prepared = data_combined.reindex(columns=features)

    data_scaled = scaler.transform(data_prepared)

    return data_scaled

def main():
    """The main function of the Streamlit application."""
    st.set_page_config(page_title="Czy jutro będzie padać?")
    st.title("Czy jutro będzie padać?")

    encoder = load_encoder()
    model = load_model()
    scaler = load_scaler()
    model_columns = load_model_columns()

    # formularz
    with st.form(key='input_form'):
        # ... (form fields here) ...

        submit_button = st.form_submit_button(label='Przewidź')

    if submit_button:
        # Prepare input data
        input_data = pd.DataFrame([[min_temp, max_temp, rainfall, wind_gust_speed, wind_speed_9am, wind_speed_3pm,
                                    humidity_3pm, pressure_9am, pressure_3pm, latitude, longtitude, year, month, day, rain_today,
                                    location, wind_gust_dir, wind_dir_9am, wind_dir_3pm]],
                                  columns=['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm',
                                           'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Latitude', 'Longitude', 'Year', 'Month', 'Day', 'RainToday',
                                           'Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])
        # Model prediction
        processed_data = process_input(input_data, encoder, model_columns, scaler)
        prediction = model.predict(processed_data)
        st.write(f'Predykcja: {"Rain" if prediction[0] == "Deszcz" else "Brak deszczu"}')

if __name__ == "__main__":
    main()