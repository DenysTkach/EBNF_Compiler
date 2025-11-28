(* Example 31: Complex expressions *)
MODULE ComplexExpr;
  VAR
    a, b, c, result : INTEGER;

BEGIN
  a := 5;
  b := 3;
  c := 2;
  result := a + b * c;
  WriteInt(result);
  WriteLn();
  result := (a + b) * c;
  WriteInt(result);
  WriteLn()
END ComplexExpr.
