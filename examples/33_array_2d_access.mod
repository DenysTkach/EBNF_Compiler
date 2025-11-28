(* Example 33: 2D array element access *)
MODULE Array2DAccess;
  VAR
    matrix : ARRAY [3, 3] OF INTEGER;
    i, j : INTEGER;

BEGIN
  FOR i := 0 TO 2 DO
    FOR j := 0 TO 2 DO
      matrix[i, j] := i + j
    END
  END;

  WriteInt(matrix[1, 2]);
  WriteLn();
  WriteInt(matrix[2, 1]);
  WriteLn()
END Array2DAccess.
