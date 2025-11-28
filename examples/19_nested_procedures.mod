(* Example 19: Nested procedures *)
MODULE NestedProcedures;
  VAR
    global : INTEGER;

  PROCEDURE Outer();
    VAR
      local : INTEGER;

    PROCEDURE Inner();
    BEGIN
      local := 10;
      global := 20
    END Inner;

  BEGIN
    local := 5;
    Inner();
    WriteInt(local);
    WriteLn()
  END Outer;

BEGIN
  global := 0;
  Outer();
  WriteInt(global);
  WriteLn()
END NestedProcedures.
