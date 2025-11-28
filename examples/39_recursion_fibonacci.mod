(* Example 39: Direct recursion - Fibonacci *)
MODULE RecursionFibonacci;
  FUNCTION Fib(n : INTEGER) : INTEGER;
  BEGIN
    IF n <= 1 THEN
      RETURN n
    ELSE
      RETURN Fib(n - 1) + Fib(n - 2)
    END
  END Fib;

  VAR
    i, result : INTEGER;

BEGIN
  FOR i := 0 TO 6 DO
    result := Fib(i);
    WriteInt(result);
    WriteLn()
  END
END RecursionFibonacci.
