(* Example 36: Type conversions *)
MODULE TypeConversion;
  VAR
    i : INTEGER;
    r : REAL;
    s : STRING;

BEGIN
  i := 42;
  r := IntToReal(i);
  WriteReal(r);
  WriteLn();

  r := 3.14159;
  i := RealToInt(r);
  WriteInt(i);
  WriteLn();

  i := 123;
  s := IntToString(i);
  WriteString(s);
  WriteLn();

  r := 2.718;
  s := RealToString(r);
  WriteString(s);
  WriteLn()
END TypeConversion.
