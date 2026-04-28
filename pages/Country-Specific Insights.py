import streamlit as st
import pandas as pd
import plotly.express as px
from style_utils import apply_theme, add_theme_toggle

# 1. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('Cleaned_df.csv')
    df=df[df['year']!=2016]
    
    return df

df = load_data()
    


# --- 2. Sidebar Filters ---
st.sidebar.title("🔍 Filters")

with st.sidebar.form(key='my_filter_form'):
    year_range = st.slider("Select Year Range", 
                           int(df['year'].min()), int(df['year'].max()), 
                           value=(int(df['year'].min()), int(df['year'].max())))

    selected_country = st.selectbox("Select Country", 
                                    options=sorted(df['country'].unique()), 
                                    index=0)

    selected_sex = st.multiselect("Select Gender", 
                                  options=df['sex'].unique(), 
                                  default=list(df['sex'].unique()))

    selected_ages = st.multiselect("Select Age Groups", 
                                   options=df['age'].unique(), 
                                   default=list(df['age'].unique()))

    submit_button = st.form_submit_button(label='Apply Filters')
# Apply Theme
apply_theme()
add_theme_toggle()

# --- 3. Filtering Logic ---
filtered_df = df[
    (df['country'] == selected_country) & 
    (df['year'] >= year_range[0]) & 
    (df['year'] <= year_range[1]) &
    (df['sex'].isin(selected_sex)) &
    (df['age'].isin(selected_ages))
]

# --- 4. Page Content ---
with st.container():
    st.title("🌎 Country-Specific Insights")
    st.subheader(f"Analysis for: {selected_country}")

st.divider()

