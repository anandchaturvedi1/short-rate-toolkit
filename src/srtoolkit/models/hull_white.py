from .base import ShortRateModel
import numpy as np
from dataclasses import dataclass

@dataclass
class HullWhite(ShortRateModel):
    # params: {"kappa":..., "sigma":..., "theta": callable or float}
    def simulate_path(self, T: float, n_steps: int, rng: np.random.Generator):
        dt = T / n_steps
        kappa = self.params["kappa"]
        sigma = self.params["sigma"]
        theta = self.params.get("theta", 0.0)  # can be function of t in advanced usage
        r = np.empty(n_steps + 1)
        r[0] = self.r0
        for i in range(1, n_steps+1):
            z = rng.normal()
            dr = kappa*(theta - r[i-1])*dt + sigma * np.sqrt(dt) * z
            r[i] = r[i-1] + dr
        return r

    def zero_coupon_bond_price(self, t: float, T: float, r_t: float):
        # Hull-White one-factor analytic bond price
        kappa = self.params["kappa"]
        sigma = self.params["sigma"]
        tau = T - t
        B = (1 - np.exp(-kappa * tau)) / kappa
        # For demo we assume forward curve adjustments are zero, use simplified A:
        A = np.exp( - (sigma**2) / (4*kappa) * (B**2) * (1 - np.exp(-2*kappa*t)) )
        return A * np.exp(-B * r_t)
