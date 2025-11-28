(* Example 40: Mutual recursion - Even/Odd *)
MODULE MutualRecursion;
  FUNCTION IsEven(n : INTEGER) : BOOLEAN;
  BEGIN
    IF n = 0 THEN
      RETURN TRUE
    ELSE
      RETURN IsOdd(n - 1)
    END
  END IsEven;

  FUNCTION IsOdd(n : INTEGER) : BOOLEAN;
  BEGIN
    IF n = 0 THEN
      RETURN FALSE
    ELSE
      RETURN IsEven(n - 1)
    END
  END IsOdd;

  VAR
    result : BOOLEAN;

BEGIN
  result := IsEven(4);
  IF result THEN
    WriteString("4 is even");
    WriteLn()
  END;

  result := IsOdd(5);
  IF result THEN
    WriteString("5 is odd");
    WriteLn()
  END
END MutualRecursion.
