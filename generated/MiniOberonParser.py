# Generated from grammar/MiniOberon.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,415,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,102,8,2,1,2,1,2,1,3,1,3,1,3,1,3,
        5,3,110,8,3,10,3,12,3,113,9,3,1,4,1,4,1,4,1,4,5,4,119,8,4,10,4,12,
        4,122,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,134,8,6,10,
        6,12,6,137,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,149,8,
        8,10,8,12,8,152,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        3,10,164,8,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,5,13,178,8,13,10,13,12,13,181,9,13,1,14,1,14,1,15,1,15,
        1,15,3,15,188,8,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,196,8,16,10,
        16,12,16,199,9,16,1,16,1,16,1,17,1,17,1,17,1,17,3,17,207,8,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,219,8,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,229,8,17,1,18,1,18,1,
        18,5,18,234,8,18,10,18,12,18,237,9,18,1,19,3,19,240,8,19,1,19,1,
        19,1,19,1,19,1,20,1,20,1,20,5,20,249,8,20,10,20,12,20,252,9,20,1,
        21,1,21,1,21,5,21,257,8,21,10,21,12,21,260,9,21,1,21,3,21,263,8,
        21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,271,8,22,1,23,1,23,1,23,1,
        23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,285,8,24,1,25,1,
        25,1,25,5,25,290,8,25,10,25,12,25,293,9,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,5,26,304,8,26,10,26,12,26,307,9,26,1,26,1,
        26,3,26,311,8,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,329,8,28,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,3,29,338,8,29,1,30,1,30,3,30,342,8,30,1,31,4,31,
        345,8,31,11,31,12,31,346,1,32,1,32,1,32,1,32,1,32,1,32,3,32,355,
        8,32,1,33,1,33,1,33,5,33,360,8,33,10,33,12,33,363,9,33,1,34,1,34,
        1,34,1,34,3,34,369,8,34,1,35,1,35,1,36,3,36,374,8,36,1,36,1,36,1,
        36,1,36,5,36,380,8,36,10,36,12,36,383,9,36,1,37,1,37,1,38,1,38,1,
        39,1,39,1,39,1,39,5,39,393,8,39,10,39,12,39,396,9,39,1,40,1,40,1,
        41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,3,41,409,8,41,1,42,1,
        42,1,43,1,43,1,43,0,0,44,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,0,7,1,0,26,29,1,0,42,43,4,0,3,3,10,10,50,51,
        53,54,1,0,11,12,1,0,13,14,1,0,30,31,1,0,43,44,417,0,88,1,0,0,0,2,
        91,1,0,0,0,4,98,1,0,0,0,6,111,1,0,0,0,8,114,1,0,0,0,10,125,1,0,0,
        0,12,129,1,0,0,0,14,140,1,0,0,0,16,144,1,0,0,0,18,155,1,0,0,0,20,
        163,1,0,0,0,22,165,1,0,0,0,24,167,1,0,0,0,26,174,1,0,0,0,28,182,
        1,0,0,0,30,187,1,0,0,0,32,189,1,0,0,0,34,228,1,0,0,0,36,230,1,0,
        0,0,38,239,1,0,0,0,40,245,1,0,0,0,42,253,1,0,0,0,44,270,1,0,0,0,
        46,272,1,0,0,0,48,284,1,0,0,0,50,286,1,0,0,0,52,294,1,0,0,0,54,314,
        1,0,0,0,56,320,1,0,0,0,58,337,1,0,0,0,60,339,1,0,0,0,62,344,1,0,
        0,0,64,354,1,0,0,0,66,356,1,0,0,0,68,364,1,0,0,0,70,370,1,0,0,0,
        72,373,1,0,0,0,74,384,1,0,0,0,76,386,1,0,0,0,78,388,1,0,0,0,80,397,
        1,0,0,0,82,408,1,0,0,0,84,410,1,0,0,0,86,412,1,0,0,0,88,89,3,2,1,
        0,89,90,5,0,0,1,90,1,1,0,0,0,91,92,5,15,0,0,92,93,5,42,0,0,93,94,
        5,1,0,0,94,95,3,4,2,0,95,96,5,42,0,0,96,97,5,2,0,0,97,3,1,0,0,0,
        98,101,3,6,3,0,99,100,5,19,0,0,100,102,3,42,21,0,101,99,1,0,0,0,
        101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,20,0,0,104,5,1,0,0,0,105,
        110,3,8,4,0,106,110,3,12,6,0,107,110,3,16,8,0,108,110,3,34,17,0,
        109,105,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,0,
        110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,7,1,0,0,0,113,
        111,1,0,0,0,114,115,5,16,0,0,115,120,3,10,5,0,116,117,5,1,0,0,117,
        119,3,10,5,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,
        121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,5,1,0,0,124,
        9,1,0,0,0,125,126,5,42,0,0,126,127,5,3,0,0,127,128,3,68,34,0,128,
        11,1,0,0,0,129,130,5,17,0,0,130,135,3,14,7,0,131,132,5,1,0,0,132,
        134,3,14,7,0,133,131,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,
        136,1,0,0,0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,1,0,0,139,
        13,1,0,0,0,140,141,5,42,0,0,141,142,5,3,0,0,142,143,3,20,10,0,143,
        15,1,0,0,0,144,145,5,18,0,0,145,150,3,18,9,0,146,147,5,1,0,0,147,
        149,3,18,9,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,
        151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,5,1,0,0,154,
        17,1,0,0,0,155,156,3,40,20,0,156,157,5,4,0,0,157,158,3,20,10,0,158,
        19,1,0,0,0,159,164,3,22,11,0,160,164,3,24,12,0,161,164,3,32,16,0,
        162,164,5,42,0,0,163,159,1,0,0,0,163,160,1,0,0,0,163,161,1,0,0,0,
        163,162,1,0,0,0,164,21,1,0,0,0,165,166,7,0,0,0,166,23,1,0,0,0,167,
        168,5,24,0,0,168,169,5,5,0,0,169,170,3,26,13,0,170,171,5,6,0,0,171,
        172,5,23,0,0,172,173,3,30,15,0,173,25,1,0,0,0,174,179,3,28,14,0,
        175,176,5,7,0,0,176,178,3,28,14,0,177,175,1,0,0,0,178,181,1,0,0,
        0,179,177,1,0,0,0,179,180,1,0,0,0,180,27,1,0,0,0,181,179,1,0,0,0,
        182,183,7,1,0,0,183,29,1,0,0,0,184,188,3,22,11,0,185,188,3,24,12,
        0,186,188,5,42,0,0,187,184,1,0,0,0,187,185,1,0,0,0,187,186,1,0,0,
        0,188,31,1,0,0,0,189,197,5,25,0,0,190,191,3,40,20,0,191,192,5,4,
        0,0,192,193,3,20,10,0,193,194,5,1,0,0,194,196,1,0,0,0,195,190,1,
        0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,200,1,
        0,0,0,199,197,1,0,0,0,200,201,5,20,0,0,201,33,1,0,0,0,202,203,5,
        21,0,0,203,204,5,42,0,0,204,206,5,8,0,0,205,207,3,36,18,0,206,205,
        1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,209,5,9,0,0,209,210,
        5,1,0,0,210,211,3,4,2,0,211,212,5,42,0,0,212,213,5,1,0,0,213,229,
        1,0,0,0,214,215,5,22,0,0,215,216,5,42,0,0,216,218,5,8,0,0,217,219,
        3,36,18,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,
        5,9,0,0,221,222,5,4,0,0,222,223,3,20,10,0,223,224,5,1,0,0,224,225,
        3,4,2,0,225,226,5,42,0,0,226,227,5,1,0,0,227,229,1,0,0,0,228,202,
        1,0,0,0,228,214,1,0,0,0,229,35,1,0,0,0,230,235,3,38,19,0,231,232,
        5,1,0,0,232,234,3,38,19,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,
        1,0,0,0,235,236,1,0,0,0,236,37,1,0,0,0,237,235,1,0,0,0,238,240,5,
        18,0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,242,3,
        40,20,0,242,243,5,4,0,0,243,244,3,20,10,0,244,39,1,0,0,0,245,250,
        5,42,0,0,246,247,5,7,0,0,247,249,5,42,0,0,248,246,1,0,0,0,249,252,
        1,0,0,0,250,248,1,0,0,0,250,251,1,0,0,0,251,41,1,0,0,0,252,250,1,
        0,0,0,253,258,3,44,22,0,254,255,5,1,0,0,255,257,3,44,22,0,256,254,
        1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,262,
        1,0,0,0,260,258,1,0,0,0,261,263,5,1,0,0,262,261,1,0,0,0,262,263,
        1,0,0,0,263,43,1,0,0,0,264,271,3,46,23,0,265,271,3,48,24,0,266,271,
        3,52,26,0,267,271,3,54,27,0,268,271,3,56,28,0,269,271,3,58,29,0,
        270,264,1,0,0,0,270,265,1,0,0,0,270,266,1,0,0,0,270,267,1,0,0,0,
        270,268,1,0,0,0,270,269,1,0,0,0,271,45,1,0,0,0,272,273,3,60,30,0,
        273,274,5,52,0,0,274,275,3,68,34,0,275,47,1,0,0,0,276,277,5,42,0,
        0,277,278,5,8,0,0,278,279,3,50,25,0,279,280,5,9,0,0,280,285,1,0,
        0,0,281,282,5,42,0,0,282,283,5,8,0,0,283,285,5,9,0,0,284,276,1,0,
        0,0,284,281,1,0,0,0,285,49,1,0,0,0,286,291,3,68,34,0,287,288,5,7,
        0,0,288,290,3,68,34,0,289,287,1,0,0,0,290,293,1,0,0,0,291,289,1,
        0,0,0,291,292,1,0,0,0,292,51,1,0,0,0,293,291,1,0,0,0,294,295,5,32,
        0,0,295,296,3,68,34,0,296,297,5,33,0,0,297,305,3,42,21,0,298,299,
        5,34,0,0,299,300,3,68,34,0,300,301,5,33,0,0,301,302,3,42,21,0,302,
        304,1,0,0,0,303,298,1,0,0,0,304,307,1,0,0,0,305,303,1,0,0,0,305,
        306,1,0,0,0,306,310,1,0,0,0,307,305,1,0,0,0,308,309,5,35,0,0,309,
        311,3,42,21,0,310,308,1,0,0,0,310,311,1,0,0,0,311,312,1,0,0,0,312,
        313,5,20,0,0,313,53,1,0,0,0,314,315,5,36,0,0,315,316,3,68,34,0,316,
        317,5,37,0,0,317,318,3,42,21,0,318,319,5,20,0,0,319,55,1,0,0,0,320,
        321,5,38,0,0,321,322,5,42,0,0,322,323,5,52,0,0,323,324,3,68,34,0,
        324,325,5,39,0,0,325,328,3,68,34,0,326,327,5,40,0,0,327,329,3,68,
        34,0,328,326,1,0,0,0,328,329,1,0,0,0,329,330,1,0,0,0,330,331,5,37,
        0,0,331,332,3,42,21,0,332,333,5,20,0,0,333,57,1,0,0,0,334,335,5,
        41,0,0,335,338,3,68,34,0,336,338,5,41,0,0,337,334,1,0,0,0,337,336,
        1,0,0,0,338,59,1,0,0,0,339,341,5,42,0,0,340,342,3,62,31,0,341,340,
        1,0,0,0,341,342,1,0,0,0,342,61,1,0,0,0,343,345,3,64,32,0,344,343,
        1,0,0,0,345,346,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,63,1,
        0,0,0,348,349,5,5,0,0,349,350,3,66,33,0,350,351,5,6,0,0,351,355,
        1,0,0,0,352,353,5,2,0,0,353,355,5,42,0,0,354,348,1,0,0,0,354,352,
        1,0,0,0,355,65,1,0,0,0,356,361,3,68,34,0,357,358,5,7,0,0,358,360,
        3,68,34,0,359,357,1,0,0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,362,
        1,0,0,0,362,67,1,0,0,0,363,361,1,0,0,0,364,368,3,72,36,0,365,366,
        3,70,35,0,366,367,3,72,36,0,367,369,1,0,0,0,368,365,1,0,0,0,368,
        369,1,0,0,0,369,69,1,0,0,0,370,371,7,2,0,0,371,71,1,0,0,0,372,374,
        3,74,37,0,373,372,1,0,0,0,373,374,1,0,0,0,374,375,1,0,0,0,375,381,
        3,78,39,0,376,377,3,76,38,0,377,378,3,78,39,0,378,380,1,0,0,0,379,
        376,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,0,381,382,1,0,0,0,382,
        73,1,0,0,0,383,381,1,0,0,0,384,385,7,3,0,0,385,75,1,0,0,0,386,387,
        7,3,0,0,387,77,1,0,0,0,388,394,3,82,41,0,389,390,3,80,40,0,390,391,
        3,82,41,0,391,393,1,0,0,0,392,389,1,0,0,0,393,396,1,0,0,0,394,392,
        1,0,0,0,394,395,1,0,0,0,395,79,1,0,0,0,396,394,1,0,0,0,397,398,7,
        4,0,0,398,81,1,0,0,0,399,409,3,86,43,0,400,409,5,45,0,0,401,409,
        3,84,42,0,402,409,3,48,24,0,403,409,3,60,30,0,404,405,5,8,0,0,405,
        406,3,68,34,0,406,407,5,9,0,0,407,409,1,0,0,0,408,399,1,0,0,0,408,
        400,1,0,0,0,408,401,1,0,0,0,408,402,1,0,0,0,408,403,1,0,0,0,408,
        404,1,0,0,0,409,83,1,0,0,0,410,411,7,5,0,0,411,85,1,0,0,0,412,413,
        7,6,0,0,413,87,1,0,0,0,34,101,109,111,120,135,150,163,179,187,197,
        206,218,228,235,239,250,258,262,270,284,291,305,310,328,337,341,
        346,354,361,368,373,381,394,408
    ]

