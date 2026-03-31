# 📊 DRAM Simulation Dashboard

Simulation tool for the **Dynamic Misalignment Mechanism of Regulatory Fatigue (DRAM)** built using **Streamlit**.

This application models how misalignment between **Intentional Direction (ID)** and **Affective Regulation (AR)** evolves over time and contributes to accumulated **fatigue**.

---

## 🚀 Features

- Interactive simulation with adjustable parameters
- Real-time visualization of:
  - Intentional Direction (ID)
  - Affective Regulation (AR)
  - Fatigue accumulation
- Data table output
- Export simulation results to CSV

---

## ⚙️ Parameters

The simulation can be customized using the sidebar:

| Parameter | Description |
|----------|------------|
| Initial ID | Starting value of Intentional Direction |
| Initial AR | Starting value of Affective Regulation |
| α (Adjustment Rate) | Speed at which AR adapts to ID |
| Δ (Constraint) | Change applied to ID per iteration |
| Iterations | Number of simulation steps |

---

## 🧠 Model Logic

At each iteration:

1. **Affective Regulation (AR)** adjusts toward ID:
