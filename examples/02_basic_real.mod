(* Example 02: Basic REAL operations *)
MODULE BasicReal;
  VAR
    x, y, z : REAL;

BEGIN
  x := 3.14;
  y := 2.5;
  z := x * y;
  WriteReal(z);
  WriteLn()
END BasicReal.
