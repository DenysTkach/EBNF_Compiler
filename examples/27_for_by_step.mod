(* Example 27: FOR loop with BY step *)
MODULE ForByStep;
  VAR
    i : INTEGER;

BEGIN
  FOR i := 0 TO 10 BY 2 DO
    WriteInt(i);
    WriteLn()
  END
END ForByStep.
