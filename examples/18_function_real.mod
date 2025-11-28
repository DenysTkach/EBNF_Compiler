(* Example 18: FUNCTION returning REAL *)
MODULE FunctionReal;
  FUNCTION Multiply(x : REAL; y : REAL) : REAL;
  BEGIN
    RETURN x * y
  END Multiply;

  VAR
    res : REAL;

BEGIN
  res := Multiply(3.5, 2.0);
  WriteReal(res);
  WriteLn()
END FunctionReal.
