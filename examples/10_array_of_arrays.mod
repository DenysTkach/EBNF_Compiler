(* Example 10: Array of arrays *)
MODULE ArrayOfArrays;
  TYPE
    Row = ARRAY [5] OF INTEGER;
    Matrix = ARRAY [3] OF Row;

  VAR
    m : Matrix;
    val : INTEGER;

BEGIN
  m[0][1] := 99;
  val := m[0][1];
  WriteInt(val);
  WriteLn()
END ArrayOfArrays.
