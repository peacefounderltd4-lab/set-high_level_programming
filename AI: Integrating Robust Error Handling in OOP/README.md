# AI: Integrating Robust Error Handling in OOP

## Overview
This task demonstrates the integration of robust data validation and exception handling into an Object-Oriented Python application using Gemini Code Assist scaffolding.

## Structure
- `initial_code.py`: Unvalidated implementation of the `Product` and `InventoryManager` classes.
- `refactored_code.py`: Enhanced implementation incorporating `@property` decorators, custom exception handling, and validation tests.

## Key Concepts Applied
1. **Encapsulation**: Protected internal attributes (`_price`, `_quantity`) behind `@property` setters.
2. **Data Integrity**: Enforced non-negative numeric domain constraints on prices and quantities.
3. **Custom Exceptions**: Implemented `InvalidProductDataError` for precise error signaling during illegal operations.
4. 
