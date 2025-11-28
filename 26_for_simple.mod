(* Example 26: Simple FOR loop *)
MODULE ForSimple;
  VAR
    i : INTEGER;

BEGIN
  FOR i := 1 TO 5 DO
    WriteInt(i);
    WriteLn()
  END
END ForSimple.
