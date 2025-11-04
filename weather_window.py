"""Compatibility shim for tests.

Tests expect a top-level `weather_window.py`. The implementation lives in
`src/weather_window.py` so re-export the function here.
"""
from src.weather_window import sliding_window_max

__all__ = ["sliding_window_max"]

if __name__ == "__main__":
    print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
