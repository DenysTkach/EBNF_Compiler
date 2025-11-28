(* Example 35: Array of records *)
MODULE RecordArray;
  TYPE
    Point = RECORD
      x : INTEGER;
      y : INTEGER;
    END;

  VAR
    points : ARRAY [3] OF Point;

BEGIN
  points[0].x := 1;
  points[0].y := 2;
  points[1].x := 3;
  points[1].y := 4;

  WriteInt(points[0].x);
  WriteLn();
  WriteInt(points[1].y);
  WriteLn()
END RecordArray.
