import streamlit as st

from utils.cookie_manager import get_cookie_manager
from services.visitor_service import get_unique_visitor_count
from services.simulation import run_simulation
from components.chart import plot_simulation
from services.visitor_service import get_country_stats

# ============================================
# CONFIG
# ============================================

st.set_page_config(page_title="DRAM Simulation Tool", layout="wide")

# ============================================
# COOKIE INIT
# ============================================

cookies = get_cookie_manager()
if cookies is None:
    st.stop()

# ============================================
# VISITOR
# ============================================

visitor_count = get_unique_visitor_count(cookies)
country_stats = get_country_stats()
# ============================================
# UI
# ============================================

st.title("📊 DRAM Simulation Dashboard")

st.markdown("""
Simulation of the **Dynamic Misalignment Mechanism of Regulatory Fatigue (DRAM)**.
""")

# ============================================
# SIDEBAR
# ============================================

st.sidebar.header("Simulation Parameters")

initial_id = st.sidebar.number_input("Initial ID", value=1.0)
initial_ar = st.sidebar.number_input("Initial AR", value=0.8)

alpha = st.sidebar.slider("Adjustment Rate (α)", 0.0, 1.0, 0.3)
delta = st.sidebar.slider("Constraint (Δ)", -0.2, 0.0, -0.05)

iterations = st.sidebar.number_input("Iterations", 5, 200, 30)

# ============================================
# RUN
# ============================================

df = run_simulation(initial_id, initial_ar, alpha, delta, iterations)

# ============================================
# LAYOUT
# ============================================

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Dynamics Trajectory")
    fig = plot_simulation(df)
    st.pyplot(fig)



with col2:
    st.metric("👥 Total Visit Hari Ini", visitor_count)
    st.subheader("🌍 Visitor by Country")
    st.bar_chart(country_stats)
    st.subheader("Data Table")
    st.dataframe(df)

print(country_stats)

# ============================================
# DOWNLOAD
# ============================================

st.divider()

csv = df.to_csv(index=False).encode()

st.download_button(
    "📥 Download CSV",
    csv,
    "dram_results.csv",
    "text/csv"
)

# ============================================
# FOOTER
# ============================================

st.caption("© 2026 DRAM Simulation Tool")