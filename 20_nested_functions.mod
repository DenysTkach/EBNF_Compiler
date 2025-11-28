(* Example 20: Nested functions *)
MODULE NestedFunctions;
  FUNCTION Outer(x : INTEGER) : INTEGER;
    FUNCTION Inner(y : INTEGER) : INTEGER;
    BEGIN
      RETURN y + 10
    END Inner;

  BEGIN
    RETURN Inner(x) + 5
  END Outer;

  VAR
    result : INTEGER;

BEGIN
  result := Outer(3);
  WriteInt(result);
  WriteLn()
END NestedFunctions.
