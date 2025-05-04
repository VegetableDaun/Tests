from contextlib import nullcontext

import pytest

from app.file_1 import square, Calculator


@pytest.mark.parametrize(
    "x, y",
    [
        (1, 1),
        (2, 4),
        (-2, 4),
        (0, 0),
        (3., 9.)
    ]
)
def test_square(x, y):
    assert square(x) == y


class TestCalculator:
    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (3, 1, 3, nullcontext()),
            (3, 2, 1.5, nullcontext()),
            (1.5, 3, 0.5, nullcontext()),
            (3, 0, 0, pytest.raises(ZeroDivisionError)),
            (3, 2.0, 1.5, nullcontext()),
            ('6', 1, 0, pytest.raises(TypeError)),
            (6, '2', 0, pytest.raises(TypeError)),
            ('6', '2', 0, pytest.raises(TypeError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (1, 1, 2, nullcontext()),
            (1, -1, 0, nullcontext()),
            ('1', '1', 0, pytest.raises(TypeError)),
            ('1', 1, 0, pytest.raises(TypeError)),
            (1, '2', 0, pytest.raises(TypeError)),
        ]
    )
    def test_sum(self, x, y, res, expectation):
        with expectation:
            assert Calculator().sum(x, y) == res
