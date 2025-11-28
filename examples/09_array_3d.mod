(* Example 09: 3D Array *)
MODULE Array3D;
  VAR
    cube : ARRAY [2, 3, 4] OF REAL;
    x : REAL;

BEGIN
  cube[0, 1, 2] := 3.14;
  cube[1, 0, 3] := 2.71;
  x := cube[0, 1, 2];
  WriteReal(x);
  WriteLn()
END Array3D.
