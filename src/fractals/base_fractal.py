from abc import ABC, abstractmethod
import numpy as np
from typing import List, Tuple

class BaseFractal(ABC):
    """
    Abstract base class for all fractal implementations.
    Following Single Responsibility and Open/Closed principles.
    """
    def __init__(self, max_depth: int = 10):  # Updated from 5 to 10
        self.max_depth = max_depth
        self._points: List[Tuple[float, float]] = []

    @abstractmethod
    def generate(self, depth: int) -> List[Tuple[float, float]]:
        """Generate the fractal points for given depth."""
        pass

    @property
    def points(self) -> List[Tuple[float, float]]:
        """Get the current fractal points."""
        return self._points

    def set_max_depth(self, depth: int) -> None:
        """Set maximum iteration depth."""
        if depth < 0:
            raise ValueError("Depth must be non-negative")
        self.max_depth = depth