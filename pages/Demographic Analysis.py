import streamlit as st
import pandas as pd
import plotly.express as px
from style_utils import apply_theme, add_theme_toggle

# 1. Config & Theme
apply_theme()

# 2. Load Data (مع استبعاد 2016 كما اتفقنا)
@st.cache_data
def load_data():
    df = pd.read_csv('Cleaned_df.csv')
    df = df[df['year'] != 2016]
    return df

df = load_data()

# 3. Sidebar Filters
add_theme_toggle()
st.sidebar.title("🔍 Demographic Filters")

with st.sidebar.form(key='demo_filters'):
    # اختيار الجنس
    gender_selection = st.multiselect("Select Gender", 
                                      options=df['sex'].unique(), 
                                      default=list(df['sex'].unique()))
    # اختيار الأجيال
    gen_selection = st.multiselect("Select Generation", 
                                    options=df['generation'].unique(), 
                                    default=list(df['generation'].unique()))
    
    submit_demo = st.form_submit_button(label='Apply Filters')

# Filtering logic
filtered_demo_df = df[
    (df['sex'].isin(gender_selection)) & 
    (df['generation'].isin(gen_selection))
]

# 4. Main Content
st.title("👥 Demographic Analysis")
st.markdown("تحليل عميق لمعدلات الانتحار بناءً على الفئات العمرية، النوع الاجتماعي، والأجيال.")

st.divider()

if not filtered_demo_df.empty:
    # --- صف الرؤى الأساسية (KPIs) ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        most_affected_age = filtered_demo_df.groupby('age')['suicides_no'].sum().idxmax()
        st.metric("Most Affected Age Group", most_affected_age)
        
    with col2:
        gender_ratio = filtered_demo_df.groupby('sex')['suicides_no'].sum()
        highest_gender = gender_ratio.idxmax()
        st.metric("Highest Risk Gender", highest_gender)
        
    with col3:
        total_demo_cases = filtered_demo_df['suicides_no'].sum()
        st.metric("Total Cases (Filtered)", f"{total_demo_cases:,}")

    st.divider()

    # --- Charts Section ---
    
    # 1. توزيع الانتحار حسب السن والنوع (Grouped Bar Chart)
    st.subheader("📊 Suicide Counts by Age Group & Gender")
    age_order = ["5-14 years", "15-24 years", "25-34 years", "35-54 years", "55-74 years", "75+ years"]
    
    fig_age_sex = px.bar(
        filtered_demo_df.groupby(['age', 'sex'])['suicides_no'].sum().reset_index(),
        x='age', y='suicides_no', color='sex',
        barmode='group',
        category_orders={"age": age_order},
        template="plotly_dark" if st.session_state.theme == 'dark' else "plotly_white",
        color_discrete_map={'male': '#00d4ff', 'female': '#ff4b4b'}
    )
    st.plotly_chart(fig_age_sex, use_container_width=True)

    # 2. مقارنة الأجيال (Donut Chart)
    st.subheader("🧬 Generational Contribution")
    fig_gen = px.pie(
        filtered_demo_df, values='suicides_no', names='generation',
        hole=0.5,
        template="plotly_dark" if st.session_state.theme == 'dark' else "plotly_white",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(fig_gen, use_container_width=True)

    # 3. خريطة حرارية: السن مقابل السنة (Heatmap)
    st.subheader("🔥 Heatmap: Age Groups Trend Over Years")
    heatmap_data = filtered_demo_df.groupby(['year', 'age'])['suicides/100k pop'].mean().unstack()
    fig_heat = px.imshow(
        heatmap_data.T, 
        labels=dict(x="Year", y="Age Group", color="Rate per 100k"),
        aspect="auto",
        color_continuous_scale="Reds",
        template="plotly_dark" if st.session_state.theme == 'dark' else "plotly_white"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

else:
    st.warning("⚠️ No data available for the selected demographic filters.")