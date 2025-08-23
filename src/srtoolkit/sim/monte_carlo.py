from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, List, Dict, Any
import numpy as np

def _simulate_single(model, T, n_steps, seed):
    rng = np.random.default_rng(seed)
    return model.simulate_path(T=T, n_steps=n_steps, rng=rng)

def parallel_simulate(model, n_paths: int, T: float, n_steps: int, n_workers: int = 4):
    """
    Simulate multiple paths in parallel using ThreadPoolExecutor.
    Returns numpy array shape (n_paths, n_steps+1).
    """
    seeds = np.random.SeedSequence().spawn(n_paths)
    results = [None] * n_paths
    with ThreadPoolExecutor(max_workers=n_workers) as ex:
        futures = {ex.submit(_simulate_single, model, T, n_steps, s.entropy): i for i,s in enumerate(seeds)}
        for f in as_completed(futures):
            idx = futures[f]
            results[idx] = f.result()
    return np.vstack(results)

def monte_carlo_price_zero_coupon(model, n_paths:int, T:float, n_steps:int, discount_step_index:int = None, n_workers:int = 4):
    """
    Monte Carlo estimate of P(0,T) by averaging exp(-integral r dt).
    discount_step_index: if None, integral is approximated with trapezoid; else use full path.
    """
    paths = parallel_simulate(model, n_paths=n_paths, T=T, n_steps=n_steps, n_workers=n_workers)
    dt = T / n_steps
    # integrate r(t) approximated by sum r_i * dt (left Riemann)
    integral = (paths[:,:-1].sum(axis=1)) * dt
    discounts = np.exp(-integral)
    price = discounts.mean()
    stderr = discounts.std(ddof=1) / np.sqrt(n_paths)
    return price, stderr
