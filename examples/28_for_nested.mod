(* Example 28: Nested FOR loops *)
MODULE ForNested;
  VAR
    i, j : INTEGER;

BEGIN
  FOR i := 1 TO 3 DO
    FOR j := 1 TO 2 DO
      WriteInt(i);
      WriteInt(j);
      WriteLn()
    END
  END
END ForNested.
