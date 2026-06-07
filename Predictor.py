import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import pickle
import os

try:
    from style_utils import apply_theme
    apply_theme()
except:
    pass

st.set_page_config(page_title="Risk Prediction", layout="wide")

st.title("Suicide Risk Prediction Model 🧠")

@st.cache_resource
def load_assets():
    mlp = load_model('mlp_suicide_model.h5')
    cnn = load_model('cnn_suicide_model.h5')
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    df = pd.read_csv('Cleaned_df.csv') 
    countries_list = sorted(df['country'].unique().tolist())
    generations_list = ['G.I. Generation', 'Silent', 'Boomers', 'Generation X', 'Millenials', 'Generation Z']
    
    return mlp, cnn, scaler, countries_list, generations_list

# تنفيذ التحميل
try:
    mlp, cnn, scaler, countries_list, generations_list = load_assets()
except Exception as e:
    st.error(f"Error loading assets: {e}. Make sure 'Cleaned_df.csv' and model files are in the folder.")
    st.stop()

# --- القائمة الجانبية ---
model_option = st.sidebar.selectbox("Choose AI Model", ("MLP", "CNN")) # تم تعديل الاختيارات هنا
st.sidebar.markdown("---")
st.sidebar.write("### Economics Note:")
st.sidebar.info("**GDP (Gross Domestic Product):** يعبر عن القوة الاقتصادية للدولة. زيادة الـ GDP تعني اقتصاداً أقوى، وهو عامل مؤثر في تقليل المخاطر الاجتماعية.")

st.info(f"Currently using: {model_option} Model")

# --- واجهة إدخال البيانات ---
col1, col2 = st.columns(2)

with col1:
    selected_country = st.selectbox("Select Country", options=countries_list)
    country_index = countries_list.index(selected_country)
    
    year = st.number_input("Year", min_value=1985, value=2015)
    
    sex = st.radio("Sex", options=[0, 1], format_func=lambda x: "Male" if x==1 else "Female")

with col2:
    age_map = {0: "5-14 years", 1: "15-24 years", 2: "25-34 years", 3: "35-54 years", 4: "55-74 years", 5: "75+ years"}
    age = st.selectbox("Age Group", options=list(age_map.keys()), format_func=lambda x: age_map[x])
    
    pop = st.number_input("Population Count", value=100000, step=1000)
    
    gdp = st.number_input("GDP for Year (In Billions $)", value=10.0, help="إجمالي الناتج المحلي للدولة")
    
    selected_gen = st.selectbox("Generation", options=generations_list)
    gen_index = generations_list.index(selected_gen)

# --- عملية التوقع ---
if st.button("Analyze Suicide Risk"):
    input_features = np.array([[country_index, year, sex, age, pop, gdp, gen_index]])
    
    input_scaled = scaler.transform(input_features)
    
    if model_option == "MLP":
        prediction = mlp.predict(input_scaled)
    else: # هذا الجزء خاص بـ CNN فقط الآن
        input_reshaped = input_scaled.reshape(1, input_scaled.shape[1], 1)
        prediction = cnn.predict(input_reshaped)

    # عرض النتيجة النهائية
    probability = prediction[0][0]
    
    st.markdown("---")
    if probability > 0.5:
        st.error(f"### Prediction: HIGH RISK 🔴")
    else:
        st.success(f"### Prediction: LOW RISK 🟢")