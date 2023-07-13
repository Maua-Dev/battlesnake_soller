from src.app.entities.coordinate import Coordinate


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

    def test_coordinate_distance(self):
        a = Coordinate(1, 1)
        b = Coordinate(2, 2)

        assert Coordinate.distance(a, b) == 2

    def test_coodinate_distance_diagonal(self):
        a = Coordinate(0, 0)
        b = Coordinate(3, 4)

        assert Coordinate.distance(a, b) == 7

    def test_move_command(self):

        head = Coordinate(1, 1)

        assert head.move_command("up") == Coordinate(1, 2)
        assert head.move_command("down") == Coordinate(1, 0)
        assert head.move_command("left") == Coordinate(0, 1)
        assert head.move_command("right") == Coordinate(2, 1)
        assert head.move_command("invalid") == head

