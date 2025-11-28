(* Example 08: 2D Array *)
MODULE Array2D;
  VAR
    matrix : ARRAY [3, 4] OF INTEGER;
    val : INTEGER;

BEGIN
  matrix[0, 0] := 1;
  matrix[1, 2] := 42;
  val := matrix[1, 2];
  WriteInt(val);
  WriteLn()
END Array2D.