# --- 5. KPIs Section ---
if not filtered_df.empty:
    total_suicides = filtered_df['suicides_no'].sum()
    avg_rate = filtered_df['suicides/100k pop'].mean()
    
    top_sex = filtered_df.groupby('sex')['suicides_no'].sum().idxmax()
    top_age = filtered_df.groupby('age')['suicides/100k pop'].mean().idxmax()
    
    peak_year_series = filtered_df.groupby('year')['suicides_no'].sum()
    peak_year = peak_year_series.idxmax()
    peak_value = peak_year_series.max()

    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-icon"><i class="fas fa-skull"></i></div>
            <div class="metric-value">{total_suicides:,}</div>
            <div class="metric-label">Total Cases</div>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-icon"><i class="fas fa-chart-line"></i></div>
            <div class="metric-value">{avg_rate:.2f}</div>
            <div class="metric-label">Avg Rate (100k)</div>
        </div>""", unsafe_allow_html=True)
        
    with col3:
        risk_class = "high-risk" if top_sex.lower() == "male" else ""
        st.markdown(f"""<div class="metric-card">
            <div class="metric-icon"><i class="fas fa-venus-mars"></i></div>
            <div class="metric-value {risk_class}">{top_sex}</div>
            <div class="metric-label">Highest Risk Sex</div>
        </div>""", unsafe_allow_html=True)
        
    with col4:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-icon"><i class="fas fa-users"></i></div>
            <div class="metric-value" style="font-size: 0.8em;">{top_age}</div>
            <div class="metric-label">Highest Risk Age</div>
        </div>""", unsafe_allow_html=True)
        
    with col5:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-icon"><i class="fas fa-calendar-day"></i></div>
            <div class="metric-value">{peak_year}</div>
            <div class="metric-label">Peak Year ({peak_value:,})</div>
        </div>""", unsafe_allow_html=True)
else:
    st.warning("No data available for the selected filters.")

country_trend = filtered_df.groupby('year')['suicides/100k pop'].mean().reset_index()


#######################################################

peak_year_series = filtered_df.groupby('year')['suicides_no'].sum()
peak_year = peak_year_series.idxmax()
max_suicides = peak_year_series.max()

peak_year_factors = filtered_df[filtered_df['year'] == peak_year]

tab1,tab2,tab3,tab4 = st.tabs(["Historical Peaks", "Global Perspective", "Generational Breakdown", "Socio-Economic Impact"])

with tab1:
    fig_peak = px.bar(
        peak_year_factors, 
        x='age', 
        y='suicides_no', 
        color='sex', 
        barmode='group',
        title=f"⚠️ Peak Year Analysis: {peak_year} ({max_suicides:,} Total Suicides)",
        labels={'suicides_no': 'Suicide Count', 'age': 'Age Group'},
        category_orders={"age": ["5-14 years", "15-24 years", "25-34 years", "35-54 years", "55-74 years", "75+ years"]},
        color_discrete_map={'male': '#00CC96', 'female': '#EF553B'} # ألوان اختيارية
    )

    st.plotly_chart(fig_peak, use_container_width=True)

    top_demographic = peak_year_factors.loc[peak_year_factors['suicides_no'].idxmax()]
    st.info(f"""
    **Insight for {peak_year}:** 
    In the highest recorded year, the most affected demographic was **{top_demographic['sex']}s** 
    aged **{top_demographic['age']}** with **{top_demographic['suicides_no']:,}** cases.
    """)
    volatility_data = filtered_df.groupby('age')['suicides/100k pop'].std().reset_index()
    volatility_data.columns = ['Age Group', 'Volatility (Std)']
    volatility_data = volatility_data.sort_values(by='Volatility (Std)', ascending=False)

    most_volatile = volatility_data.iloc[0]

    st.subheader("💡 Volatility Insight")
    col_v1, col_v2 = st.columns([1, 2])

    with col_v1:
        st.metric("Most Unstable Group", most_volatile['Age Group'])

    with col_v2:
        st.write(f"""
        The **{most_volatile['Age Group']}** age group has shown the most volatile suicide trends in **{selected_country}**. 
        This means their rates fluctuate significantly year-over-year compared to other groups, 
        suggesting they may be more sensitive to specific socio-economic changes in the country.
        """)
######################################################################################
global_avg = df.groupby('year')['suicides/100k pop'].mean().reset_index()

country_avg = filtered_df.groupby('year')['suicides/100k pop'].mean().reset_index()

import plotly.graph_objects as go

with tab2:
    fig_comp = go.Figure()

    fig_comp.add_trace(go.Scatter(
        x=country_avg['year'], 
        y=country_avg['suicides/100k pop'],
        mode='lines+markers',
        name=f'{selected_country}',
        line=dict(color='#EF553B', width=3)
    ))

    fig_comp.add_trace(go.Scatter(
        x=global_avg['year'], 
        y=global_avg['suicides/100k pop'],
        mode='lines',
        name='Global Average',
        line=dict(color='gray', width=2, dash='dash') # خط منقط للتمييز
    ))

    fig_comp.update_layout(
        title=f"🌍 {selected_country} vs. Global Average Suicide Rate",
        xaxis_title="Year",
        yaxis_title="Suicides per 100k Pop",
        hovermode="x unified",
        template="plotly_dark"
    )

    st.plotly_chart(fig_comp, use_container_width=True)

    current_avg = country_avg['suicides/100k pop'].mean()
    world_avg = global_avg['suicides/100k pop'].mean()
    diff = ((current_avg - world_avg) / world_avg) * 100
    if current_avg > world_avg:
        st.warning(f"The average suicide rate in **{selected_country}** is **{abs(diff):.1f}% higher** than the global average.")
    else:
        st.success(f"The average suicide rate in **{selected_country}** is **{abs(diff):.1f}% lower** than the global average.")

    latest_year = df['year'].max()

    global_ranking = df[df['year'] == latest_year].groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).reset_index()
    global_ranking['rank'] = range(1, len(global_ranking) + 1)

    country_rank_row = global_ranking[global_ranking['country'] == selected_country]

    st.subheader(f"🏆 Global Ranking ({latest_year})")

    if not country_rank_row.empty:
        c_rank = country_rank_row['rank'].values[0]
        c_rate = country_rank_row['suicides/100k pop'].values[0]
        total_c = len(global_ranking)
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.metric("Rank", f"#{c_rank} / {total_c}")
        with col_r2:
            st.metric("Rate", f"{c_rate:.2f}")

        top_10 = global_ranking.head(10).copy()
        if selected_country not in top_10['country'].values:
            top_10 = pd.concat([top_10, country_rank_row])

        fig_rank = px.bar(
            top_10, 
            x='suicides/100k pop', 
            y='country', 
            orientation='h',
            title=f"Top Countries vs. {selected_country} ({latest_year})",
            color='country',
            color_discrete_map={selected_country: '#FF4B4B'} 
        )
        fig_rank.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_rank, use_container_width=True)
    else:
        st.warning(f"No global ranking data available for {selected_country} in {latest_year}.")
#############################################################################################################################
gen_comparison = filtered_df.groupby('generation')['suicides_no'].sum().reset_index()

gen_comparison = gen_comparison.sort_values(by='suicides_no', ascending=False)

with tab3:
    fig_gen = px.pie(
        gen_comparison, 
        values='suicides_no', 
        names='generation', 
        title=f'👥 Total Suicides by Generation in {selected_country}',
        hole=0.5, 
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig_gen.update_traces(textinfo='percent+label', pull=[0.1, 0, 0, 0, 0, 0]) # بيسحب أكبر جزء لبره شوية

    st.plotly_chart(fig_gen, use_container_width=True)

    top_gen = gen_comparison.iloc[0]['generation']
    top_gen_val = gen_comparison.iloc[0]['suicides_no']

    st.write(f"""
    In **{selected_country}**, the **{top_gen}** generation has the highest recorded number of suicides 
    with a total of **{top_gen_val:,}** cases across the analyzed period.
    """)

#####################################################################
eco_data = filtered_df.groupby('year').agg({
    'suicides/100k pop': 'mean',
    'gdp_per_capita ($)': 'first'
}).reset_index()

correlation_val = eco_data['suicides/100k pop'].corr(eco_data['gdp_per_capita ($)'])

with tab4:
    fig_eco = px.scatter(
        eco_data, 
        x='gdp_per_capita ($)', 
        y='suicides/100k pop',
        trendline="ols", 
        title=f"💰 Economy vs. Suicide Rate: {selected_country}",
        labels={'gdp_per_capita ($)': 'GDP per Capita ($)', 'suicides/100k pop': 'Suicides per 100k'},
        hover_data=['year'],
        template="plotly_dark"
    )

    st.plotly_chart(fig_eco, use_container_width=True)

    st.subheader("🧐 Economic Insight")

    if abs(correlation_val) < 0.3:
        relation_text = "Weak or No Correlation"
        explanation = "Economic growth doesn't seem to be a primary driver for suicide rates in this country."
    elif correlation_val <= -0.3:
        relation_text = "Negative Correlation"
        explanation = "As GDP increases, suicide rates tend to decrease. Economic prosperity might be a protective factor here."
    else:
        relation_text = "Positive Correlation"
        explanation = "Surprisingly, as GDP increases, suicide rates also tend to increase. This might suggest other social pressures."

    st.write(f"**Correlation Coefficient:** `{correlation_val:.2f}` ({relation_text})")
    st.info(explanation)
    ##########################################
