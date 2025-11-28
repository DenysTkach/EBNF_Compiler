(* Example 29: Arithmetic operations *)
MODULE ArithmeticOps;
  VAR
    a, b, sum, diff, prod, quot : INTEGER;

BEGIN
  a := 20;
  b := 5;
  sum := a + b;
  diff := a - b;
  prod := a * b;
  quot := a / b;
  WriteInt(sum);
  WriteLn();
  WriteInt(diff);
  WriteLn();
  WriteInt(prod);
  WriteLn();
  WriteInt(quot);
  WriteLn()
END ArithmeticOps.
