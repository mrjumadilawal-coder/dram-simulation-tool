import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# TITLE
# ============================================

st.set_page_config(page_title="DRAM Simulation Tool", layout="wide")

st.title("📊 DRAM Simulation Dashboard")

st.markdown("""
Simulation of the **Dynamic Misalignment Mechanism of Regulatory Fatigue (DRAM)**.
""")

# ============================================
# SIDEBAR INPUT
# ============================================

st.sidebar.header("Simulation Parameters")

initial_id = st.sidebar.number_input("Initial Intentional Direction (ID)", value=1.0)
initial_ar = st.sidebar.number_input("Initial Affective Regulation (AR)", value=0.8)

alpha = st.sidebar.slider("Adjustment Rate (α)", 0.0, 1.0, 0.3)
delta = st.sidebar.slider("Constraint (Δ per iteration)", -0.2, 0.0, -0.05)

iterations = st.sidebar.number_input("Iterations", 5, 200, 30)

# ============================================
# SIMULATION FUNCTION
# ============================================

def run_simulation():
    data = []

    id_val = initial_id
    ar_val = initial_ar

    # Initial state
    misalignment = id_val - ar_val
    fatigue = abs(misalignment)

    data.append([1, id_val, ar_val, misalignment, fatigue])

    # Iteration
    for i in range(2, int(iterations) + 1):

        # Update AR
        ar_val = ar_val + alpha * (id_val - ar_val)

        # Update ID (constraint)
        id_val = id_val + delta

        # Misalignment
        misalignment = id_val - ar_val

        # Fatigue accumulation
        fatigue += abs(misalignment)

        data.append([i, id_val, ar_val, misalignment, fatigue])

    df = pd.DataFrame(data, columns=[
        "Iteration", "ID", "AR", "Misalignment", "Fatigue"
    ])

    return df


# Run simulation
df = run_simulation()

# ============================================
# VISUALIZATION
# ============================================

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Dynamics Trajectory")

    fig, ax = plt.subplots()

    ax.plot(df["Iteration"], df["ID"], label="ID")
    ax.plot(df["Iteration"], df["AR"], label="AR")
    ax.plot(df["Iteration"], df["Fatigue"], linestyle="--", label="Fatigue")

    ax.set_xlabel("Iteration")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

with col2:
    st.subheader("Data Table")
    st.dataframe(df)

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
# FOOTNOTE
# ============================================

st.caption("Official DRAM Simulation Tool. Copyright @2026 Jumadil Awal & Abdul Azis. All Rights Reserved.")