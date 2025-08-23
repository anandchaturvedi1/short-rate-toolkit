from dataclasses import dataclass
from typing import Dict, Any
import numpy as np

@dataclass
class ShortRateModel:
    """Base abstract class for short-rate models."""
    r0: float  # initial short rate
    params: Dict[str, Any]

    @classmethod
    def from_dict(cls, r0: float, params: Dict[str, Any]):
        return cls(r0=r0, params=params)

    def simulate_path(self, T: float, n_steps: int, rng: np.random.Generator):
        """Simulate one path --- concrete implementations override."""
        raise NotImplementedError

    def zero_coupon_bond_price(self, t: float, T: float, r_t: float):
        """Price P(t,T) given current short rate r_t."""
        raise NotImplementedError
