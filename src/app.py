import streamlit as st
import numpy as np
import plotly.graph_objects as go
from fractals.koch_snowflake import KochSnowflake
from fractals.sierpinski_triangle import SierpinskiTriangle
from fractals.cantor_set import CantorSet

def plot_connected_points(points, title):
    """
    Create a Plotly figure for fractals with connected points.
    
    Args:
        points (List[Tuple[float, float]]): List of (x, y) coordinates
        title (str): Title of the plot
        
    Returns:
        go.Figure: Plotly figure object
    """
    x_coords, y_coords = zip(*points)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='lines',
        line=dict(color='blue', width=2),
        name=title
    ))
    
    fig.update_layout(
        title=title,
        showlegend=False,
        width=800,
        height=800,
        xaxis=dict(
            scaleanchor="y",
            scaleratio=1,
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray'
        ),
        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray'
        ),
        plot_bgcolor='white',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    return fig

def plot_cantor_set(points, title):
    """
    Create a Plotly figure for the Cantor set.
    
    Args:
        points (List[Tuple[float, float]]): List of (x, y) coordinates with None values for breaks
        title (str): Title of the plot
        
    Returns:
        go.Figure: Plotly figure object
    """
    x_coords, y_coords = zip(*points)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='lines',
        line=dict(color='blue', width=2),
        name=title,
        connectgaps=False  # Don't connect across None values
    ))
    
    fig.update_layout(
        title=title,
        showlegend=False,
        width=800,
        height=400,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray',
            autorange='reversed'  # Invert y-axis for better visualization
        ),
        plot_bgcolor='white',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    return fig

def main():
    st.title("Fractal Explorer")
    st.write("Explore the fascinating world of mathematical fractals!")

    # Sidebar controls
    with st.sidebar:
        st.header("Controls")
        
        fractal_type = st.selectbox(
            "Select Fractal",
            ["Koch Snowflake", "Sierpiński Triangle", "Cantor Set"]
        )
        
        # Help text for fractal selection
        fractal_descriptions = {
            "Koch Snowflake": "A snowflake-like shape that grows by adding triangular bumps to each line segment.",
            "Sierpiński Triangle": "A triangular pattern that emerges by repeatedly removing center triangles.",
            "Cantor Set": "A set created by repeatedly removing the middle third of line segments."
        }
        st.info(fractal_descriptions[fractal_type])
        
        # Iteration depth with explanation
        st.subheader("Iteration Controls")
        depth = st.slider(
            "Iteration Depth",
            min_value=0,
            max_value=7,
            value=2,
            help="""Higher iterations create more detailed patterns:
            - 0-2: Basic shape forms
            - 3-4: Pattern becomes clear
            - 5-7: Fine details emerge"""
        )
        
        # Size control with explanation
        size = st.slider(
            "Size",
            min_value=0.1,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="""Adjusts the overall size of the fractal:
            - Smaller values: More compact visualization
            - Larger values: Expanded visualization
            Does not affect the fractal's mathematical properties."""
        )

        # Cantor Set specific controls
        spacing = None
        if fractal_type == "Cantor Set":
            st.subheader("Cantor Set Options")
            spacing = st.slider(
                "Vertical Spacing",
                min_value=0.1,
                max_value=0.5,
                value=0.2,
                step=0.1,
                help="""Controls the vertical distance between iteration levels:
                - Smaller values: More compact visualization
                - Larger values: More spread out visualization"""
            )

    # Use tabs for better layout separation
    tab1, tab2 = st.tabs(["Fractal Visualization", "Learn More About Fractals"])
    
    with tab1:
        # Generate and display fractal
        try:
            if fractal_type == "Koch Snowflake":
                fractal = KochSnowflake(size=size, max_depth=7)
                points = fractal.generate(depth)
                fig = plot_connected_points(points, "Koch Snowflake")
                
            elif fractal_type == "Sierpiński Triangle":
                fractal = SierpinskiTriangle(size=size, max_depth=7)
                points = fractal.generate(depth)
                fig = plot_connected_points(points, "Sierpiński Triangle")
                
            else:  # Cantor Set
                fractal = CantorSet(size=size, max_depth=7, spacing=spacing)
                points = fractal.generate(depth)
                fig = plot_cantor_set(points, "Cantor Set")
                
            st.plotly_chart(fig)

        except Exception as e:
            st.error(f"An error occurred while generating the fractal: {str(e)}")

    with tab2:
        # Educational content
        st.subheader("Educational Content")
        st.write("""
        Fractals are geometric shapes that exhibit self-similarity at different scales. 
        This means that zooming in on a part of the fractal reveals a pattern similar 
        to the whole shape.
        
        **Key Mathematical Properties:**
        1. **Self-Similarity**: Parts of the shape are similar to the whole
        2. **Infinite Detail**: The pattern continues infinitely when zooming in
        3. **Fractional Dimension**: Often has a dimension that's not a whole number
        4. **Iterative Process**: Created by repeating a simple rule
        """)

        if fractal_type == "Koch Snowflake":
            st.write("""
            **Koch Snowflake Properties:**
            - Starts with an equilateral triangle
            - Each iteration adds triangular bumps to every line segment
            - Has infinite perimeter but finite area
            - Each iteration increases perimeter by 4/3
            - Dimension ≈ 1.262
            """)
        elif fractal_type == "Sierpiński Triangle":
            st.write("""
            **Sierpiński Triangle Properties:**
            - Starts with a single triangle
            - Each iteration removes central triangles
            - Area approaches zero as iterations increase
            - Maintains perfect symmetry
            - Dimension ≈ 1.585
            """)
        else:
            st.write("""
            **Cantor Set Properties:**
            - Starts with a line segment
            - Each iteration removes middle thirds
            - Has zero total length but uncountably many points
            - Demonstrates self-similarity at every scale
            - Dimension ≈ 0.631
            """)


