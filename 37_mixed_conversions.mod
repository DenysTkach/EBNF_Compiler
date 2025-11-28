(* Example 37: Mixed type conversions in expressions *)
MODULE MixedConversions;
  VAR
    x : INTEGER;
    y : REAL;
    z : REAL;
    msg : STRING;

BEGIN
  x := 10;
  y := 3.5;
  z := IntToReal(x) + y;
  WriteReal(z);
  WriteLn();

  msg := "Result: ";
  WriteString(msg);
  WriteString(RealToString(z));
  WriteLn()
END MixedConversions.
