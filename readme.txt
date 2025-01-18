# Fractal Explorer

An interactive web application for exploring and learning about mathematical fractals, built with Python and Streamlit.

## Features

- Interactive visualization of classic fractals:
  - Koch Snowflake
  - Sierpiński Triangle
  - Cantor Set
- Adjustable parameters (iteration depth, size)
- Educational content about fractal properties
- Real-time visualization updates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hfern-place/fractal-explorer.git
cd fractal-explorer
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run src/app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Project Structure

- `src/`: Source code
  - `fractals/`: Fractal implementations
  - `utils/`: Utility functions
  - `app.py`: Streamlit application
- `tests/`: Unit tests
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Development

### Running Tests

```bash
pytest tests/
```

### Adding New Fractals

1. Create a new class in `src/fractals/` that inherits from `BaseFractal`
2. Implement the required `generate()` method
3. Add corresponding unit tests
4. Update the UI in `app.py` to include the new fractal

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
