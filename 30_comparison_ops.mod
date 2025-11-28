(* Example 30: Comparison operations *)
MODULE ComparisonOps;
  VAR
    x, y : INTEGER;
    result : BOOLEAN;

BEGIN
  x := 10;
  y := 20;

  result := x < y;
  IF result THEN
    WriteString("x < y");
    WriteLn()
  END;

  result := x = y;
  IF result THEN
    WriteString("x = y");
    WriteLn()
  ELSE
    WriteString("x # y");
    WriteLn()
  END;

  result := x <= y;
  IF result THEN
    WriteString("x <= y");
    WriteLn()
  END
END ComparisonOps.
