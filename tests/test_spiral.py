import pytest

from src.spiral import Spiral


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
    indirect=['spiral_matrix']
)
def test_spiral(spiral_number: int, spiral_matrix: list[list[int]]):
    assert Spiral(spiral_number).get_spiral() == '\n'.join(['\t'.join(map(str, row)) for row in spiral_matrix])
