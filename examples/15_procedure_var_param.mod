(* Example 15: PROCEDURE with VAR parameter *)
MODULE ProcedureVarParam;
  PROCEDURE Increment(VAR x : INTEGER);
  BEGIN
    x := x + 1
  END Increment;

  VAR
    n : INTEGER;

BEGIN
  n := 5;
  Increment(n);
  WriteInt(n);
  WriteLn()
END ProcedureVarParam.