class MiniOberonParser ( Parser ):

    grammarFileName = "MiniOberon.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "'='", "':'", "'['", "']'", 
                     "','", "'('", "')'", "'#'", "'+'", "'-'", "'*'", "'/'", 
                     "'MODULE'", "'CONST'", "'TYPE'", "'VAR'", "'BEGIN'", 
                     "'END'", "'PROCEDURE'", "'FUNCTION'", "'OF'", "'ARRAY'", 
                     "'RECORD'", "'INTEGER'", "'REAL'", "'STRING'", "'BOOLEAN'", 
                     "'TRUE'", "'FALSE'", "'IF'", "'THEN'", "'ELSIF'", "'ELSE'", 
                     "'WHILE'", "'DO'", "'FOR'", "'TO'", "'BY'", "'RETURN'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'<='", "'>='", "':='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MODULE", "CONST", 
                      "TYPE", "VAR", "BEGIN", "END", "PROCEDURE", "FUNCTION", 
                      "OF", "ARRAY", "RECORD", "INTEGER", "REAL", "STRING", 
                      "BOOLEAN", "TRUE", "FALSE", "IF", "THEN", "ELSIF", 
                      "ELSE", "WHILE", "DO", "FOR", "TO", "BY", "RETURN", 
                      "IDENT", "INTLIT", "REALLIT", "STRINGLIT", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "OBERON_COMMENT", "LE", "GE", "ASSIGN", 
                      "LT", "GT" ]

    RULE_program = 0
    RULE_module = 1
    RULE_block = 2
    RULE_declarations = 3
    RULE_constsec = 4
    RULE_constdecl = 5
    RULE_typesec = 6
    RULE_typedecl = 7
    RULE_varsec = 8
    RULE_vardecl = 9
    RULE_type_ = 10
    RULE_basetype = 11
    RULE_arraytype = 12
    RULE_dimlist = 13
    RULE_dimitem = 14
    RULE_elemtype = 15
    RULE_recordtype = 16
    RULE_procdecl = 17
    RULE_paramlist = 18
    RULE_param = 19
    RULE_identlist = 20
    RULE_statseq = 21
    RULE_statement = 22
    RULE_assign = 23
    RULE_call = 24
    RULE_arglist = 25
    RULE_ifstmt = 26
    RULE_whilestmt = 27
    RULE_forstmt = 28
    RULE_returnstmt = 29
    RULE_designator = 30
    RULE_selectors = 31
    RULE_selector = 32
    RULE_exprlist = 33
    RULE_expr = 34
    RULE_relop = 35
    RULE_simpleexpr = 36
    RULE_sign = 37
    RULE_addop = 38
    RULE_term = 39
    RULE_mulop = 40
    RULE_factor = 41
    RULE_boollit = 42
    RULE_number = 43

    ruleNames =  [ "program", "module", "block", "declarations", "constsec", 
                   "constdecl", "typesec", "typedecl", "varsec", "vardecl", 
                   "type_", "basetype", "arraytype", "dimlist", "dimitem", 
                   "elemtype", "recordtype", "procdecl", "paramlist", "param", 
                   "identlist", "statseq", "statement", "assign", "call", 
                   "arglist", "ifstmt", "whilestmt", "forstmt", "returnstmt", 
                   "designator", "selectors", "selector", "exprlist", "expr", 
                   "relop", "simpleexpr", "sign", "addop", "term", "mulop", 
                   "factor", "boollit", "number" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    MODULE=15
    CONST=16
    TYPE=17
    VAR=18
    BEGIN=19
    END=20
    PROCEDURE=21
    FUNCTION=22
    OF=23
    ARRAY=24
    RECORD=25
    INTEGER=26
    REAL=27
    STRING=28
    BOOLEAN=29
    TRUE=30
    FALSE=31
    IF=32
    THEN=33
    ELSIF=34
    ELSE=35
    WHILE=36
    DO=37
    FOR=38
    TO=39
    BY=40
    RETURN=41
    IDENT=42
    INTLIT=43
    REALLIT=44
    STRINGLIT=45
    WS=46
    LINE_COMMENT=47
    BLOCK_COMMENT=48
    OBERON_COMMENT=49
    LE=50
    GE=51
    ASSIGN=52
    LT=53
    GT=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module(self):
            return self.getTypedRuleContext(MiniOberonParser.ModuleContext,0)


        def EOF(self):
            return self.getToken(MiniOberonParser.EOF, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniOberonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.module()
            self.state = 89
            self.match(MiniOberonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self):
            return self.getToken(MiniOberonParser.MODULE, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniOberonParser.IDENT)
            else:
                return self.getToken(MiniOberonParser.IDENT, i)

        def block(self):
            return self.getTypedRuleContext(MiniOberonParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)




    def module(self):

        localctx = MiniOberonParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MiniOberonParser.MODULE)
            self.state = 92
            self.match(MiniOberonParser.IDENT)
            self.state = 93
            self.match(MiniOberonParser.T__0)
            self.state = 94
            self.block()
            self.state = 95
            self.match(MiniOberonParser.IDENT)
            self.state = 96
            self.match(MiniOberonParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(MiniOberonParser.DeclarationsContext,0)


        def END(self):
            return self.getToken(MiniOberonParser.END, 0)

        def BEGIN(self):
            return self.getToken(MiniOberonParser.BEGIN, 0)

        def statseq(self):
            return self.getTypedRuleContext(MiniOberonParser.StatseqContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniOberonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.declarations()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 99
                self.match(MiniOberonParser.BEGIN)
                self.state = 100
                self.statseq()


            self.state = 103
            self.match(MiniOberonParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constsec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ConstsecContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ConstsecContext,i)


        def typesec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.TypesecContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.TypesecContext,i)


        def varsec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.VarsecContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.VarsecContext,i)


        def procdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ProcdeclContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ProcdeclContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = MiniOberonParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6750208) != 0):
                self.state = 109
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16]:
                    self.state = 105
                    self.constsec()
                    pass
                elif token in [17]:
                    self.state = 106
                    self.typesec()
                    pass
                elif token in [18]:
                    self.state = 107
                    self.varsec()
                    pass
                elif token in [21, 22]:
                    self.state = 108
                    self.procdecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstsecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniOberonParser.CONST, 0)

        def constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ConstdeclContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ConstdeclContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_constsec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstsec" ):
                listener.enterConstsec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstsec" ):
                listener.exitConstsec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstsec" ):
                return visitor.visitConstsec(self)
            else:
                return visitor.visitChildren(self)




    def constsec(self):

        localctx = MiniOberonParser.ConstsecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constsec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniOberonParser.CONST)
            self.state = 115
            self.constdecl()
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.match(MiniOberonParser.T__0)
                    self.state = 117
                    self.constdecl() 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 123
            self.match(MiniOberonParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_constdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstdecl" ):
                listener.enterConstdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstdecl" ):
                listener.exitConstdecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniOberonParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(MiniOberonParser.IDENT)
            self.state = 126
            self.match(MiniOberonParser.T__2)
            self.state = 127
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniOberonParser.TYPE, 0)

        def typedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.TypedeclContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.TypedeclContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_typesec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesec" ):
                listener.enterTypesec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesec" ):
                listener.exitTypesec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypesec" ):
                return visitor.visitTypesec(self)
            else:
                return visitor.visitChildren(self)




    def typesec(self):

        localctx = MiniOberonParser.TypesecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typesec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MiniOberonParser.TYPE)
            self.state = 130
            self.typedecl()
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.match(MiniOberonParser.T__0)
                    self.state = 132
                    self.typedecl() 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 138
            self.match(MiniOberonParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniOberonParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_typedecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedecl" ):
                listener.enterTypedecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedecl" ):
                listener.exitTypedecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniOberonParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MiniOberonParser.IDENT)
            self.state = 141
            self.match(MiniOberonParser.T__2)
            self.state = 142
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniOberonParser.VAR, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.VardeclContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.VardeclContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_varsec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsec" ):
                listener.enterVarsec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsec" ):
                listener.exitVarsec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarsec" ):
                return visitor.visitVarsec(self)
            else:
                return visitor.visitChildren(self)




    def varsec(self):

        localctx = MiniOberonParser.VarsecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varsec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(MiniOberonParser.VAR)
            self.state = 145
            self.vardecl()
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 146
                    self.match(MiniOberonParser.T__0)
                    self.state = 147
                    self.vardecl() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 153
            self.match(MiniOberonParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identlist(self):
            return self.getTypedRuleContext(MiniOberonParser.IdentlistContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniOberonParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniOberonParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.identlist()
            self.state = 156
            self.match(MiniOberonParser.T__3)
            self.state = 157
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basetype(self):
            return self.getTypedRuleContext(MiniOberonParser.BasetypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MiniOberonParser.ArraytypeContext,0)


        def recordtype(self):
            return self.getTypedRuleContext(MiniOberonParser.RecordtypeContext,0)


        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniOberonParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.basetype()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.arraytype()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.recordtype()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.match(MiniOberonParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniOberonParser.INTEGER, 0)

        def REAL(self):
            return self.getToken(MiniOberonParser.REAL, 0)

        def STRING(self):
            return self.getToken(MiniOberonParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniOberonParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_basetype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasetype" ):
                listener.enterBasetype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasetype" ):
                listener.exitBasetype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasetype" ):
                return visitor.visitBasetype(self)
            else:
                return visitor.visitChildren(self)




    def basetype(self):

        localctx = MiniOberonParser.BasetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MiniOberonParser.ARRAY, 0)

        def dimlist(self):
            return self.getTypedRuleContext(MiniOberonParser.DimlistContext,0)


        def OF(self):
            return self.getToken(MiniOberonParser.OF, 0)

        def elemtype(self):
            return self.getTypedRuleContext(MiniOberonParser.ElemtypeContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_arraytype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraytype" ):
                listener.enterArraytype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraytype" ):
                listener.exitArraytype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniOberonParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MiniOberonParser.ARRAY)
            self.state = 168
            self.match(MiniOberonParser.T__4)
            self.state = 169
            self.dimlist()
            self.state = 170
            self.match(MiniOberonParser.T__5)
            self.state = 171
            self.match(MiniOberonParser.OF)
            self.state = 172
            self.elemtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.DimitemContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.DimitemContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_dimlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimlist" ):
                listener.enterDimlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimlist" ):
                listener.exitDimlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimlist" ):
                return visitor.visitDimlist(self)
            else:
                return visitor.visitChildren(self)




    def dimlist(self):

        localctx = MiniOberonParser.DimlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dimlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.dimitem()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 175
                self.match(MiniOberonParser.T__6)
                self.state = 176
                self.dimitem()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimitemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def INTLIT(self):
            return self.getToken(MiniOberonParser.INTLIT, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_dimitem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimitem" ):
                listener.enterDimitem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimitem" ):
                listener.exitDimitem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimitem" ):
                return visitor.visitDimitem(self)
            else:
                return visitor.visitChildren(self)




    def dimitem(self):

        localctx = MiniOberonParser.DimitemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dimitem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==42 or _la==43):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basetype(self):
            return self.getTypedRuleContext(MiniOberonParser.BasetypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MiniOberonParser.ArraytypeContext,0)


        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_elemtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElemtype" ):
                listener.enterElemtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElemtype" ):
                listener.exitElemtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElemtype" ):
                return visitor.visitElemtype(self)
            else:
                return visitor.visitChildren(self)




    def elemtype(self):

        localctx = MiniOberonParser.ElemtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elemtype)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.basetype()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.arraytype()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(MiniOberonParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecordtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RECORD(self):
            return self.getToken(MiniOberonParser.RECORD, 0)

        def END(self):
            return self.getToken(MiniOberonParser.END, 0)

        def identlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.IdentlistContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.IdentlistContext,i)


        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.Type_Context)
            else:
                return self.getTypedRuleContext(MiniOberonParser.Type_Context,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_recordtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecordtype" ):
                listener.enterRecordtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecordtype" ):
                listener.exitRecordtype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordtype" ):
                return visitor.visitRecordtype(self)
            else:
                return visitor.visitChildren(self)




    def recordtype(self):

        localctx = MiniOberonParser.RecordtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_recordtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniOberonParser.RECORD)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 190
                self.identlist()
                self.state = 191
                self.match(MiniOberonParser.T__3)
                self.state = 192
                self.type_()
                self.state = 193
                self.match(MiniOberonParser.T__0)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(MiniOberonParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(MiniOberonParser.PROCEDURE, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniOberonParser.IDENT)
            else:
                return self.getToken(MiniOberonParser.IDENT, i)

        def block(self):
            return self.getTypedRuleContext(MiniOberonParser.BlockContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniOberonParser.ParamlistContext,0)


        def FUNCTION(self):
            return self.getToken(MiniOberonParser.FUNCTION, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniOberonParser.Type_Context,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_procdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcdecl" ):
                listener.enterProcdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcdecl" ):
                listener.exitProcdecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcdecl" ):
                return visitor.visitProcdecl(self)
            else:
                return visitor.visitChildren(self)




    def procdecl(self):

        localctx = MiniOberonParser.ProcdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_procdecl)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(MiniOberonParser.PROCEDURE)
                self.state = 203
                self.match(MiniOberonParser.IDENT)
                self.state = 204
                self.match(MiniOberonParser.T__7)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18 or _la==42:
                    self.state = 205
                    self.paramlist()


                self.state = 208
                self.match(MiniOberonParser.T__8)
                self.state = 209
                self.match(MiniOberonParser.T__0)
                self.state = 210
                self.block()
                self.state = 211
                self.match(MiniOberonParser.IDENT)
                self.state = 212
                self.match(MiniOberonParser.T__0)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(MiniOberonParser.FUNCTION)
                self.state = 215
                self.match(MiniOberonParser.IDENT)
                self.state = 216
                self.match(MiniOberonParser.T__7)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18 or _la==42:
                    self.state = 217
                    self.paramlist()


                self.state = 220
                self.match(MiniOberonParser.T__8)
                self.state = 221
                self.match(MiniOberonParser.T__3)
                self.state = 222
                self.type_()
                self.state = 223
                self.match(MiniOberonParser.T__0)
                self.state = 224
                self.block()
                self.state = 225
                self.match(MiniOberonParser.IDENT)
                self.state = 226
                self.match(MiniOberonParser.T__0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_paramlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamlist" ):
                listener.enterParamlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamlist" ):
                listener.exitParamlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniOberonParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.param()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 231
                self.match(MiniOberonParser.T__0)
                self.state = 232
                self.param()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identlist(self):
            return self.getTypedRuleContext(MiniOberonParser.IdentlistContext,0)


        def type_(self):
            return self.getTypedRuleContext(MiniOberonParser.Type_Context,0)


        def VAR(self):
            return self.getToken(MiniOberonParser.VAR, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniOberonParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 238
                self.match(MiniOberonParser.VAR)


            self.state = 241
            self.identlist()
            self.state = 242
            self.match(MiniOberonParser.T__3)
            self.state = 243
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniOberonParser.IDENT)
            else:
                return self.getToken(MiniOberonParser.IDENT, i)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_identlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentlist" ):
                listener.enterIdentlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentlist" ):
                listener.exitIdentlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentlist" ):
                return visitor.visitIdentlist(self)
            else:
                return visitor.visitChildren(self)




    def identlist(self):

        localctx = MiniOberonParser.IdentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_identlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniOberonParser.IDENT)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 246
                self.match(MiniOberonParser.T__6)
                self.state = 247
                self.match(MiniOberonParser.IDENT)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatseqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_statseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatseq" ):
                listener.enterStatseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatseq" ):
                listener.exitStatseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatseq" ):
                return visitor.visitStatseq(self)
            else:
                return visitor.visitChildren(self)




    def statseq(self):

        localctx = MiniOberonParser.StatseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statseq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.statement()
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 254
                    self.match(MiniOberonParser.T__0)
                    self.state = 255
                    self.statement() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 261
                self.match(MiniOberonParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MiniOberonParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(MiniOberonParser.CallContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniOberonParser.IfstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MiniOberonParser.WhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniOberonParser.ForstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniOberonParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniOberonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.whilestmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 269
                self.returnstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def designator(self):
            return self.getTypedRuleContext(MiniOberonParser.DesignatorContext,0)


        def ASSIGN(self):
            return self.getToken(MiniOberonParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MiniOberonParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.designator()
            self.state = 273
            self.match(MiniOberonParser.ASSIGN)
            self.state = 274
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniOberonParser.ArglistContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = MiniOberonParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(MiniOberonParser.IDENT)
                self.state = 277
                self.match(MiniOberonParser.T__7)
                self.state = 278
                self.arglist()
                self.state = 279
                self.match(MiniOberonParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(MiniOberonParser.IDENT)
                self.state = 282
                self.match(MiniOberonParser.T__7)
                self.state = 283
                self.match(MiniOberonParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = MiniOberonParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 287
                self.match(MiniOberonParser.T__6)
                self.state = 288
                self.expr()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniOberonParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ExprContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniOberonParser.THEN)
            else:
                return self.getToken(MiniOberonParser.THEN, i)

        def statseq(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.StatseqContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.StatseqContext,i)


        def END(self):
            return self.getToken(MiniOberonParser.END, 0)

        def ELSIF(self, i:int=None):
            if i is None:
                return self.getTokens(MiniOberonParser.ELSIF)
            else:
                return self.getToken(MiniOberonParser.ELSIF, i)

        def ELSE(self):
            return self.getToken(MiniOberonParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniOberonParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MiniOberonParser.IF)
            self.state = 295
            self.expr()
            self.state = 296
            self.match(MiniOberonParser.THEN)
            self.state = 297
            self.statseq()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 298
                self.match(MiniOberonParser.ELSIF)
                self.state = 299
                self.expr()
                self.state = 300
                self.match(MiniOberonParser.THEN)
                self.state = 301
                self.statseq()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 308
                self.match(MiniOberonParser.ELSE)
                self.state = 309
                self.statseq()


            self.state = 312
            self.match(MiniOberonParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniOberonParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprContext,0)


        def DO(self):
            return self.getToken(MiniOberonParser.DO, 0)

        def statseq(self):
            return self.getTypedRuleContext(MiniOberonParser.StatseqContext,0)


        def END(self):
            return self.getToken(MiniOberonParser.END, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_whilestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestmt" ):
                listener.enterWhilestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestmt" ):
                listener.exitWhilestmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MiniOberonParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MiniOberonParser.WHILE)
            self.state = 315
            self.expr()
            self.state = 316
            self.match(MiniOberonParser.DO)
            self.state = 317
            self.statseq()
            self.state = 318
            self.match(MiniOberonParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniOberonParser.FOR, 0)

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def ASSIGN(self):
            return self.getToken(MiniOberonParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ExprContext,i)


        def TO(self):
            return self.getToken(MiniOberonParser.TO, 0)

        def DO(self):
            return self.getToken(MiniOberonParser.DO, 0)

        def statseq(self):
            return self.getTypedRuleContext(MiniOberonParser.StatseqContext,0)


        def END(self):
            return self.getToken(MiniOberonParser.END, 0)

        def BY(self):
            return self.getToken(MiniOberonParser.BY, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_forstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForstmt" ):
                listener.enterForstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForstmt" ):
                listener.exitForstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniOberonParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MiniOberonParser.FOR)
            self.state = 321
            self.match(MiniOberonParser.IDENT)
            self.state = 322
            self.match(MiniOberonParser.ASSIGN)
            self.state = 323
            self.expr()
            self.state = 324
            self.match(MiniOberonParser.TO)
            self.state = 325
            self.expr()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 326
                self.match(MiniOberonParser.BY)
                self.state = 327
                self.expr()


            self.state = 330
            self.match(MiniOberonParser.DO)
            self.state = 331
            self.statseq()
            self.state = 332
            self.match(MiniOberonParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniOberonParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_returnstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstmt" ):
                listener.enterReturnstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstmt" ):
                listener.exitReturnstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniOberonParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnstmt)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(MiniOberonParser.RETURN)
                self.state = 335
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(MiniOberonParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesignatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def selectors(self):
            return self.getTypedRuleContext(MiniOberonParser.SelectorsContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_designator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesignator" ):
                listener.enterDesignator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesignator" ):
                listener.exitDesignator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesignator" ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = MiniOberonParser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_designator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MiniOberonParser.IDENT)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2 or _la==5:
                self.state = 340
                self.selectors()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selector(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.SelectorContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.SelectorContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_selectors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectors" ):
                listener.enterSelectors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectors" ):
                listener.exitSelectors(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectors" ):
                return visitor.visitSelectors(self)
            else:
                return visitor.visitChildren(self)




    def selectors(self):

        localctx = MiniOberonParser.SelectorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_selectors)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 343
                self.selector()
                self.state = 346 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprlistContext,0)


        def IDENT(self):
            return self.getToken(MiniOberonParser.IDENT, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_selector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelector" ):
                listener.enterSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelector" ):
                listener.exitSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelector" ):
                return visitor.visitSelector(self)
            else:
                return visitor.visitChildren(self)




    def selector(self):

        localctx = MiniOberonParser.SelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_selector)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(MiniOberonParser.T__4)
                self.state = 349
                self.exprlist()
                self.state = 350
                self.match(MiniOberonParser.T__5)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(MiniOberonParser.T__1)
                self.state = 353
                self.match(MiniOberonParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_exprlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprlist" ):
                listener.enterExprlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprlist" ):
                listener.exitExprlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MiniOberonParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 357
                self.match(MiniOberonParser.T__6)
                self.state = 358
                self.expr()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.SimpleexprContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.SimpleexprContext,i)


        def relop(self):
            return self.getTypedRuleContext(MiniOberonParser.RelopContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniOberonParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.simpleexpr()
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30399297484751880) != 0):
                self.state = 365
                self.relop()
                self.state = 366
                self.simpleexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(MiniOberonParser.LT, 0)

        def LE(self):
            return self.getToken(MiniOberonParser.LE, 0)

        def GT(self):
            return self.getToken(MiniOberonParser.GT, 0)

        def GE(self):
            return self.getToken(MiniOberonParser.GE, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = MiniOberonParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30399297484751880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.TermContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.TermContext,i)


        def sign(self):
            return self.getTypedRuleContext(MiniOberonParser.SignContext,0)


        def addop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.AddopContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.AddopContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_simpleexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleexpr" ):
                listener.enterSimpleexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleexpr" ):
                listener.exitSimpleexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleexpr" ):
                return visitor.visitSimpleexpr(self)
            else:
                return visitor.visitChildren(self)




    def simpleexpr(self):

        localctx = MiniOberonParser.SimpleexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_simpleexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==12:
                self.state = 372
                self.sign()


            self.state = 375
            self.term()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 376
                self.addop()
                self.state = 377
                self.term()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniOberonParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = MiniOberonParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniOberonParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddop" ):
                return visitor.visitAddop(self)
            else:
                return visitor.visitChildren(self)




    def addop(self):

        localctx = MiniOberonParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.FactorContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.FactorContext,i)


        def mulop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniOberonParser.MulopContext)
            else:
                return self.getTypedRuleContext(MiniOberonParser.MulopContext,i)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniOberonParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.factor()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 389
                self.mulop()
                self.state = 390
                self.factor()
                self.state = 396
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniOberonParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulop" ):
                return visitor.visitMulop(self)
            else:
                return visitor.visitChildren(self)




    def mulop(self):

        localctx = MiniOberonParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(MiniOberonParser.NumberContext,0)


        def STRINGLIT(self):
            return self.getToken(MiniOberonParser.STRINGLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(MiniOberonParser.BoollitContext,0)


        def call(self):
            return self.getTypedRuleContext(MiniOberonParser.CallContext,0)


        def designator(self):
            return self.getTypedRuleContext(MiniOberonParser.DesignatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniOberonParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniOberonParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MiniOberonParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_factor)
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.match(MiniOberonParser.STRINGLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.boollit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 403
                self.designator()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 404
                self.match(MiniOberonParser.T__7)
                self.state = 405
                self.expr()
                self.state = 406
                self.match(MiniOberonParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MiniOberonParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniOberonParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_boollit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoollit" ):
                listener.enterBoollit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoollit" ):
                listener.exitBoollit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = MiniOberonParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not(_la==30 or _la==31):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REALLIT(self):
            return self.getToken(MiniOberonParser.REALLIT, 0)

        def INTLIT(self):
            return self.getToken(MiniOberonParser.INTLIT, 0)

        def getRuleIndex(self):
            return MiniOberonParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = MiniOberonParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





