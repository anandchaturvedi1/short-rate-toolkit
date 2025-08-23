from srtoolkit.models.vasicek import Vasicek
from srtoolkit.models.cir import CIR
from srtoolkit.sim.monte_carlo import monte_carlo_price_zero_coupon
import numpy as np

def main():
    # Setup small demo with Vasicek
    vas_params = {"kappa": 0.15, "theta": 0.03, "sigma": 0.01}
    v = Vasicek.from_dict(r0=0.02, params=vas_params)
    price_mc, stderr = monte_carlo_price_zero_coupon(v, n_paths=2000, T=2.0, n_steps=200, n_workers=6)
    print(f"Vasicek MC P(0,2) ≈ {price_mc:.6f} (stderr {stderr:.3e})")
    # Analytic P(0,2) using r0
    analytic = v.zero_coupon_bond_price(0.0, 2.0, v.r0)
    print(f"Vasicek analytic P(0,2) = {analytic:.6f}")

    # CIR short example
    cir_params = {"kappa": 0.2, "theta": 0.04, "sigma": 0.02}
    c = CIR.from_dict(r0=0.03, params=cir_params)
    price_mc_c, stderr_c = monte_carlo_price_zero_coupon(c, n_paths=2000, T=2.0, n_steps=200)
    print(f"CIR MC P(0,2) ≈ {price_mc_c:.6f} (stderr {stderr_c:.3e})")
    print("Demo complete.")

if __name__ == "__main__":
    main()
