from src.app.entities.battlesanke import Battlesnake
from src.app.entities.board import Board
from src.app.entities.coordinate import Coordinate


class Test_Board:
    def test_board(self):
        height = 1
        width = 2
        food = []
        snakes = []
        hazards = []

        board = Board(height, width, food, snakes, hazards)

        assert board.height == height
        assert board.width == width
        assert board.food == food
        assert board.snakes == snakes
        assert board.hazards == hazards
        
    def test_from_json(self):
        request = {
          "game": {
            "id": "game-id-string"
          },
          "turn": 4,
          "board": {
            "height": 11,
            "width": 11,
            "food": [
              {"x": 1, "y": 3},
              {"x": 5, "y": 5},
              {"x": 9, "y": 0}
            ],
            "snakes": [
              {
                "id": "snake-id-string",
                "name": "Sneky McSnek Face",
                "health": 90,
                "body": [
                  {"x": 0, "y": 0},
                  {"x": 1, "y": 0},
                  {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1"
              },
              {
                "id": "snake-id-string",
                "name": "Sneky McSnek Face",
                "health": 90,
                "body": [
                  {"x": 0, "y": 0},
                  {"x": 1, "y": 0},
                  {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1"
              }
            ],
            "hazards": [
              {"x": 3, "y": 2}
            ]
          },
          "you": {
            "id": "snake-id-string",
            "name": "Sneky McSnek Face",
            "health": 90,
            "body": [
              {"x": 0, "y": 0},
              {"x": 1, "y": 0},
              {"x": 2, "y": 0}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1"
            }
        }
        expected_board = Board(
            11,
            11,
            [
                Coordinate(1, 3),
                Coordinate(5, 5),
                Coordinate(9, 0)
            ],
            [
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(0, 0),
                        Coordinate(1, 0),
                        Coordinate(2, 0)
                    ],
                    "111",
                    Coordinate(0, 0),
                    3,
                    "why are we shouting??",
                    "1"
                ),
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(0, 0),
                        Coordinate(1, 0),
                        Coordinate(2, 0)
                    ],
                    "111",
                    Coordinate(0, 0),
                    3,
                    "why are we shouting??",
                    "1"
                )
            ],
            [
                Coordinate(3, 2)
            ]
        )

        actual_board = Board.from_json(request["board"])

        assert actual_board == expected_board

    def test_navigate_right(self):
        a = Coordinate(0, 0)
        b = Coordinate(1, 0)

        assert Board.navigate_to(a, b) == "right"

    def test_navigate_up(self):
        a = Coordinate(0, 0)
        b = Coordinate(0, 1)

        assert Board.navigate_to(a, b) == "up"

    def test_navigate_right_2(self):
        a = Coordinate(0, 0)
        b = Coordinate(1, 1)

        assert Board.navigate_to(a, b) == "right"

    def test_get_closest_food(self):
        board = Board(
            height =11,
            width = 11,
            food= [
                Coordinate(8, 8),
                Coordinate(9, 9),
                Coordinate(11, 7)
            ],
            snakes=[
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(3, 2),
                        Coordinate(2, 1),
                        Coordinate(1, 0)
                    ],
                    "111",
                    Coordinate(4, 6),
                    3,
                    "why are we shouting??",
                    "1"
                ),
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 6),
                        Coordinate(4, 7),
                        Coordinate(4, 8)
                    ],
                    "111",
                    Coordinate(0, 0),
                    3,
                    "why are we shouting??",
                    "1"
                )
            ],
            hazards=[
                Coordinate(3, 2)
            ]
        )

        my_snake = Battlesnake(
            snake_id="snake-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(0, 0),
            length=3,
            shout="Tá ligado?",
            squad="1"
        )
        closest_food = board.get_closest_food(my_snake)

        assert type(closest_food) == Coordinate
        assert closest_food == Coordinate(8, 8)


    def test_is_inside_snake(self):

        my_snake = Battlesnake(
            snake_id="snake-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(0, 0),
            length=3,
            shout="Tá ligado?",
            squad="1"
        )


        board = Board(
            height =11,
            width = 11,
            food= [
                Coordinate(8, 8),
                Coordinate(9, 9),
                Coordinate(11, 7)
            ],
            snakes=[
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(3, 2),
                        Coordinate(2, 1),
                        Coordinate(1, 0)
                    ],
                    "111",
                    Coordinate(3, 2),
                    3,
                    "why are we shouting??",
                    "1"
                ),
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 6),
                        Coordinate(4, 7),
                        Coordinate(4, 8)
                    ],
                    "111",
                    Coordinate(4, 6),
                    3,
                    "why are we shouting??",
                    "1"
                ),
                my_snake
            ],
            hazards=[
                Coordinate(3, 2)
            ]
        )

        
        assert board.is_snake("up", my_snake.head) == False
        assert type(board.is_snake("right", my_snake.head)) == Battlesnake


        