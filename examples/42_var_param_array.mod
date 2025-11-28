(* Example 42: VAR parameters with arrays *)
MODULE VarParamArray;
  PROCEDURE FillArray(VAR arr : ARRAY [5] OF INTEGER; value : INTEGER);
    VAR
      i : INTEGER;
  BEGIN
    FOR i := 0 TO 4 DO
      arr[i] := value
    END
  END FillArray;

  VAR
    myArray : ARRAY [5] OF INTEGER;
    i : INTEGER;

BEGIN
  FillArray(myArray, 7);

  FOR i := 0 TO 4 DO
    WriteInt(myArray[i]);
    WriteLn()
  END
END VarParamArray.
