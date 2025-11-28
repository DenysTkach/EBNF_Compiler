# src/symtab.py
# Простая таблица символов и представление типов для MiniOberon.

from dataclasses import dataclass
from typing import Optional, Dict, Any


# -------------------- Типы --------------------

@dataclass
class Type:
    """Очень простое представление типов."""
    kind: str               # 'base', 'array', 'record'
    name: Optional[str] = None      # для базовых и именных типов
    elem: Optional['Type'] = None   # для массивов: тип элемента
    dims: Optional[list] = None     # список размерностей (пока просто храним)
    fields: Optional[Dict[str, 'Type']] = None  # для record


def base_type(name: str) -> Type:
    return Type(kind="base", name=name)


# Базовые типы, которые есть в языке
INT_TYPE = base_type("INTEGER")
REAL_TYPE = base_type("REAL")
STRING_TYPE = base_type("STRING")


# -------------------- Символы --------------------

@dataclass
class Symbol:
    name: str
    kind: str         # 'var', 'const', 'type', 'func', 'proc', 'param'
    type: Optional[Type] = None
    extra: Optional[dict] = None   # сюда можно складывать доп.инфу (параметры, byref и т.п.)


# -------------------- Scope --------------------

class Scope:
    def __init__(self, name: str, parent: Optional['Scope'] = None):
        self.name = name
        self.parent = parent
        self.symbols: Dict[str, Symbol] = {}

    def define(self, sym: Symbol):
        """Добавить символ в текущий scope. Если имя уже есть — ошибка."""
        if sym.name in self.symbols:
            raise KeyError(f"Symbol '{sym.name}' already defined in scope '{self.name}'")
        self.symbols[sym.name] = sym

    def lookup(self, name: str) -> Optional[Symbol]:
        """Поиск символа по имени вверх по цепочке scope-ов."""
        if name in self.symbols:
            return self.symbols[name]
        if self.parent is not None:
            return self.parent.lookup(name)
        return None

    def __repr__(self):
        return f"<Scope {self.name}: {list(self.symbols.keys())}>"
