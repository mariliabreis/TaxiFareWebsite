import streamlit as st
import datetime
import pandas as pd
import numpy as np
import requests

st.markdown('''# NY Taxi
## This tool was created to help you calculate how much your taxi fare will be
### Please, select your parameters for our calculation:
''')

key = 42

d = st.date_input(
    "Choose a date",
    datetime.date(2021, 3, 12))
st.write('You chose:', d)

t = st.time_input('Choose a time', datetime.time(8, 45))

date_time = datetime.datetime.combine(d,t).strftime("%Y-%m-%d %H:%M:%S UTC")

st.write('You chose', t)

st.markdown('''
### Pickup and dropoff coordinates:
''')

pickup_lon = st.number_input('Insert the pickup longitude')
st.write('The pickup longitude is ', pickup_lon)

pickup_lat = st.number_input('Insert the pickup latitude')
st.write('The pickup latitude is ', pickup_lat)

dropoff_lon = st.number_input('Insert the dropoff longitude')
st.write('The dropoff longitude is ', dropoff_lon)

dropoff_lat = st.number_input('Insert the dropoff latitude')
st.write('The dropoff latitude is ', dropoff_lat)

st.markdown('''
### Number of passengers:
''')

number_passengers = st.number_input('')
st.write('The number of passengers is ', number_passengers)

url = 'http://taxifare.lewagon.ai/predict_fare/'
params = {'key': key,
          'pickup_datetime': date_time,
          'pickup_longitude': float(pickup_lon),
          'pickup_latitude': float(pickup_lat),
          'dropoff_longitude': float(dropoff_lon),
          'dropoff_latitude': float(dropoff_lat),
          'passenger_count': int(number_passengers)}

prediction = requests.get(url=url, params=params).json()

st.write('## Your predicted fare is', prediction['prediction'])