# def main():
#     st.title("Fractal Explorer")
#     st.write("Explore the fascinating world of mathematical fractals!")

#     # Sidebar controls
#     with st.sidebar:
#         st.header("Controls")
        
#         fractal_type = st.selectbox(
#             "Select Fractal",
#             ["Koch Snowflake", "Sierpiński Triangle", "Cantor Set"]
#         )
        
#         # Help text for fractal selection
#         fractal_descriptions = {
#             "Koch Snowflake": "A snowflake-like shape that grows by adding triangular bumps to each line segment.",
#             "Sierpiński Triangle": "A triangular pattern that emerges by repeatedly removing center triangles.",
#             "Cantor Set": "A set created by repeatedly removing the middle third of line segments."
#         }
#         st.info(fractal_descriptions[fractal_type])
        
#         # Iteration depth with explanation
#         st.subheader("Iteration Controls")
#         depth = st.slider(
#             "Iteration Depth",
#             min_value=0,
#             max_value=7,
#             value=2,
#             help="""Higher iterations create more detailed patterns:
#             - 0-2: Basic shape forms
#             - 3-4: Pattern becomes clear
#             - 5-7: Fine details emerge"""
#         )
        
#         # Size control with explanation
#         size = st.slider(
#             "Size",
#             min_value=0.1,
#             max_value=2.0,
#             value=1.0,
#             step=0.1,
#             help="""Adjusts the overall size of the fractal:
#             - Smaller values: More compact visualization
#             - Larger values: Expanded visualization
#             Does not affect the fractal's mathematical properties."""
#         )

#         # Cantor Set specific controls
#         spacing = None
#         if fractal_type == "Cantor Set":
#             st.subheader("Cantor Set Options")
#             spacing = st.slider(
#                 "Vertical Spacing",
#                 min_value=0.1,
#                 max_value=0.5,
#                 value=0.2,
#                 step=0.1,
#                 help="""Controls the vertical distance between iteration levels:
#                 - Smaller values: More compact visualization
#                 - Larger values: More spread out visualization"""
#             )

#     # Main area
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         # Generate and display fractal
#         try:
#             if fractal_type == "Koch Snowflake":
#                 fractal = KochSnowflake(size=size, max_depth=7)
#                 points = fractal.generate(depth)
#                 fig = plot_connected_points(points, "Koch Snowflake")
                
