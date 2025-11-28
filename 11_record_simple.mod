(* Example 11: Simple RECORD *)
MODULE RecordSimple;
  TYPE
    Point = RECORD
      x : INTEGER;
      y : INTEGER;
    END;

  VAR
    p : Point;

BEGIN
  p.x := 10;
  p.y := 20;
  WriteInt(p.x);
  WriteLn();
  WriteInt(p.y);
  WriteLn()
END RecordSimple.
