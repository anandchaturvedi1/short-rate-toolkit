from .base import ShortRateModel
import numpy as np
from dataclasses import dataclass

@dataclass
class CIR(ShortRateModel):
    # params: {"kappa":..., "theta":..., "sigma":...}
    def simulate_path(self, T: float, n_steps: int, rng: np.random.Generator):
        dt = T / n_steps
        kappa = self.params["kappa"]
        theta = self.params["theta"]
        sigma = self.params["sigma"]
        r = np.empty(n_steps + 1)
        r[0] = max(self.r0, 0.0)
        for i in range(1, n_steps + 1):
            z = rng.normal()
            # full truncation Euler-Maruyama to keep positivity approximately
            dr = kappa * (theta - r[i-1]) * dt + sigma * np.sqrt(max(r[i-1],0))*np.sqrt(dt) * z
            r[i] = max(r[i-1] + dr, 0.0)
        return r

    def zero_coupon_bond_price(self, t: float, T: float, r_t: float):
        # Using closed form for CIR (Cox-Ingersoll-Ross) bond price
        kappa = self.params["kappa"]
        theta = self.params["theta"]
        sigma = self.params["sigma"]
        tau = T - t
        gamma = np.sqrt(kappa**2 + 2 * sigma**2)
        denom = (gamma + kappa) * (np.exp(gamma * tau) - 1) + 2 * gamma
        B = 2 * (np.exp(gamma * tau) - 1) / denom
        A = ( (2*gamma*np.exp((kappa+gamma)*tau/2)) / denom ) ** (2 * kappa * theta / sigma**2)
        return A * np.exp(-B * r_t)
