import numpy as np
from .base_fractal import BaseFractal
from typing import List, Tuple


class KochSnowflake(BaseFractal):
    """Implementation of Koch Snowflake fractal."""

    def __init__(self, size: float = 1.0, max_depth: int = 5):
        super().__init__(max_depth)
        self.size = size

    def generate(self, depth: int) -> List[Tuple[float, float]]:
        """Generate Koch snowflake points for given depth."""
        if depth > self.max_depth:
            raise ValueError(f"Depth cannot exceed max_depth ({self.max_depth})")

        # Initialize with an equilateral triangle
        h = self.size * np.sqrt(3) / 2
        base_points = [
            (-self.size / 2, 0),  # Bottom-left
            (self.size / 2, 0),   # Bottom-right
            (0, h),               # Top
            (-self.size / 2, 0)   # Close the triangle
        ]

        # Generate Koch points recursively
        self._points = self._generate_koch_points(base_points, depth)

        # Round points for consistent output
        self._points = [(round(x, 6), round(y, 6)) for x, y in self._points]

        return self._points

    def _generate_koch_points(self, points: List[Tuple[float, float]], depth: int) -> List[Tuple[float, float]]:
        """Recursively generate Koch curve points."""
        if depth == 0:
            return points

        new_points = []
        for i in range(len(points) - 1):
            p1 = np.array(points[i])
            p2 = np.array(points[i + 1])

            # Calculate segment points
            segment = p2 - p1
            p3 = p1 + segment / 3
            p4 = p1 + 2 * segment / 3

            # Calculate peak point
            rotated = np.array([
                -segment[1] * np.sqrt(3) / 6,
                segment[0] * np.sqrt(3) / 6
            ])
            p5 = p3 + rotated

            # Add new points
            new_points.extend([
                tuple(np.round(p1, 6)),
                tuple(np.round(p3, 6)),
                tuple(np.round(p5, 6)),
                tuple(np.round(p4, 6))
            ])

        new_points.append(tuple(np.round(points[-1], 6)))  # Append the last point
        return self._generate_koch_points(new_points, depth - 1)
