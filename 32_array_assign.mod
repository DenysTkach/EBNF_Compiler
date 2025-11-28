(* Example 32: Array element assignment and access *)
MODULE ArrayAssign;
  VAR
    arr : ARRAY [10] OF INTEGER;
    i, val : INTEGER;

BEGIN
  FOR i := 0 TO 9 DO
    arr[i] := i * 2
  END;

  val := arr[5];
  WriteInt(val);
  WriteLn()
END ArrayAssign.
