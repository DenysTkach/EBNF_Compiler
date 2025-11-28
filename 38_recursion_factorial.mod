(* Example 38: Direct recursion - Factorial *)
MODULE RecursionFactorial;
  FUNCTION Factorial(n : INTEGER) : INTEGER;
  BEGIN
    IF n <= 1 THEN
      RETURN 1
    ELSE
      RETURN n * Factorial(n - 1)
    END
  END Factorial;

  VAR
    result : INTEGER;

BEGIN
  result := Factorial(5);
  WriteInt(result);
  WriteLn()
END RecursionFactorial.
