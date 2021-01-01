from typing import Any

class NamedValue:
    def __init__(self,name: str,value: Any):
        self._name = name
        self._value = value
    def get_name(self) -> str:
        return self._name
    def get_value(self) -> Any:
        return self._value
    def to_string(self) -> str:
        return f"NamedValue(name = {repr(self.get_name())} , value = {repr(self.get_value())})"
    def __repr__(self) -> str:
        return self.to_string()
    def __str__(self) -> str:
        return self.to_string()

def ensure_value(value_or_namedvalue: Any):
    if type(value_or_namedvalue) == NamedValue:
# If the parameter is a NamedValue instance return the value inside the instance.
        return value_or_namedvalue.get_value()
# If the parameter is a value, return the parameter itself.
    return value_or_namedvalue

