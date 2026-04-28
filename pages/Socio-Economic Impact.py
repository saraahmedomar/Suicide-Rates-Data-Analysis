import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from style_utils import apply_theme, add_theme_toggle

apply_theme()

@st.cache_data
def load_data():
    df = pd.read_csv('Cleaned_df.csv')
    df = df[df['year'] != 2016]
    return df

df = load_data()

st.title("🌍 Socio-Economic Impact Analysis")
st.markdown("Exploring the relationship between economic wealth and suicide rates.")

st.sidebar.title("🔍 Filters")
year_range = st.sidebar.slider("Select Year Range", 
                       int(df['year'].min()), int(df['year'].max()), 
                       value=(int(df['year'].min()), int(df['year'].max())))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.divider()

st.subheader("💰 Economy vs. Suicide Rates")

eco_trend = filtered_df.groupby('year').agg({
    'suicides/100k pop': 'mean',
    'gdp_per_capita ($)': 'mean'
}).reset_index()

fig_eco = go.Figure()
fig_eco.add_trace(go.Scatter(x=eco_trend['year'], y=eco_trend['gdp_per_capita ($)'],
                                  name="GDP per Capita ($)", yaxis="y2", line=dict(color='#00d4ff', width=3)))
fig_eco.add_trace(go.Scatter(x=eco_trend['year'], y=eco_trend['suicides/100k pop'],
                                  name="Suicide Rate (per 100k)", line=dict(color='#ff4b4b', width=3)))

fig_eco.update_layout(
    yaxis=dict(title="Suicide Rate"),
    yaxis2=dict(title="GDP per Capita ($)", overlaying="y", side="right"),
    hovermode="x unified",
    template="plotly_dark" if st.session_state.get('theme') == 'dark' else "plotly_white"
)
st.plotly_chart(fig_eco, use_container_width=True)

st.divider()

st.header("🔍 Custom Correlation Explorer")
st.info("Choose variables to explore hidden patterns!")

col1, col2, col3 = st.columns(3)
with col1:
    x_axis = st.selectbox("Select X-axis", ['age', 'sex', 'generation', 'country'], index=0)
with col2:
    y_axis = st.selectbox("Select Y-axis", ['suicides/100k pop', 'suicides_no', 'gdp_per_capita ($)'], index=0)
with col3:
    chart_type = st.radio("Chart Type", ["Pie Chart", "Bar Chart"], horizontal=True)

if chart_type == "Pie Chart":
    fig_custom = px.pie(filtered_df, values=y_axis, names=x_axis, color="sex",
                        template="plotly_dark" if st.session_state.get('theme') == 'dark' else "plotly_white")
else:
    df_bar = filtered_df.groupby([x_axis, 'sex'])[y_axis].mean().reset_index()
    fig_custom = px.bar(df_bar, x=x_axis, y=y_axis, color="sex", barmode='group',
                        template="plotly_dark" if st.session_state.get('theme') == 'dark' else "plotly_white")

st.plotly_chart(fig_custom, use_container_width=True)