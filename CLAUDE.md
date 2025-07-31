# Development Instructions

## Python Dependency Management

This project uses `uv` for Python dependency management. Always use `uv` to manage dependencies:

```bash
# Sync dependencies (preferred)
uv sync

# Run scripts
uv run python script.py

# Add new dependencies
uv add package_name

# For development dependencies
uv add --dev package_name
```

Note: Use `uv sync` instead of `uv pip install` when possible.

## Testing

When testing the napari-broadcastable-points functionality:

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_broadcast_slicing.py

# Run with verbose output
uv run pytest -v

# Run specific test
uv run pytest tests/test_broadcast_slicing.py::TestBroadcastablePointsSlicing::test_data_insertion
```

The test suite includes comprehensive non-GUI tests for:
- Data insertion and broadcast dimension handling
- Slicing behavior verification
- Comparison with regular Points layer
- Edge cases (empty data, no broadcast dims, etc.)
- Various broadcast dimension combinations