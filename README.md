# miniparser
miniparser is a simple and lightweight yet highly efficient expression engine in Python. It's designed for scenarios where you need fast, reliable evaluation of mathematical, logical, or custom expressions without the overhead of a full scripting language.

Key Features:

⚡ Minimal Footprint: No external dependencies, ensuring a quick and easy install.

🚀 High Performance: Optimized for speed, making it suitable for high-throughput applications.

📝 Clear Syntax: Supports standard arithmetic, logical operators, and custom functions/variables.

🔒 Safe Execution: Provides a secure way to evaluate user-defined logic.

Perfect for configuration files, simple rule engines, or dynamic calculations.

# Supported Syntax
### Values
- Decimal
- Octal
- Hexadecimal
- Binary
### Operators
The current supported operators are:
- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)
- exponent (^)
- modulo (%)
### Variables
Variables name are supported. The current standard is any letters and the '_' character.

For example:
- x
- _abc
- x_x
- ABC