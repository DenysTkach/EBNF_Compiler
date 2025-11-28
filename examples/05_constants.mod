(* Example 05: Constants *)
MODULE Constants;
  CONST
    MaxValue = 100;
    Pi = 3.14159;
    AppName = "MyApp";
    IsDebug = TRUE;

  VAR
    x : INTEGER;

BEGIN
  x := MaxValue;
  WriteString(AppName);
  WriteLn();
  WriteInt(x);
  WriteLn()
END Constants.
