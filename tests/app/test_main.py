from src.app.main import move, read_root, start_battle


class Test_Main:
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

        expected = {
            "move": "right",
            "shout": "Some random shout"
        }
        assert type(response) == dict
        assert response["move"] == expected["move"]
        assert type(response["shout"])

    def test_move_dodge_snake(self):

            

            request = {
        "game":{
            "id":"0155b4dd-98d8-465b-a8a4-2c6379aa1bd5",
            "ruleset":{
                "name":"standard",
                "version":"v1.2.3",
                "settings":{
                    "foodSpawnChance":15,
                    "minimumFood":1,
                    "hazardDamagePerTurn":0,
                    "hazardMap":"",
                    "hazardMapAuthor":"",
                    "royale":{
                    "shrinkEveryNTurns":0
                    },
                    "squad":{
                    "allowBodyCollisions":False,
                    "sharedElimination":False,
                    "sharedHealth":False,
                    "sharedLength":False
                    }
                }
            },
            "map":"standard",
            "timeout":500,
            "source":"custom"
        },
        "turn":52,
        "board":{
            "height":11,
            "width":11,
            "snakes":[
                {
                    "id":"gs_kjV64Dkmxr8WGwhHKMqKMt9V",
                    "name":"isapizi",
                    "latency":"45",
                    "health":98,
                    "body":[
                    {
                        "x":3,
                        "y":1
                    },
                    {
                        "x":3,
                        "y":0
                    },
                    {
                        "x":4,
                        "y":0
                    },
                    {
                        "x":4,
                        "y":1
                    },
                    {
                        "x":4,
                        "y":2
                    },
                    {
                        "x":4,
                        "y":3
                    },
                    {
                        "x":4,
                        "y":4
                    },
                    {
                        "x":3,
                        "y":4
                    },
                    {
                        "x":3,
                        "y":3
                    },
                    {
                        "x":2,
                        "y":3
                    },
                    {
                        "x":1,
                        "y":3
                    },
                    {
                        "x":1,
                        "y":4
                    },
                    {
                        "x":1,
                        "y":5
                    }
                    ],
                    "head":{
                    "x":3,
                    "y":1
                    },
                    "length":13,
                    "shout":"Tá ligado, cachorro do mangue?",
                    "squad":"",
                    "customizations":{
                    "color":"#9370db",
                    "head":"caffeine",
                    "tail":"weight"
                    }
                },
                {
                    "id":"gs_dtTdxTM9fRyMFJgCghbv6p7b",
                    "name":"Scared Bot",
                    "latency":"1",
                    "health":50,
                    "body":[
                    {
                        "x":8,
                        "y":2
                    },
                    {
                        "x":8,
                        "y":1
                    },
                    {
                        "x":7,
                        "y":1
                    },
                    {
                        "x":7,
                        "y":0
                    }
                    ],
                    "head":{
                    "x":8,
                    "y":2
                    },
                    "length":4,
                    "shout":"",
                    "squad":"",
                    "customizations":{
                    "color":"#000000",
                    "head":"bendr",
                    "tail":"curled"
                    }
                },
                {
                    "id":"gs_3GBDdgTVDWmQxFVVBTWdSgDQ",
                    "name":"Loopy Bot",
                    "latency":"1",
                    "health":48,
                    "body":[
                    {
                        "x":5,
                        "y":9
                    },
                    {
                        "x":5,
                        "y":8
                    },
                    {
                        "x":4,
                        "y":8
                    }
                    ],
                    "head":{
                    "x":5,
                    "y":9
                    },
                    "length":3,
                    "shout":"",
                    "squad":"",
                    "customizations":{
                    "color":"#800080",
                    "head":"caffeine",
                    "tail":"iguana"
                    }
                }
            ],
            "food":[
                {
                    "x":3,
                    "y":10
                }
            ],
            "hazards":[
                
            ]
        },
        "you":{
            "id":"gs_kjV64Dkmxr8WGwhHKMqKMt9V",
            "name":"isapizi",
            "latency":"45",
            "health":98,
            "body":[
                {
                    "x":3,
                    "y":1
                },
                {
                    "x":3,
                    "y":0
                },
                {
                    "x":4,
                    "y":0
                },
                {
                    "x":4,
                    "y":1
                },
                {
                    "x":4,
                    "y":2
                },
                {
                    "x":4,
                    "y":3
                },
                {
                    "x":4,
                    "y":4
                },
                {
                    "x":3,
                    "y":4
                },
                {
                    "x":3,
                    "y":3
                },
                {
                    "x":2,
                    "y":3
                },
                {
                    "x":1,
                    "y":3
                },
                {
                    "x":1,
                    "y":4
                },
                {
                    "x":1,
                    "y":5
                }
            ],
            "head":{
                "x":3,
                "y":1
            },
            "length":13,
            "shout":"Tá ligado, cachorro do mangue?",
            "squad":"",
            "customizations":{
                "color":"#9370db",
                "head":"caffeine",
                "tail":"weight"
            }
        }
        }
                
            response = move(request)
