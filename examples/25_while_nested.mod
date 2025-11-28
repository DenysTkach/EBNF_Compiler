(* Example 25: Nested WHILE loops *)
MODULE WhileNested;
  VAR
    i, j : INTEGER;

BEGIN
  i := 0;
  WHILE i < 3 DO
    j := 0;
    WHILE j < 2 DO
      WriteInt(i);
      WriteInt(j);
      WriteLn();
      j := j + 1
    END;
    i := i + 1
  END
END WhileNested.
