import numpy as np
from srtoolkit.models.vasicek import Vasicek
from srtoolkit.sim.monte_carlo import monte_carlo_price_zero_coupon

def test_vasicek_mc_close_to_analytic():
    v = Vasicek.from_dict(r0=0.02, params={"kappa":0.2,"theta":0.03,"sigma":0.01})
    mc_price, _ = monte_carlo_price_zero_coupon(v, n_paths=500, T=1.0, n_steps=100, n_workers=2)
    analytic = v.zero_coupon_bond_price(0.0, 1.0, v.r0)
    assert abs(mc_price - analytic) < 1e-2
