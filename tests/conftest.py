import pytest


@pytest.fixture(scope='session')
def spiral_matrix(request) -> list[list[int]]:
    match request.param:
        case 1:
            return [
                [1],
            ]
        case 2:
            return [
                [1, 2],
                [4, 3],
            ]
        case 3:
            return [
                [1, 2, 3],
                [8, 9, 4],
                [7, 6, 5],
            ]
        case 5:
            return [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ]
        case 6:
            return [
                [1, 2, 3, 4, 5, 6],
                [20, 21, 22, 23, 24, 7],
                [19, 32, 33, 34, 25, 8],
                [18, 31, 36, 35, 26, 9],
                [17, 30, 29, 28, 27, 10],
                [16, 15, 14, 13, 12, 11],
            ]


@pytest.fixture(scope='session')
def spiral(spiral_matrix) -> str:
    # TODO: make this fixture use spiral_matrix right
    return '\n'.join(['\t'.join(map(str, row)) for row in spiral_matrix])
