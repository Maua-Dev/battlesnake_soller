from src.app.entities.coodinate import Coordinate


class Test_Coordinate:
    def test_coodinate(self):
        x = 1.0
        y = 2.0

        coordinate = Coordinate(x, y)

        assert coordinate.x == x
        assert coordinate.y == y

    def test_coodinate_eq(self):
        x = 1.0
        y = 2.0

        coordinate = Coordinate(x, y)
        coordinate2 = Coordinate(x, y)

        assert coordinate == coordinate2

    def test_coodinate_neq(self):
        x = 1.0
        y = 2.0

        coordinate = Coordinate(x, y)
        coordinate2 = Coordinate(x, 3.0)

        assert coordinate != coordinate2

    def test_coodinate_from_json(self):
        x = 1.0
        y = 2.0

        json = {
            'x': x,
            'y': y
        }

        coordinate = Coordinate.from_json(json)

        assert coordinate.x == x
        assert coordinate.y == y


