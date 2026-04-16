import streamlit as st
import pandas as pd
import plotly.express as px

from utils.cookie_manager import get_cookie_manager
from services.visitor_service import get_unique_visitor_count, get_country_stats
from services.simulation import run_simulation

# ============================================
# CONFIG
# ============================================

st.set_page_config(
    page_title="DRAM Simulation Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# GLOBAL STYLE (BIAR CLEAN & CENTERED)
# ============================================

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
    max-width: 1400px;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# COOKIE INIT
# ============================================

cookies = get_cookie_manager()
if cookies is None:
    st.stop()

# ============================================
# VISITOR DATA
# ============================================

visitor_count = get_unique_visitor_count(cookies)
country_stats = get_country_stats()

# ============================================
# HEADER
# ============================================

st.title("📊 DRAM Simulation Dashboard")
st.caption("Dynamic Misalignment Mechanism of Regulatory Fatigue")

st.divider()

# ============================================
# SIDEBAR
# ============================================

st.sidebar.header("⚙️ Simulation Parameters")

initial_id = st.sidebar.number_input("Initial ID", value=1.0)
initial_ar = st.sidebar.number_input("Initial AR", value=0.8)

alpha = st.sidebar.slider("Adjustment Rate (α)", 0.0, 1.0, 0.3)
delta = st.sidebar.slider("Constraint (Δ)", -0.2, 0.0, -0.05)

iterations = st.sidebar.number_input("Iterations", 5, 200, 30)

# ============================================
# SIMULATION
# ============================================

df = run_simulation(initial_id, initial_ar, alpha, delta, iterations)

# ============================================
# MAIN CHART (PLOTLY)
# ============================================

fig_plotly = px.line(
    df,
    x="Iteration",
    y=["ID", "AR", "Fatigue"],
    markers=True
)

fig_plotly.update_layout(
    template="plotly_dark",
    hovermode="x unified",
    height=500,
    margin=dict(l=0, r=0, t=30, b=0)
)

# ============================================
# MAIN GRID
# ============================================

col_main, col_side = st.columns([4, 1.5])

# ============================================
# LEFT (MAIN CHART)
# ============================================

with col_main:
    st.markdown("### 📈 Dynamics Trajectory")
    st.plotly_chart(fig_plotly, use_container_width=True)

# ============================================
# RIGHT (SIDE DASHBOARD)
# ============================================

with col_side:

    # ===== VISITOR CARD =====
    st.markdown("#### 👥 Visitors Todays")

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #0f172a, #1e293b);
        padding:18px;
        border-radius:14px;
        text-align:center;
        margin-bottom:15px;
    ">
        <h1 style="color:#22c55e; margin:0;">{visitor_count}</h1>
        <span style="color:#94a3b8;">Today</span>
    </div>
    """, unsafe_allow_html=True)

    # ===== COUNTRY CHART =====
    st.markdown("#### 🌍 Country")

    if country_stats:
        df_country = pd.DataFrame(
            list(country_stats.items()),
            columns=["Country", "Visitors"]
        )

        fig_country = px.bar(
            df_country,
            x="Country",
            y="Visitors",
            text="Visitors",
            color="Visitors",
            color_continuous_scale="greens"
        )

        fig_country.update_layout(
            template="plotly_dark",
            height=220,
            margin=dict(l=0, r=0, t=10, b=0),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig_country, use_container_width=True)

    else:
        st.info("No data")


# ============================================
# TABLE
# ============================================

st.divider()

st.markdown("### 📋 Simulation Data")

st.dataframe(
    df,
    use_container_width=True,
    height=320
)

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