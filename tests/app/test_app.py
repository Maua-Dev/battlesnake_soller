from src.app.main import move, read_root, start_battle


class Test_App:
    def test_read_root(self):
        resp = read_root()
        
        
        assert resp == {
        "apiversion": "1",
        "author": "VgsStudio",
        "color": "#9370DB",
        "head": "caffeine",
        "tail": "weight",
        "version": "0.0.1-beta"
        }

    def test_start_battle(self):
        request = {
            "game": {
                "id": "game-id-string"
            },
            "turn": 4,
            "board": {
                "height": 11,
                "width": 11,
                "food": [
                    {
                        "x": 5,
                        "y": 5
                    }
                ],
                "snakes": [
                    {
                        "id": "snake-id-string",
                        "name": "Sneky Snek",
                        "health": 90,
                        "latency": "111",
                        "body": [
                            {
                                "x": 1,
                                "y": 3
                            }
                        ],
                        "head": {
                            "x": 1,
                            "y": 3
                        },
                        "length": 3,
                        "shout": "Hello my name is Sneky Snek"
                    }
                ],
                "hazards": [
                    {
                        "x": 3,
                        "y": 2
                    }
                ]
            },
            "you": {
                "id": "snake-id-string",
                "name": "Sneky Snek",
                "health": 90,
                "latency": "111",
                "body": [
                    {
                        "x": 1,
                        "y": 3
                    }
                ],
                "squad": "1",
                "head": {
                    "x": 1,
                    "y": 3
                },
                "length": 3,
                "shout": "Hello my name is Sneky Snek"
            }
        }
        response = start_battle(request)

        assert response is None

    def test_move(self):
        request = {
            "game": {
                "id": "game-id-string"
            },
            "turn": 4,
            "board": {
                "height": 11,
                "width": 11,
                "food": [
                    {
                        "x": 5,
                        "y": 5
                    }
                ],
                "snakes": [
                    {
                        "id": "snake-id-string",
                        "name": "Sneky Snek",
                        "health": 90,
                        "latency": "111",
                        "body": [
                            {
                                "x": 1,
                                "y": 3
                            }
                        ],
                        "head": {
                            "x": 1,
                            "y": 3
                        },
                        "length": 3,
                        "shout": "Hello my name is Sneky Snek"
                    }
                ],
                "hazards": [
                    {
                        "x": 3,
                        "y": 2
                    }
                ]
            },
            "you": {
                "id": "snake-id-string",
                "name": "Sneky Snek",
                "health": 90,
                "latency": "111",
                "body": [
                    {
                        "x": 1,
                        "y": 3
                    }
                ],
                "squad": "1",
                "head": {
                    "x": 1,
                    "y": 3
                },
                "length": 3,
                "shout": "Hello my name is Sneky Snek"
            }
        }

        response = move(request)

        assert response == "right"
