# MiniOberon Compiler

A compiler for a subset of the Oberon programming language, developed as a semester project.

## Description

The compiler consists of the following modules:

- **Lexer/Scanner** - source code tokenization (ANTLR4)
- **Parser** - syntax analysis and parse tree construction (ANTLR4)
- **AST Builder** - conversion of parse tree to Abstract Syntax Tree
- **Semantic Analyzer** - semantic analysis (type checking, scope checking, variable existence)

## Language Features

### Data Types
- `INTEGER` - integer numbers
- `REAL` - floating-point numbers
- `STRING` - strings
- `BOOLEAN` - boolean values
- Multi-dimensional arrays (`ARRAY`)
- Records (`RECORD`)
- User-defined types (`TYPE`)

### Language Constructs
- Global and local variables
- Constants (`CONST`)
- Procedures (`PROCEDURE`) and functions (`FUNCTION`)
- Nested procedures/functions
- Parameters by value and by reference (`VAR`)
- Direct and mutual recursion
- Control structures:
  - `IF-THEN-ELSIF-ELSE-END`
  - `WHILE-DO-END`
  - `FOR-TO-BY-DO-END`
- Arithmetic operations: `+`, `-`, `*`, `/`
- Comparison operations: `=`, `#`, `<`, `<=`, `>`, `>=`

### Built-in Functions
**Output:**
- `WriteInt(x: INTEGER)` - print integer
- `WriteReal(x: REAL)` - print real number
- `WriteString(s: STRING)` - print string
- `WriteLn()` - print newline

**Input:**
- `ReadInt(): INTEGER` - read integer
- `ReadReal(): REAL` - read real number
- `ReadString(): STRING` - read string

**Type Conversions:**
- `IntToReal(x: INTEGER): REAL` - convert INTEGER → REAL
- `RealToInt(x: REAL): INTEGER` - convert REAL → INTEGER
- `IntToString(x: INTEGER): STRING` - convert INTEGER → STRING
- `RealToString(x: REAL): STRING` - convert REAL → STRING

## Installation and Setup

### Requirements
- Python 3.8+
- Java (for ANTLR4)
- ANTLR 4.13.2

### Installing Dependencies

```bash
# Install ANTLR4 runtime for Python
pip install antlr4-python3-runtime==4.13.2
```

### Parser Generation

If you modified the grammar `grammar/MiniOberon.g4`, regenerate the parser:

```bash
# Windows
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o generated grammar/MiniOberon.g4

# Linux/Mac
antlr4 -Dlanguage=Python3 -visitor -o generated grammar/MiniOberon.g4
```

## Usage

### Running Frontend on a Single File

To check syntax, build AST, and perform semantic analysis:

```bash
python -m src.frontend examples/01_basic_integer.mod
```

**Example Output:**
```
Parsing file: examples/01_basic_integer.mod

=== AST ===
{'type': 'Program',
 'module': {'type': 'Module',
            'name': 'BasicInteger',
            ...
            }}

=== Semantic analysis ===
OK: semantic analysis completed without errors.
```

### Testing All Examples

To automatically test all examples in the `examples/` folder:

```bash
python test_all_examples.py
```

**Example Output:**
```
Testing 42 example files...

[OK] 01_basic_integer.mod                     OK
[OK] 02_basic_real.mod                        OK
[OK] 03_basic_string.mod                      OK
...
[OK] 42_var_param_array.mod                   OK

======================================================================
Total: 42 | Passed: 42 | Failed: 0
```

### Viewing AST for a Specific File

For detailed AST inspection:

```bash
python -m src.frontend examples/17_function_params.mod
```

The AST will be printed in a readable format with indentation.

### Checking Syntax Only (Without Semantics)

If you need to check only syntax parsing:

```python
from src.frontend import parse_source, load_source

code = load_source("examples/01_basic_integer.mod")
ast = parse_source(code)
print(ast)
```

### Checking Semantic Analysis

To check only semantics (if AST is already built):

```python
from src.sema import SemanticAnalyzer, SemanticError
from src.frontend import parse_source, load_source

code = load_source("examples/01_basic_integer.mod")
ast = parse_source(code)

analyzer = SemanticAnalyzer()
try:
    analyzer.analyze(ast)
    print("Semantic analysis: OK")
except SemanticError as e:
    print(f"Semantic error: {e}")
```

## Project Structure

```
EBNF_Compiler/
├── grammar/
│   ├── MiniOberon.g4           # ANTLR4 grammar
│   └── minioberon.ebnf         # EBNF documentation
├── generated/                  # ANTLR4 generated files
│   ├── MiniOberonLexer.py
│   ├── MiniOberonParser.py
│   └── MiniOberonVisitor.py
├── src/
│   ├── frontend.py             # Main frontend module
│   ├── ast_builder.py          # AST construction
│   ├── sema.py                 # Semantic analysis
│   └── symtab.py               # Symbol table (auxiliary)
├── examples/                   # 42 example programs
│   ├── 01_basic_integer.mod
│   ├── 02_basic_real.mod
│   ├── ...
│   └── 42_var_param_array.mod
├── test_all_examples.py        # Testing script
└── README.md                   # This file
```

