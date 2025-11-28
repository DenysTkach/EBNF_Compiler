(* Example 07: 1D Array *)
MODULE Array1D;
  VAR
    arr : ARRAY [5] OF INTEGER;
    i : INTEGER;

BEGIN
  arr[0] := 10;
  arr[1] := 20;
  arr[2] := 30;
  i := arr[1];
  WriteInt(i);
  WriteLn()
END Array1D.
