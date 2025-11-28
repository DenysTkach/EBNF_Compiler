(* Example 17: FUNCTION with parameters *)
MODULE FunctionParams;
  FUNCTION Add(a : INTEGER; b : INTEGER) : INTEGER;
  BEGIN
    RETURN a + b
  END Add;

  VAR
    result : INTEGER;

BEGIN
  result := Add(15, 27);
  WriteInt(result);
  WriteLn()
END FunctionParams.
