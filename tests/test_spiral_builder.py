import pytest

from src.base import AbstractSpiralBuilder
from src.builder import AlgebraSpiralBuilder, ConditionalSpiralBuilder


@pytest.mark.parametrize(
    'spiral_number, spiral_matrix',
    (
        pytest.param(
            1,
            1,
            id='spiral_number_equals_1'
        ),
        pytest.param(
            2,
            2,
            id='spiral_number_equals_2'
        ),
        pytest.param(
            3,
            3,
            id='spiral_number_equals_3'
        ),
        pytest.param(
            5,
            5,
            id='spiral_number_equals_5'
        ),
        pytest.param(
            6,
            6,
            id='spiral_number_equals_8'
        ),
    ),
    indirect=['spiral_matrix'],
)
@pytest.mark.parametrize(
    'builder',
    (
        ConditionalSpiralBuilder(),
        AlgebraSpiralBuilder(),
    )
)
def test_spiral_builders(spiral_number: int, builder: AbstractSpiralBuilder, spiral_matrix: list[list[int]]):
    assert builder.build(spiral_number) == spiral_matrix
