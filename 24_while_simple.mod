(* Example 24: Simple WHILE loop *)
MODULE WhileSimple;
  VAR
    i : INTEGER;

BEGIN
  i := 0;
  WHILE i < 5 DO
    WriteInt(i);
    WriteLn();
    i := i + 1
  END
END WhileSimple.
