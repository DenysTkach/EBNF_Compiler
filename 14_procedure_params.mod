(* Example 14: PROCEDURE with parameters *)
MODULE ProcedureParams;
  PROCEDURE PrintSum(a : INTEGER; b : INTEGER);
    VAR
      sum : INTEGER;
  BEGIN
    sum := a + b;
    WriteInt(sum);
    WriteLn()
  END PrintSum;

BEGIN
  PrintSum(10, 20)
END ProcedureParams.
