from typing import Any


class Shape:
    def __init__(self, center = 8, out_color = 'black'):
        self._center = center
        self.__out_color = out_color

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