## Example Programs

The `examples/` folder contains 42 examples demonstrating all language features:

### Basic Examples (01-06)
- **01-04**: Working with basic types (INTEGER, REAL, STRING, BOOLEAN)
- **05**: Constants
- **06**: Type aliases

### Arrays (07-10)
- **07**: One-dimensional arrays
- **08**: Two-dimensional arrays
- **09**: Three-dimensional arrays
- **10**: Arrays of arrays

### Records (11-12)
- **11**: Simple records (RECORD)
- **12**: Nested records

### Procedures and Functions (13-20)
- **13-15**: Procedures (simple, with parameters, VAR parameters)
- **16-18**: Functions (simple, with parameters, different return types)
- **19-20**: Nested procedures/functions

### Control Structures (21-28)
- **21-23**: IF, IF-ELSE, IF-ELSIF-ELSE
- **24-25**: WHILE loops
- **26-28**: FOR loops (simple, with BY step, nested)

### Expressions (29-31)
- **29**: Arithmetic operations
- **30**: Comparison operations
- **31**: Complex expressions with precedence

### Working with Data (32-35)
- **32-33**: Array indexing
- **34-35**: Record field access

### Type Conversions (36-37)
- **36**: All type conversion functions
- **37**: Mixed conversions in expressions

### Recursion (38-40)
- **38**: Factorial (direct recursion)
- **39**: Fibonacci numbers (direct recursion)
- **40**: Even/odd checking (mutual recursion)

### VAR Parameters (41-42)
- **41**: Value swapping (swap)
- **42**: Passing arrays by reference

## Running Specific Examples

### Example 1: Simple Program with Variables

```bash
python -m src.frontend examples/01_basic_integer.mod
```

**Source Code (01_basic_integer.mod):**
```oberon
MODULE BasicInteger;
  VAR
    a, b, c : INTEGER;

BEGIN
  a := 10;
  b := 20;
  c := a + b;
  WriteInt(c);
  WriteLn()
END BasicInteger.
```

### Example 2: Function with Recursion

```bash
python -m src.frontend examples/38_recursion_factorial.mod
```

**Source Code (38_recursion_factorial.mod):**
```oberon
MODULE RecursionFactorial;
  FUNCTION Factorial(n : INTEGER) : INTEGER;
  BEGIN
    IF n <= 1 THEN
      RETURN 1
    ELSE
      RETURN n * Factorial(n - 1)
    END
  END Factorial;

  VAR
    result : INTEGER;

BEGIN
  result := Factorial(5);
  WriteInt(result);
  WriteLn()
END RecursionFactorial.
```

### Example 3: Working with Arrays

```bash
python -m src.frontend examples/08_array_2d.mod
```

**Source Code (08_array_2d.mod):**
```oberon
MODULE Array2D;
  VAR
    matrix : ARRAY [3, 4] OF INTEGER;
    val : INTEGER;

BEGIN
  matrix[0, 0] := 1;
  matrix[1, 2] := 42;
  val := matrix[1, 2];
  WriteInt(val);
  WriteLn()
END Array2D.
```

## Testing Project Functionality

### Quick Test

Run the test script:

```bash
python test_all_examples.py
```

If all 42 examples pass (Passed: 42 | Failed: 0), the frontend is working correctly.

### Detailed Testing

1. **Test Lexer:**
   ```bash
   python -m src.frontend examples/01_basic_integer.mod
   ```
   There should be no tokenization errors.

2. **Test Parser:**
   If the AST is printed without syntax errors - parser is working.

3. **Test Semantic Analyzer:**
   At the end you should see:
   ```
   === Semantic analysis ===
   OK: semantic analysis completed without errors.
   ```

4. **Test Error Handling:**
   Create a file with an error:
   ```oberon
   MODULE Test;
     VAR x : INTEGER;
   BEGIN
     y := 5  (* error: y is not declared *)
   END Test.
   ```

   Run:
   ```bash
   python -m src.frontend test_error.mod
   ```

   You should see an error:
   ```
   SEMANTIC ERROR: Unknown variable/constant 'y'
   ```

## Grammar

Complete grammar description is in file `grammar/minioberon.ebnf`.

ANTLR4 grammar is in file `grammar/MiniOberon.g4`.

## Comments in Code

The language supports three comment styles:

```oberon
// Single-line comment

/* Multi-line
   C-style comment */

(* Multi-line
   Oberon-style comment *)
```

## Author

Semester project for a compilers course.

## License

Educational project.
