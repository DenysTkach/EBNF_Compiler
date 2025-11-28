(* Example 13: Simple PROCEDURE *)
MODULE ProcedureSimple;
  PROCEDURE Greet();
  BEGIN
    WriteString("Hello from procedure");
    WriteLn()
  END Greet;

BEGIN
  Greet()
END ProcedureSimple.
