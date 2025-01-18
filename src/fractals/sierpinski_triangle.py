import numpy as np
from .base_fractal import BaseFractal
from typing import List, Tuple

class SierpinskiTriangle(BaseFractal):
    """Implementation of Sierpiński Triangle fractal."""
    
    def __init__(self, size: float = 1.0, max_depth: int = 5):
        super().__init__(max_depth)
        self.size = size

    def generate(self, depth: int) -> List[Tuple[float, float]]:
        """Generate Sierpiński triangle points for given depth."""
        if depth > self.max_depth:
            raise ValueError(f"Depth cannot exceed max_depth ({self.max_depth})")

        # Initialize with base triangle
        h = self.size * np.sqrt(3) / 2
        vertices = [
            (0, h),  # top
            (self.size/2, 0),  # bottom right
            (-self.size/2, 0)  # bottom left
        ]
        
        self._points = []
        self._generate_sierpinski(vertices, depth)
        return self._points

    def _generate_sierpinski(self, vertices: List[Tuple[float, float]], depth: int) -> None:
        """Recursively generate Sierpiński triangle points."""
        if depth == 0:
            self._points.extend(vertices + [vertices[0]])  # Close the triangle
            return

        # Calculate midpoints
        v1, v2, v3 = vertices
        m1 = self._midpoint(v1, v2)
        m2 = self._midpoint(v2, v3)
        m3 = self._midpoint(v3, v1)

        # Recursively generate three smaller triangles
        self._generate_sierpinski([v1, m1, m3], depth - 1)
        self._generate_sierpinski([m1, v2, m2], depth - 1)
        self._generate_sierpinski([m3, m2, v3], depth - 1)

    @staticmethod
    def _midpoint(p1: Tuple[float, float], p2: Tuple[float, float]) -> Tuple[float, float]:
        """Calculate the midpoint between two points."""
        return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)