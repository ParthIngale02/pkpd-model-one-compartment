# pkpd-model-one-compartment
# One-Compartment Pharmacokinetic Model – IV Bolus

This repository contains a simulation of a one-compartment pharmacokinetic (PK) model following an intravenous (IV) bolus dose, implemented in Python.

---

## Model Overview

- **Dose**: 100 mg  
- **Volume of Distribution (Vd)**: 10 L  
- **Elimination Rate Constant (kel)**: 0.2 hr⁻¹  
- **Model Equation**:  
  \[
  \frac{dC}{dt} = -k_{el} \cdot C
  \]

Where `C` is the drug concentration in plasma and `kel` is the first-order elimination constant.

---

## Files

| File | Description |
|------|-------------|
| `pk_model.py` | Python script to simulate and plot the concentration-time profile |
| `pk_model_results.csv` | CSV file with simulated time and concentration data |
| `pk_model_plot.png` | Drug concentration vs. time plot |

---

## Requirements

- Python 3.x  
- Packages: `numpy`, `scipy`, `pandas`, `matplotlib`

Install dependencies (if needed):
```bash
pip install numpy scipy pandas matplotlib
python pk_model.py
## Usage

To run the simulation:
```bash
python pk_model.py
Outputs are saved to the output/ folder:

pk_model_results.csv

pk_model_plot.png

Author
Parth Ingale
M.S. Bioengineering, Northeastern University
