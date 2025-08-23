from .base import ShortRateModel
import numpy as np
from dataclasses import dataclass

@dataclass
class HoLee(ShortRateModel):
    # params: {"sigma":...}
    # In Ho-Lee r(t) = theta(t) + sigma * W(t). For demo we assume theta constant.
    def simulate_path(self, T: float, n_steps: int, rng: np.random.Generator):
        dt = T / n_steps
        sigma = self.params["sigma"]
        theta = self.params.get("theta", 0.0)
        r = np.empty(n_steps + 1)
        r[0] = self.r0
        w = 0.0
        for i in range(1, n_steps+1):
            z = rng.normal()
            w += np.sqrt(dt) * z
            r[i] = theta + sigma * w
        return r

    def zero_coupon_bond_price(self, t: float, T: float, r_t: float):
        # Under Ho-Lee (affine), price is exp(-r_t*(T-t) + ...).
        # For simplicity we'll return an approximation using deterministic theta.
        sigma = self.params["sigma"]
        theta = self.params.get("theta", 0.0)
        tau = T - t
        # analytic A,B for Ho-Lee with constant theta:
        B = tau
        A = np.exp(-theta * tau + 0.5 * sigma**2 * tau**3 / 3.0)
        return A * np.exp(-B * r_t)
