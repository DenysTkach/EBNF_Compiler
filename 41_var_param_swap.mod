(* Example 41: VAR parameters - Swap *)
MODULE VarParamSwap;
  PROCEDURE Swap(VAR a : INTEGER; VAR b : INTEGER);
    VAR
      temp : INTEGER;
  BEGIN
    temp := a;
    a := b;
    b := temp
  END Swap;

  VAR
    x, y : INTEGER;

BEGIN
  x := 10;
  y := 20;
  WriteInt(x);
  WriteLn();
  WriteInt(y);
  WriteLn();

  Swap(x, y);

  WriteInt(x);
  WriteLn();
  WriteInt(y);
  WriteLn()
END VarParamSwap.
