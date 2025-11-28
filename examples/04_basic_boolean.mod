(* Example 04: Basic BOOLEAN operations *)
MODULE BasicBoolean;
  VAR
    flag1, flag2 : BOOLEAN;

BEGIN
  flag1 := TRUE;
  flag2 := FALSE;
  IF flag1 THEN
    WriteString("Flag1 is true");
    WriteLn()
  END
END BasicBoolean.
