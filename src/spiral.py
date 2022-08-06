from .base import AbstractSpiralBuilder, SpiralCommon
from .builder import AlgebraSpiralBuilder


class Spiral(SpiralCommon):
    def __init__(self, spiral_number: int, builder_cls=AlgebraSpiralBuilder):
        super(Spiral, self).__init__(spiral_number)
        self._builder: AbstractSpiralBuilder = builder_cls()

    def get_spiral(self, row_divider: str = '\n', column_divider: str = '\t') -> str:
        matrix = self._builder.build(self.spiral_number)
        return row_divider.join([column_divider.join(map(str, row)) for row in matrix])

    def __str__(self):
        return f'Square spiral with side length {self.spiral_number}:\n' \
               f'{self.get_spiral()}'
