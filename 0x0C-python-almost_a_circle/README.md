# 0x0C. Python - Almost a circle

<p align="center">
  <img src="https://example.com/your_image.png" alt="Project Logo">
</p>

## Description

This project is part of the Holberton School curriculum and focuses on building a class hierarchy in Python. The goal is to create multiple classes and implement their relationships to create a program that represents a circle and performs various operations related to circles.

The project includes the following files:

- `models/base.py`: Defines the `Base` class which serves as the base class for all other classes in the project. It includes methods for JSON serialization and deserialization.
- `models/rectangle.py`: Defines the `Rectangle` class which represents a rectangle. It inherits from the `Base` class and includes methods for calculating area and displaying the rectangle.
- `models/square.py`: Defines the `Square` class which represents a square. It inherits from the `Rectangle` class and includes additional methods for calculating the square's area and displaying it.
- `models/__init__.py`: Empty file that makes the `models` directory a Python package.
- `tests/test_models/`: Directory containing test files for each class.

## Requirements

- Python 3.4 or later

## Usage

To use the classes defined in this project, follow these steps:

1. Clone the repository: `git clone https://github.com/jinDeHao/0x0C-python-almost_a_circle.git`
2. Change into the project directory: `cd 0x0C-python-almost_a_circle`
3. Import the desired classes in your Python script: `from models.rectangle import Rectangle`
4. Start using the imported classes in your code.

## Testing

To run the tests for this project, follow these steps:

1. Ensure you have the project cloned and are in the project directory.
2. Run the test file for the desired class: `python -m unittest discover tests`

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Authors

- Omar ID HMAID <o.idhmaid@gmail.com>

Feel free to contact the authors if you have any questions or suggestions.
