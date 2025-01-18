import pytest
import numpy as np
from src.fractals.sierpinski_triangle import SierpinskiTriangle

def test_sierpinski_initialization():
    sierpinski = SierpinskiTriangle(size=1.0, max_depth=5)
    assert sierpinski.size == 1.0
    assert sierpinski.max_depth == 5

def test_sierpinski_depth_validation():
    sierpinski = SierpinskiTriangle(max_depth=3)
    with pytest.raises(ValueError):
        sierpinski.generate(4)

def test_sierpinski_points_generation():
    sierpinski = SierpinskiTriangle(size=1.0, max_depth=1)
    points = sierpinski.generate(1)
    
    # For depth 1, we should have 12 points (3 triangles * 4 points each)
    assert len(points) == 12

def test_sierpinski_symmetry():
    sierpinski = SierpinskiTriangle(size=1.0, max_depth=1)
    points = sierpinski.generate(1)
    points_array = np.array(points)
    
    # Test symmetry around y-axis
    x_coords = points_array[:, 0]
    assert np.allclose(np.min(x_coords), -np.max(x_coords))