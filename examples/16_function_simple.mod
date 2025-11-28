(* Example 16: Simple FUNCTION *)
MODULE FunctionSimple;
  FUNCTION GetNumber() : INTEGER;
  BEGIN
    RETURN 42
  END GetNumber;

  VAR
    x : INTEGER;

BEGIN
  x := GetNumber();
  WriteInt(x);
  WriteLn()
END FunctionSimple.
