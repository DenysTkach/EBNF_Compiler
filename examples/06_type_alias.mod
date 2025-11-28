(* Example 06: Type declarations (aliases) *)
MODULE TypeAlias;
  TYPE
    Counter = INTEGER;
    Distance = REAL;
    Message = STRING;

  VAR
    cnt : Counter;
    dist : Distance;
    msg : Message;

BEGIN
  cnt := 42;
  dist := 12.5;
  msg := "Test";
  WriteInt(cnt);
  WriteLn()
END TypeAlias.
