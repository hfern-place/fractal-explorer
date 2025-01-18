import numpy as np
from src.fractals.koch_snowflake import KochSnowflake


def test_koch_snowflake_points_generation():
    koch = KochSnowflake(size=1.0, max_depth=1)
    points = koch.generate(1)

    # Ensure points are generated
    assert len(points) > 0, "No points were generated"


def test_koch_snowflake_symmetry():
    koch = KochSnowflake(size=1.0, max_depth=1)
    points = koch.generate(1)

    # Ensure points are generated
    assert len(points) > 0, "No points were generated"

    # Define a tolerance for floating-point comparison
    tolerance = 1e-6

    # Convert to array for processing
    points_array = np.array(points)

    # Round points for consistent comparisons
    points_set = {tuple(np.round(p, 6)) for p in points_array}

    # Check if each point has a mirrored counterpart
    missing_points = []
    for x, y in points_set:
        if abs(x) > tolerance:  # Skip points on the y-axis
            mirrored = tuple(np.round((-x, y), 6))
            mirrored_y = tuple(np.round((x, -y), 6))
            if mirrored not in points_set and mirrored_y not in points_set:
                missing_points.append((x, y))
                print(f"Missing mirrored point for {mirrored} and {mirrored_y}")

    # Assert that all points have their mirrors
    assert not missing_points, f"Missing mirrored points: {missing_points}"
