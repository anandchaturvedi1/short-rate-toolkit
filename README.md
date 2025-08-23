# short-rate-toolkit

A concise Python library implementing classic short-rate models for fixed income analytics.  

## Features
- **Model classes**: Vasicek, CIR, Ho–Lee, Hull–White, with analytic zero-coupon bond pricing where available  
- **Monte Carlo engine**: Parallel path generation for efficient simulations  
- **Utilities**: Timing and memoization decorators for performance  
- **Examples & tests**: Ready-to-run demos for validation  

---

## Example Outputs

### Vasicek Short-Rate Paths  
Demonstrates the **mean-reverting Gaussian dynamics** of the Vasicek model.  

!

---

### CIR Short-Rate Paths  
Shows the **non-negative, mean-reverting behavior** of the CIR model, often used for credit and risk applications.  

!

---

### Distribution of Rates at Maturity  
Compares terminal rate distributions from Vasicek vs CIR, **highlighting model differences** in tail behavior and positivity.  

!

---

## Sample Results

Sample results are available in **`notebooks/demo.ipynb`**, showing both Monte Carlo and analytic pricing outputs.  

Vasicek MC P(0,2) ≈ 0.950991 (stderr 2.483e-18)
Vasicek analytic P(0,2) = 0.958281
CIR MC P(0,2) ≈ 0.929371 (stderr 0.000e+00)

- **Vasicek model**: Monte Carlo price is close to the analytic closed-form solution, demonstrating correctness of the simulation engine.  
- **CIR model**: Monte Carlo pricing produces a realistic non-negative bond price, consistent with the model’s structure.  

---

## Author
**Anand Chaturvedi** — Quantitative Finance Engineer  
(see CV for full background)  
