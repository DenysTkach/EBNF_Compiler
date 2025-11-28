(* Example 23: IF-ELSIF-ELSE *)
MODULE IfElsif;
  VAR
    x : INTEGER;

BEGIN
  x := 5;
  IF x > 10 THEN
    WriteString("Greater than 10");
    WriteLn()
  ELSIF x > 5 THEN
    WriteString("Greater than 5");
    WriteLn()
  ELSIF x = 5 THEN
    WriteString("Equal to 5");
    WriteLn()
  ELSE
    WriteString("Less than 5");
    WriteLn()
  END
END IfElsif.
