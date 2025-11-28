(* Example 34: Record field access *)
MODULE RecordFieldAccess;
  TYPE
    Person = RECORD
      age : INTEGER;
      salary : REAL;
      name : STRING;
    END;

  VAR
    p : Person;

BEGIN
  p.age := 25;
  p.salary := 50000.0;
  p.name := "Alice";

  WriteString(p.name);
  WriteLn();
  WriteInt(p.age);
  WriteLn();
  WriteReal(p.salary);
  WriteLn()
END RecordFieldAccess.
