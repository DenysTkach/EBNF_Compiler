(* Example 21: Simple IF *)
MODULE IfSimple;
  VAR
    x : INTEGER;

BEGIN
  x := 10;
  IF x > 5 THEN
    WriteString("x is greater than 5");
    WriteLn()
  END
END IfSimple.
