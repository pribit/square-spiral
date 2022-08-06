from functools import cached_property

from src.base import SpiralCommon


class TurningPoints(SpiralCommon):

    def __init__(self, spiral_number: int):
        super(TurningPoints, self).__init__(spiral_number)
        self._current_multiplier: int = 1
        self._current_subtrahend: int = 0
        self._multiplier_step: int = 1
        self._subtrahend_step: int = 0

    @cached_property
    def turns_count(self) -> int:
        return self.spiral_number * 2 - 1

    def __next__(self):
        if self._current_multiplier > self.turns_count:
            raise StopIteration('Spiral is finished')

        next_value: int = self._current_multiplier * self.spiral_number - self._current_subtrahend

        if self._current_multiplier % 2 != 0:
            self._subtrahend_step += 1
        self._current_multiplier += self._multiplier_step

        self._current_subtrahend += self._subtrahend_step

        return next_value

    def __iter__(self):
        return self