#             elif fractal_type == "Sierpiński Triangle":
#                 fractal = SierpinskiTriangle(size=size, max_depth=7)
#                 points = fractal.generate(depth)
#                 fig = plot_connected_points(points, "Sierpiński Triangle")
                
#             else:  # Cantor Set
#                 fractal = CantorSet(size=size, max_depth=7, spacing=spacing)
#                 points = fractal.generate(depth)
#                 fig = plot_cantor_set(points, "Cantor Set")
                
#             st.plotly_chart(fig)

#         except Exception as e:
#             st.error(f"An error occurred while generating the fractal: {str(e)}")

#     with col2:
#         st.subheader("Current Settings Effect")
        
#         # Display iteration effects
#         st.write("**Iteration Depth Impact**")
#         if depth <= 2:
#             st.write("At low iterations, you're seeing the basic building blocks of the fractal pattern.")
#         elif depth <= 4:
#             st.write("The characteristic fractal pattern is now clearly visible, showing self-similarity.")
#         else:
#             st.write("Fine details are emerging, demonstrating the fractal's infinite complexity.")

#         # Display size effects
#         st.write("**Size Impact**")
#         if size < 0.5:
#             st.write("The small size provides a compact view, good for seeing the overall pattern.")
#         elif size <= 1.5:
#             st.write("This medium size offers a balanced view of both structure and detail.")
#         else:
#             st.write("The large size helps examine fine details but may show fewer complete iterations.")

#         # Display fractal-specific effects
#         if fractal_type == "Koch Snowflake":
#             num_segments = 4 ** depth
#             st.write("**Current Properties**")
#             st.write(f"- Number of line segments: {num_segments:,}")
#             st.write(f"- Relative perimeter length: {(4/3)**depth:.2f}x original")
            
#         elif fractal_type == "Sierpiński Triangle":
#             num_triangles = 3 ** depth
#             st.write("**Current Properties**")
#             st.write(f"- Number of triangles: {num_triangles:,}")
#             st.write(f"- Area ratio: {(3/4)**depth:.4f} of original")
            
#         else:  # Cantor Set
#             num_segments = 2 ** depth
#             st.write("**Current Properties**")
#             st.write(f"- Number of segments: {num_segments:,}")
#             st.write(f"- Total length: {(2/3)**depth:.4f} of original")
#             if spacing:
#                 st.write("**Spacing Effect**")
#                 if spacing < 0.2:
#                     st.write("Compact vertical spacing helps see overall pattern.")
#                 elif spacing < 0.4:
#                     st.write("Medium spacing provides good balance of readability.")
#                 else:
#                     st.write("Large spacing emphasizes individual iteration levels.")

#     # Educational content
#     with st.expander("Learn More About Fractals"):
#         st.write("""
#         Fractals are geometric shapes that exhibit self-similarity at different scales. 
#         This means that zooming in on a part of the fractal reveals a pattern similar 
#         to the whole shape.
        
#         **Key Mathematical Properties:**
#         1. **Self-Similarity**: Parts of the shape are similar to the whole
#         2. **Infinite Detail**: The pattern continues infinitely when zooming in
#         3. **Fractional Dimension**: Often has a dimension that's not a whole number
#         4. **Iterative Process**: Created by repeating a simple rule
#         """)
        
#         if fractal_type == "Koch Snowflake":
#             st.write("""
#             **Koch Snowflake Properties:**
#             - Starts with an equilateral triangle
#             - Each iteration adds triangular bumps to every line segment
#             - Has infinite perimeter but finite area
#             - Each iteration increases perimeter by 4/3
#             - Dimension ≈ 1.262
#             """)
#         elif fractal_type == "Sierpiński Triangle":
#             st.write("""
#             **Sierpiński Triangle Properties:**
#             - Starts with a single triangle
#             - Each iteration removes central triangles
#             - Area approaches zero as iterations increase
#             - Maintains perfect symmetry
#             - Dimension ≈ 1.585
#             """)
#         else:
#             st.write("""
#             **Cantor Set Properties:**
#             - Starts with a line segment
#             - Each iteration removes middle thirds
#             - Has zero total length but uncountably many points
#             - Demonstrates self-similarity at every scale
#             - Dimension ≈ 0.631
#             """)

if __name__ == "__main__":
    main()