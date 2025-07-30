import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd
import os

# Define the one-compartment IV bolus PK model
def pk_model(C, t, k_el):
    dCdt = -k_el * C
    return dCdt

# Parameters
dose = 100  # mg, IV bolus dose
Vd = 10     # L, volume of distribution
k_el = 0.2  # 1/hr, elimination rate constant

# Initial concentration
C0 = dose / Vd  # mg/L

# Time vector (in hours)
t = np.linspace(0, 24, 100)

# Solve ODE
C = odeint(pk_model, C0, t, args=(k_el,)).flatten()

# Create DataFrame to save results
df = pd.DataFrame({'Time_hr': t, 'Concentration_mg_per_L': C})

# Save data and plot
os.makedirs("output", exist_ok=True)
df.to_csv("output/pk_model_results.csv", index=False)

# Plot concentration-time profile
plt.figure(figsize=(8, 5))
plt.plot(t, C, label='Drug Concentration', linewidth=2)
plt.title('One-Compartment PK Model (IV Bolus)')
plt.xlabel('Time (hr)')
plt.ylabel('Concentration (mg/L)')
plt.grid(True)
plt.legend()
plt.savefig("output/pk_model_plot.png")
plt.close()

