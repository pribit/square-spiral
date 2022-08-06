from abc import ABC, abstractmethod
from functools import cached_property


class SpiralCommon:
    def __init__(self, spiral_number: int = 5):
        self.spiral_number: int = spiral_number

    @cached_property
    def square(self) -> int:
        return self.spiral_number ** 2


class AbstractSpiralBuilder(ABC):
    @abstractmethod
    def build(self, spiral_number: int) -> list[list[int]]:
        raise NotImplementedError
