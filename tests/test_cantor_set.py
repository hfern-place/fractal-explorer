import pytest
import numpy as np
from src.fractals.cantor_set import CantorSet

def test_cantor_initialization():
    cantor = CantorSet(size=1.0, max_depth=5, spacing=0.2)
    assert cantor.size == 1.0
    assert cantor.max_depth == 5
    assert cantor.spacing == 0.2

def test_cantor_depth_validation():
    cantor = CantorSet(max_depth=3)
    with pytest.raises(ValueError):
        cantor.generate(4)

def test_cantor_points_generation():
    cantor = CantorSet(size=1.0, max_depth=1)
    points = cantor.generate(1)
    
    # For depth 1, we should have 9 points (2 segments * 3 points each + 3 None separators)
    assert len(points) == 9

def test_cantor_symmetry():
    cantor = CantorSet(size=1.0, max_depth=1)
    points = cantor.generate(1)
    points_array = np.array([p for p in points if p[0] is not None])
    
    # Test symmetry around y-axis
    x_coords = points_array[:, 0]
    assert np.allclose(np.min(x_coords), -np.max(x_coords))