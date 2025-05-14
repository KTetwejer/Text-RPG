# Text RPG

A simple text-based RPG game implemented in Python. The game features multiple locations, combat, inventory management, and branching choices.

## Features
- Multiple locations (dungeon, forest, river, camp, caravan, sewers, cave)
- Turn-based combat system
- Inventory and item management
- Branching story and choices
- Unit tests for core mechanics and locations

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd Text-RPG
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Game
Run the main game script (replace with the actual entry point if different):
```sh
python main.py
```

## Running Tests
To run all unit tests:

```sh
coverage run -m unittest discover -s tests
```

To see report about test:
```sh
coverage report
```

## Project Structure
- `src/` - Game source code
- `tests/` - Unit tests
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
