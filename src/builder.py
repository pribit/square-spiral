from src.base import AbstractSpiralBuilder
from src.turning_points import TurningPoints


class ConditionalSpiralBuilder(AbstractSpiralBuilder):
    def build(self, spiral_number: int) -> list[list[int]]:
        matrix: list[list[int | None]] = [[None] * spiral_number for _ in range(spiral_number)]
        x, y = 0, 0
        dx, dy = 1, 0
        a, b = 1, 0

        for number in range(1, spiral_number ** 2 + 1):
            matrix[y][x] = number
            x += dx
            y += dy
            if (
                x == spiral_number - a and y == b
                or y == spiral_number - a and x == spiral_number - a
                or x == b and y == spiral_number - a
                or x == b and y == a
            ):
                dx, dy = -dy, dx
            if x == b and y == a:
                a += 1
                b += 1

        return matrix


class AlgebraSpiralBuilder(AbstractSpiralBuilder):
    def build(self, spiral_number: int) -> list[list[int]]:
        matrix: list[list[int | None]] = [[None] * spiral_number for _ in range(spiral_number)]
        turning_points: TurningPoints = TurningPoints(spiral_number)
        x, y = 0, 0
        dx, dy = 1, 0
        next_turning_point: int = next(turning_points)

        for number in range(1, spiral_number ** 2 + 1):
            matrix[y][x] = number
            if number == next_turning_point:
                dx, dy = -dy, dx
                try:
                    next_turning_point = next(turning_points)
                except StopIteration:
                    pass
            x += dx
            y += dy

        return matrix
