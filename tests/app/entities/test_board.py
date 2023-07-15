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

    def test_get_near_snake_head(self):
        my_snake = Battlesnake(
            snake_id="my-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 1),
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(2, 0),
            length=4,
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
                    "death-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 2),
                        Coordinate(4, 1),
                        Coordinate(4, 0)
                    ],
                    "111",
                    Coordinate(4, 0),
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

        result = board.get_near_snake_head(my_snake)

        assert type(result) == tuple
        assert type(result[0]) == Battlesnake
        assert result[1] == "right"
        assert result[0].snake_id == "death-id-string"

    def test_is_near_snake_head(self):
        my_snake = Battlesnake(
            snake_id="my-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 1),
                Coordinate(1, 1),
                Coordinate(2, 1)
            ],
            latency="111",
            head=Coordinate(2, 1),
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
                        Coordinate(3, 1),
                        Coordinate(3, 0)
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

        assert board.is_near_snake_head("up", my_snake) == True
        assert board.is_near_snake_head("right", my_snake) == True
        assert board.is_near_snake_head("left", my_snake) == False
        assert board.is_near_snake_head("down", my_snake) == False


    def test_can_move(self):
        my_snake = Battlesnake(
            snake_id="my-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 1),
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(2, 0),
            length=4,
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
                    "death-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 2),
                        Coordinate(4, 1),
                        Coordinate(4, 0)
                    ],
                    "111",
                    Coordinate(4, 0),
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

        result = board.can_move("right", my_snake)

        assert result == True

    def test_can_move_false(self):
        my_snake = Battlesnake(
            snake_id="my-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 1),
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(2, 0),
            length=4,
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
                    "death-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 4),
                        Coordinate(4, 3),
                        Coordinate(4, 2),
                        Coordinate(4, 1),
                        Coordinate(4, 0)
                    ],
                    "111",
                    Coordinate(4, 0),
                    5,
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

        result = board.can_move("right", my_snake) 

        assert result == False 

    def test_where_to_go(self):
        my_snake = Battlesnake(
            snake_id="my-id-string",
            name="Sneky McSnek Face",
            health=90,
            body=[
                Coordinate(0, 1),
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            latency="111",
            head=Coordinate(2, 0),
            length=4,
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
                    "death-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(4, 2),
                        Coordinate(4, 1),
                        Coordinate(4, 0)
                    ],
                    "111",
                    Coordinate(4, 0),
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

        result = board.where_to_go(my_snake)

        assert result == "right"
