from screen import Screen

import numpy as np


def draw_checker():
    WIDTH = 500
    HEIGHT = 500
    CHECKER_SIZE = 125

    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 0)
    DEFAULT_COLOR = (255, 0, 255)

    screen = Screen(WIDTH, HEIGHT)

    image_buffer = np.full((HEIGHT, WIDTH, 3), DEFAULT_COLOR)


    for row in range(HEIGHT):
        for col in range(WIDTH):
            color = COLOR1
            if (int(row / CHECKER_SIZE) % 2) ^ (int(col / CHECKER_SIZE) % 2):
                color = COLOR2

            image_buffer[col, row] = color
            
    screen.draw(image_buffer)

    screen.show()

def test_buffer_size_exception():
    import pytest

    screen = Screen(100, 100)
    image_buffer = np.full((100, 50, 3), [0, 0, 0])
    with pytest.raises(Exception):
        screen.draw(image_buffer)

    screen = Screen(100, 100)
    image_buffer = np.full((100, 100, 2), [0, 0])
    with pytest.raises(Exception):
        screen.draw(image_buffer)


def test_ratio():
    from math import isclose

    screen = Screen(100, 100)
    assert isclose(screen.ratio(), 1.0)

    screen = Screen(100, 200)
    assert isclose(screen.ratio(), 0.5)

    screen = Screen(200, 100)
    assert isclose(screen.ratio(), 2.0)


if __name__ == '__main__':
    draw_checker()
