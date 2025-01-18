import numpy as np
from .base_fractal import BaseFractal  # Changed from 'from base_fractal import BaseFractal'
from typing import List, Tuple

class KochSnowflake(BaseFractal):
    """Implementation of Koch Snowflake fractal."""
    
    def __init__(self, size: float = 1.0, max_depth: int = 5):
        super().__init__(max_depth)
        self.size = size

    # Rest of the implementation remains the same
    def generate(self, depth: int) -> List[Tuple[float, float]]:
        """Generate Koch snowflake points for given depth."""
        if depth > self.max_depth:
            raise ValueError(f"Depth cannot exceed max_depth ({self.max_depth})")

        # Initialize with equilateral triangle
        h = self.size * np.sqrt(3) / 2
        base_points = [
            (0, h),
            (self.size/2, 0),
            (-self.size/2, 0),
            (0, h)
        ]
        
        self._points = self._generate_koch_points(base_points, depth)
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
                -segment[1] / 3 * np.sqrt(3) / 2,
                segment[0] / 3 * np.sqrt(3) / 2
            ])
            p5 = p3 + rotated
            
            new_points.extend([
                tuple(p1),
                tuple(p3),
                tuple(p5),
                tuple(p4)
            ])
        
        new_points.append(points[-1])
        return self._generate_koch_points(new_points, depth - 1)