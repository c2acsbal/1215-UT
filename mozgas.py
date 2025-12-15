import unittest
def mozgas_ertekeles(mozgas: str) -> tuple[int, int]:
    x = 0
    y = 0

    for m in mozgas:
        m = m.upper()
        if m == "B":
            x -= 1
        elif m == "J":
            x += 1
        elif m == "F":
            y -= 1
        elif m == "L":
            y += 1

    return x, y




class TestMozgas(unittest.TestCase):

    def test_csak_x_mozgas(self):
        self.assertEqual(mozgas_ertekeles("JJFBFFFFFFBBBL"), (2, 6))
        self.assertEqual(mozgas_ertekeles("FBLLLJLLJ"), (1, 4))




unittest.main()