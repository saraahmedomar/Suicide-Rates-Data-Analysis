import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from style_utils import apply_theme, add_theme_toggle

# Apply Theme
apply_theme()

# Custom Plotly Template based on theme
if st.session_state.theme == 'dark':
    custom_template = go.layout.Template()
    custom_template.layout = go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)',
            tickcolor='#e0e0e0'
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            linecolor='rgba(255,255,255,0.2)',
            tickcolor='#e0e0e0'
        ),
        colorway=['#00d4ff', '#ff4b4b', '#00ff88', '#ffaa00']
    )
else:
    custom_template = go.layout.Template()
    custom_template.layout = go.Layout(
        paper_bgcolor='rgba(255,255,255,0)',
        plot_bgcolor='rgba(255,255,255,0)',
        font=dict(color='#212529'),
        xaxis=dict(
            gridcolor='rgba(0,0,0,0.1)',
            linecolor='rgba(0,0,0,0.2)',
            tickcolor='#212529'
        ),
        yaxis=dict(
            gridcolor='rgba(0,0,0,0.1)',
            linecolor='rgba(0,0,0,0.2)',
            tickcolor='#212529'
        ),
        colorway=['#007bff', '#dc3545', '#28a745', '#ffc107']
    )

# 1. Config
st.set_page_config(page_title="Global Suicide Insights", page_icon="📊", layout="wide")

# 2. Load Data
@st.cache_data
def load_data():
    return pd.read_csv('Cleaned_df.csv')

df = load_data()

# --- 3. Session State for Reset ---
if 'year_range' not in st.session_state:
    st.session_state.year_range = (int(df['year'].min()), int(df['year'].max()))
if 'selected_sex' not in st.session_state:
    st.session_state.selected_sex = list(df['sex'].unique())
if 'selected_ages' not in st.session_state:
    st.session_state.selected_ages = list(df['age'].unique())
if 'selected_countries' not in st.session_state:
    st.session_state.selected_countries = []

def reset_filters():
    st.session_state.year_range = (int(df['year'].min()), int(df['year'].max()))
    st.session_state.selected_sex = list(df['sex'].unique())
    st.session_state.selected_ages = list(df['age'].unique())
    st.session_state.selected_countries = []

# --- 4. Sidebar Filter Form ---
st.sidebar.title("🔍 Filters")

with st.sidebar.form(key='my_filter_form'):
    year_range = st.slider("Select Year Range", 
                           int(df['year'].min()), int(df['year'].max()), 
                           value=st.session_state.year_range, key="yr_slider")

    selected_sex = st.multiselect("Select Gender", 
                                  options=df['sex'].unique(), 
                                  default=st.session_state.selected_sex)

    selected_ages = st.multiselect("Select Age Groups", 
                                   options=df['age'].unique(), 
                                   default=st.session_state.selected_ages)

    selected_countries = st.multiselect("Select Countries", 
                                        options=sorted(df['country'].unique()), 
                                        default=st.session_state.selected_countries)

    submit_button = st.form_submit_button(label='Apply Filters')

# Theme Toggle Button
add_theme_toggle()

# --- 5. Filtering Logic ---
filtered_df = df[
    (df['year'] >= year_range[0]) & 
    (df['year'] <= year_range[1]) &
    (df['sex'].isin(selected_sex)) &
    (df['age'].isin(selected_ages))
]
if selected_countries:
    filtered_df = filtered_df[filtered_df['country'].isin(selected_countries)]

# --- 6. Main Content ---
with st.container():
    st.title("🌎 Global Suicide Rates Dashboard")

    with st.expander("📖 View Full Data Dictionary & Sample", expanded=False):
        tab_sample, tab_desc = st.tabs(["🔢 Data Sample", "📖 Data Dictionary"])
        with tab_sample:
            st.write("The cleaned dataset contains the following columns:")
            st.dataframe(df, use_container_width=True)
        with tab_desc:
            st.markdown("""
| Column Name | Description |
| :--- | :--- |
| **country** | The name of the country where data was recorded. |
| **year** | The specific year of the recorded data. |
| **sex** | Biological sex of the target group (Male or Female). |
| **age** | The specific age range (e.g., 15-24 years). |
| **suicides_no** | Total number of recorded suicides for that group. |
| **population** | Total population count for that demographic group. |
| **suicides/100k pop** | Suicide rate calculated per 100,000 inhabitants. |
| **gdp_for_year ($)** | Total Gross Domestic Product of the country for that year. |
| **gdp_per_capita ($)** | GDP divided by the total population (Income indicator). |
| **generation** | Generation name based on the age group (e.g., Boomers, Gen X). |
| **new_age** | Encoded numerical representation of age groups. |
| **sex_numeric** | Encoded numerical representation of sex (1 for Male, 0 for Female). |
| **gdp_billion** | Total GDP scaled to billions for better readability. |
| **Category** | High-level classification (e.g., income level or region). |
            """)

st.divider()

# --- 7. Advanced KPIs ---
if not filtered_df.empty:
    total_suicides = filtered_df['suicides_no'].sum()
    avg_rate = filtered_df['suicides/100k pop'].mean()
    top_sex = filtered_df.groupby('sex')['suicides_no'].sum().idxmax()
    top_age = filtered_df.groupby('age')['suicides/100k pop'].sum().idxmax()
    top_country = filtered_df.groupby('country')['suicides/100k pop'].mean().idxmax()

    with st.container():
        st.subheader("📊 Key Performance Indicators")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-skull"></i></div>
                <div class="metric-value">{total_suicides:,}</div>
                <div class="metric-label">Total Suicides</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-chart-line"></i></div>
                <div class="metric-value">{avg_rate:.2f}</div>
                <div class="metric-label">Avg Rate / 100k</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            risk_class = "high-risk" if top_sex == "Male" else ""
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-venus-mars"></i></div>
                <div class="metric-value {risk_class}">{top_sex}</div>
                <div class="metric-label">Highest Risk Sex</div>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-users"></i></div>
                <div class="metric-value">{top_age}</div>
                <div class="metric-label">Highest Risk Age</div>
            </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon"><i class="fas fa-globe"></i></div>
                <div class="metric-value">{top_country}</div>
                <div class="metric-label">Top Country</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # --- 8. Charts (One per row for clarity) ---
    with st.container():
        st.subheader("🗺️ Global Distribution of Suicide Rates")
        map_df = filtered_df.groupby('country')['suicides/100k pop'].mean().reset_index()
        fig_map = px.choropleth(map_df, locations="country", locationmode='country names', 
                                color="suicides/100k pop", color_continuous_scale="Reds",
                                height=600, template=custom_template)
        st.plotly_chart(fig_map, use_container_width=True)

    with st.container():
        st.subheader("📈 Total Suicides Trend Over Years")
        trend_df = filtered_df.groupby('year')['suicides_no'].sum().reset_index()
        fig_line = px.line(trend_df, x='year', y='suicides_no', markers=True, height=500, template=custom_template)
        st.plotly_chart(fig_line, use_container_width=True)

else:
    st.warning("⚠️ No data matches your filter criteria.")
