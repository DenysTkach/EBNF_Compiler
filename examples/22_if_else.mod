(* Example 22: IF-ELSE *)
MODULE IfElse;
  VAR
    x : INTEGER;

BEGIN
  x := 3;
  IF x > 5 THEN
    WriteString("Greater");
    WriteLn()
  ELSE
    WriteString("Not greater");
    WriteLn()
  END
END IfElse.
