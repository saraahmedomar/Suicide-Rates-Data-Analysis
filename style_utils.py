import streamlit as st

def apply_dark_theme():
    """
    Applies a premium dark futuristic theme with glassmorphism, neon accents,
    animations, and professional styling for a high-end SaaS dashboard.
    """
    css = """
    <!-- Google Fonts and Font Awesome -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* Global Dark Futuristic Theme */
    body {
        background: linear-gradient(135deg, #0e1117 0%, #1a1a2e 100%);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    /* Glassmorphism Containers */
    .main .block-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        padding: 30px;
        margin: 20px;
        animation: fadeIn 0.8s ease-in-out;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        padding: 20px;
        width: 300px;
        font-size: 14px;
    }

    /* Navigation Links as Buttons */
    .sidebar .stMarkdown a {
        display: block;
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        text-decoration: none;
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 10px;
        border: 1px solid rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
        font-weight: 500;
    }
    .sidebar .stMarkdown a:hover {
        background: rgba(0, 212, 255, 0.2);
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        transform: translateY(-2px);
    }

    /* KPI Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        animation: fadeInUp 0.6s ease-out;
    }
    .metric-card:hover {
        box-shadow: 0 0 25px rgba(0, 212, 255, 0.4);
        transform: translateY(-5px);
    }
    .metric-card .metric-icon {
        font-size: 2em;
        margin-bottom: 10px;
        color: #00d4ff;
    }
    .metric-card .metric-value {
        font-size: 1.5em;
        font-weight: 600;
        color: #ffffff;
    }
    .metric-card .metric-label {
        font-size: 0.9em;
        color: #b0b0b0;
    }

    /* Expander and Info Boxes - Enhanced Glassmorphism */
    .st-expander, .st-info, .st-success, .st-warning, .st-error {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(15px);
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        padding: 15px;
        animation: fadeIn 0.5s ease-in-out;
    }

    /* Custom Tabs */
    .st-tabs {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 10px;
    }
    .st-tabs [data-baseweb="tab-list"] {
        gap: 5px;
    }
    .st-tabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        color: #e0e0e0;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .st-tabs [data-baseweb="tab"]:hover {
        background: rgba(0, 212, 255, 0.2);
    }
    .st-tabs [aria-selected="true"] {
        background: rgba(0, 212, 255, 0.3);
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }

    /* Premium Buttons */
    .stButton button {
        background: linear-gradient(135deg, #00d4ff 0%, #007bff 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 212, 255, 0.3);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%);
        box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6);
        transform: translateY(-2px);
    }

    /* DataFrames Styling */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 0.5px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        overflow: hidden;
    }
    .stDataFrame table {
        width: 100%;
        border-collapse: collapse;
    }
    .stDataFrame th {
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    .stDataFrame td {
        padding: 10px 12px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
    .stDataFrame tr:nth-child(even) {
        background: rgba(255, 255, 255, 0.02);
    }
    .stDataFrame tr:hover {
        background: rgba(0, 212, 255, 0.05);
    }

    /* Plotly Charts */
    .js-plotly-plot {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 0.5px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
        animation: fadeIn 0.8s ease-in-out !important;
    }

    /* Images */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        animation: fadeIn 0.6s ease-in-out;
    }

    /* Titles and Headers */
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 600;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }
    h1::before {
        content: "🌌 ";
    }
    h2::before {
        content: "📊 ";
    }
    h3::before {
        content: "🔍 ";
    }

    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.5), transparent);
        margin: 30px 0;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 212, 255, 0.3);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 212, 255, 0.5);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* High-Risk Indicators */
    .high-risk {
        color: #ff4b4b;
        font-weight: 600;
    }
    .high-risk::before {
        content: "⚠️ ";
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 15px;
            margin: 10px;
        }
        .metric-card {
            margin: 5px;
            padding: 15px;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def apply_light_theme():
    """
    Applies a clean, modern light theme with subtle shadows and professional styling.
    """
    css = """
    <!-- Google Fonts and Font Awesome -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* Global Light Theme */
    body {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        color: #212529;
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }

    /* Light Containers */
    .main .block-container {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        padding: 30px;
        margin: 20px;
        animation: fadeIn 0.8s ease-in-out;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        padding: 20px;
        width: 300px;
        font-size: 14px;
    }

    /* Navigation Links as Buttons */
    .sidebar .stMarkdown a {
        display: block;
        background: rgba(0, 123, 255, 0.1);
        color: #007bff;
        text-decoration: none;
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 10px;
        border: 1px solid rgba(0, 123, 255, 0.3);
        transition: all 0.3s ease;
        font-weight: 500;
    }
    .sidebar .stMarkdown a:hover {
        background: rgba(0, 123, 255, 0.2);
        box-shadow: 0 0 15px rgba(0, 123, 255, 0.5);
        transform: translateY(-2px);
    }

    /* KPI Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        animation: fadeInUp 0.6s ease-out;
    }
    .metric-card:hover {
        box-shadow: 0 0 25px rgba(0, 123, 255, 0.3);
        transform: translateY(-5px);
    }
    .metric-card .metric-icon {
        font-size: 2em;
        margin-bottom: 10px;
        color: #007bff;
    }
    .metric-card .metric-value {
        font-size: 1.5em;
        font-weight: 600;
        color: #212529;
    }
    .metric-card .metric-label {
        font-size: 0.9em;
        color: #6c757d;
    }

    /* Expander and Info Boxes */
    .st-expander, .st-info, .st-success, .st-warning, .st-error {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        padding: 15px;
        animation: fadeIn 0.5s ease-in-out;
    }

    /* Custom Tabs */
    .st-tabs {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 10px;
    }
    .st-tabs [data-baseweb="tab-list"] {
        gap: 5px;
    }
    .st-tabs [data-baseweb="tab"] {
        background: rgba(0, 0, 0, 0.05);
        border-radius: 10px;
        color: #212529;
        border: none;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    .st-tabs [data-baseweb="tab"]:hover {
        background: rgba(0, 123, 255, 0.1);
    }
    .st-tabs [aria-selected="true"] {
        background: rgba(0, 123, 255, 0.2);
        box-shadow: 0 0 10px rgba(0, 123, 255, 0.3);
    }

    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #0056b3 0%, #007bff 100%);
        box-shadow: 0 6px 20px rgba(0, 123, 255, 0.5);
        transform: translateY(-2px);
    }

    /* DataFrames Styling */
    .stDataFrame {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 0, 0, 0.1);
        border-radius: 15px;
        overflow: hidden;
    }
    .stDataFrame table {
        width: 100%;
        border-collapse: collapse;
    }
    .stDataFrame th {
        background: rgba(0, 123, 255, 0.1);
        color: #007bff;
        padding: 12px;
        text-align: left;
        font-weight: 600;
    }
    .stDataFrame td {
        padding: 10px 12px;
        border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    }
    .stDataFrame tr:nth-child(even) {
        background: rgba(0, 0, 0, 0.02);
    }
    .stDataFrame tr:hover {
        background: rgba(0, 123, 255, 0.05);
    }

    /* Plotly Charts */
    .js-plotly-plot {
        background: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid rgba(0, 0, 0, 0.1) !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
        animation: fadeIn 0.8s ease-in-out !important;
    }

    /* Images */
    img {
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.6s ease-in-out;
    }

    /* Titles and Headers */
    h1, h2, h3 {
        color: #212529;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }
    h1::before {
        content: "🌞 ";
    }
    h2::before {
        content: "📊 ";
    }
    h3::before {
        content: "🔍 ";
    }

    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 123, 255, 0.5), transparent);
        margin: 30px 0;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.8);
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 123, 255, 0.3);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 123, 255, 0.5);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* High-Risk Indicators */
    .high-risk {
        color: #dc3545;
        font-weight: 600;
    }
    .high-risk::before {
        content: "⚠️ ";
    }

    /* Responsive Adjustments */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 15px;
            margin: 10px;
        }
        .metric-card {
            margin: 5px;
            padding: 15px;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def apply_theme():
    """
    Applies the current theme based on session state.
    """
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'
    
    if st.session_state.theme == 'dark':
        apply_dark_theme()
    else:
        apply_light_theme()

def add_theme_toggle():
    """
    Adds a theme toggle button to the sidebar.
    Call this in the sidebar section of each page.
    """
    if st.sidebar.button("🌙 Toggle Theme" if st.session_state.theme == 'dark' else "☀️ Toggle Theme"):
        st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
        st.rerun()