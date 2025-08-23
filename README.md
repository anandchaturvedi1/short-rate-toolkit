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

<img width="863" height="470" alt="image" src="https://github.com/user-attachments/assets/b513fb19-bd4f-480d-845b-0b0b72b7ec39" />

---

### CIR Short-Rate Paths  
Shows the **non-negative, mean-reverting behavior** of the CIR model, often used for credit and risk applications.  

<img width="863" height="470" alt="image" src="https://github.com/user-attachments/assets/3b5154fa-4019-48f8-bb01-5e76095567bd" />

---

### Distribution of Rates at Maturity  
Compares terminal rate distributions from Vasicek vs CIR, **highlighting model differences** in tail behavior and positivity.  

<img width="833" height="470" alt="image" src="https://github.com/user-attachments/assets/e598c2f4-3101-4b90-ab9e-50f222bca4ad" />

---

## Sample Results

Sample results are available in **`notebooks/demo.ipynb`**, showing both Monte Carlo and analytic pricing outputs.  

> _Vasicek MC P(0,2) ≈ 0.950991 (stderr 2.483e-18)_ <br>
> _Vasicek analytic P(0,2) = 0.958281_ <br>
> _CIR MC P(0,2) ≈ 0.929371 (stderr 0.000e+00)_ <br>


- **Vasicek model**: Monte Carlo price is close to the analytic closed-form solution, demonstrating correctness of the simulation engine.  
- **CIR model**: Monte Carlo pricing produces a realistic non-negative bond price, consistent with the model’s structure.  

