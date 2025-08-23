from .base import ShortRateModel
import numpy as np
from dataclasses import dataclass
from typing import Dict

@dataclass
class Vasicek(ShortRateModel):
    # params: {"kappa":..., "theta":..., "sigma":...}
    def simulate_path(self, T: float, n_steps: int, rng: np.random.Generator):
        dt = T / n_steps
        kappa = self.params["kappa"]
        theta = self.params["theta"]
        sigma = self.params["sigma"]
        r = np.empty(n_steps + 1)
        r[0] = self.r0
        for i in range(1, n_steps + 1):
            z = rng.normal()
            dr = kappa * (theta - r[i-1]) * dt + sigma * np.sqrt(dt) * z
            r[i] = r[i-1] + dr
        return r

    def zero_coupon_bond_price(self, t: float, T: float, r_t: float):
        # Analytical Vasicek bond price P(t,T) = A(t,T) exp(-B(t,T) r_t)
        kappa = self.params["kappa"]
        theta = self.params["theta"]
        sigma = self.params["sigma"]
        tau = T - t
        if kappa == 0:
            B = tau
            A = np.exp( -theta * tau + 0.5 * sigma**2 * tau**3 / 3.0 )
        else:
            B = (1 - np.exp(-kappa * tau)) / kappa
            A = np.exp(
                (theta - (sigma**2)/(2*kappa**2))*(B - tau) - (sigma**2)*(B**2)/(4*kappa)
            )
        return A * np.exp(-B * r_t)
