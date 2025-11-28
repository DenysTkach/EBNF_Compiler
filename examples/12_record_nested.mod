(* Example 12: Nested RECORD *)
MODULE RecordNested;
  TYPE
    Address = RECORD
      street : STRING;
      number : INTEGER;
    END;

    Person = RECORD
      name : STRING;
      age : INTEGER;
      addr : Address;
    END;

  VAR
    p : Person;

BEGIN
  p.name := "John";
  p.age := 30;
  p.addr.street := "Main St";
  p.addr.number := 123;
  WriteString(p.name);
  WriteLn();
  WriteInt(p.age);
  WriteLn()
END RecordNested.
