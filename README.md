# Outerplanar Approximation (STS Algorithm)

A Python package implementing a **7/10-approximation** algorithm for finding maximum outerplanar subgraphs using the STS approach described in [An Improved Algorithm for Finding Maximum Outerplanar (arXiv:2306.05588)](https://arxiv.org/abs/2306.05588).

## Features

- **Phase 1**: Greedy triangular-cactus extraction  
- **Phase 2**: Greedy induced 4-cycle (square) addition  
- **Phase 3**: Stitch residual components with single edges  
- **Command-line interface** for end-to-end processing of edge-lists

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/outerplanar_approx.git
cd outerplanar_approx
pip install -e .
```

Or, once published to PyPI:

```bash
pip install outerplanar-approx
```

## Usage

### As a Python Module

```python
import networkx as nx
from outerplanar_approx import extract_cactus, add_squares, stitch_edges

# Read input graph
G = nx.read_edgelist("input.edgelist")

# Phase 1: Extract the triangular-cactus
C = extract_cactus(G)

# Phase 2: Add induced squares
S = add_squares(G, C)

# Phase 3: Stitch components
R = stitch_edges(G, S)

# Write output to file
nx.write_edgelist(R, "output.edgelist", data=False)
```

### Command-Line Interface

```bash
# If console script is configured:
outerplanar-approx input.edgelist output.edgelist

# Or directly via the module
python -m outerplanar_approx.utils input.edgelist output.edgelist
```

## Testing

```bash
pip install pytest
pytest -q
```

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
