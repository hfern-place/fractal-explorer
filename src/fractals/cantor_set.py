import numpy as np
from .base_fractal import BaseFractal
from typing import List, Tuple

class CantorSet(BaseFractal):
    """Implementation of Cantor Set fractal."""
    
    def __init__(self, size: float = 1.0, max_depth: int = 5, spacing: float = 0.2):
        super().__init__(max_depth)
        self.size = size
        self.spacing = spacing  # Vertical spacing between levels

    def generate(self, depth: int) -> List[Tuple[float, float]]:
        """Generate Cantor set points for given depth."""
        if depth > self.max_depth:
            raise ValueError(f"Depth cannot exceed max_depth ({self.max_depth})")

        self._points = []
        self._generate_cantor(-self.size/2, self.size/2, 0, depth)
        return self._points

    def _generate_cantor(self, left: float, right: float, level: int, depth: int) -> None:
        """Recursively generate Cantor set points."""
        if depth < 0:
            return

        # Add current line segment
        y = -level * self.spacing
        self._points.extend([
            (left, y),
            (right, y),
            (None, None)  # Break in the line
        ])

        # Calculate positions for next iteration
        segment_length = (right - left) / 3
        
        # Recursively generate left and right segments
        self._generate_cantor(left, left + segment_length, level + 1, depth - 1)
        self._generate_cantor(right - segment_length, right, level + 1, depth - 1)