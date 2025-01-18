import pytest
import numpy as np
from src.fractals.koch_snowflake import KochSnowflake

def test_koch_snowflake_initialization():
    koch = KochSnowflake(size=1.0, max_depth=5)
    assert koch.size == 1.0
    assert koch.max_depth == 5

def test_koch_snowflake_depth_validation():
    koch = KochSnowflake(max_depth=3)
    with pytest.raises(ValueError):
        koch.generate(4)

def test_koch_snowflake_points_generation():
    koch = KochSnowflake(size=1.0, max_depth=1)
    points = koch.generate(1)
    
    # For depth 1, we should have 13 points (4 segments * 3 new points + original 4 points)
    assert len(points) == 13

def test_koch_snowflake_symmetry():
    koch = KochSnowflake(size=1.0, max_depth=1)
    points = koch.generate(1)
    points_array = np.array(points)
    
    # Test symmetry around y-axis
    x_coords = points_array[:, 0]
    assert np.allclose(np.min(x_coords), -np.max(x_coords))
