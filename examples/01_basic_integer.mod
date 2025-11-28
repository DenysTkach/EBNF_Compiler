(* Example 01: Basic INTEGER operations *)
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
