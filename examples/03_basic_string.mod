(* Example 03: Basic STRING operations *)
MODULE BasicString;
  VAR
    s1, s2 : STRING;

BEGIN
  s1 := "Hello";
  s2 := "World";
  WriteString(s1);
  WriteString(s2);
  WriteLn()
END BasicString.
