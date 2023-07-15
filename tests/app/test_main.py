from src.app.main import move, read_root, start_battle


class Test_Main:
    def test_read_root(self):
        resp = read_root()
        
        
        assert resp == {
        "apiversion": "1",
        "author": "VgsStudio",
        "color": "#9370DB",
        "head": "villain",
        "tail": "coffee",
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
                        "id":"ab249877-697a-4d2c-bc05-1b3485856c9d",
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
                    "turn":3,
                    "board":{
                        "height":11,
                        "width":11,
                        "snakes":[
                            {
                                "id":"gs_QMbXX9gPhwVchxJ9dk8dCwTP",
                                "name":"isapizi",
                                "latency":"48",
                                "health":99,
                                "body":[
                                {
                                    "x":5,
                                    "y":10
                                },
                                {
                                    "x":4,
                                    "y":10
                                },
                                {
                                    "x":4,
                                    "y":9
                                },
                                {
                                    "x":5,
                                    "y":9
                                }
                                ],
                                "head":{
                                "x":5,
                                "y":10
                                },
                                "length":4,
                                "shout":"Tá ligado, cachorro do mangue?",
                                "squad":"",
                                "customizations":{
                                "color":"#9370db",
                                "head":"caffeine",
                                "tail":"weight"
                                }
                            },
                            {
                                "id":"gs_cKTHghxDXc7PRmYDvQBMGFKQ",
                                "name":"Scared Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":10,
                                    "y":3
                                },
                                {
                                    "x":9,
                                    "y":3
                                },
                                {
                                    "x":9,
                                    "y":4
                                }
                                ],
                                "head":{
                                "x":10,
                                "y":3
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#000000",
                                "head":"bendr",
                                "tail":"curled"
                                }
                            },
                            {
                                "id":"gs_qBw64K8gdDjpSrgYXFr6Kvy8",
                                "name":"Loopy Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":5,
                                    "y":0
                                },
                                {
                                    "x":4,
                                    "y":0
                                },
                                {
                                    "x":4,
                                    "y":1
                                }
                                ],
                                "head":{
                                "x":5,
                                "y":0
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#800080",
                                "head":"caffeine",
                                "tail":"iguana"
                                }
                            },
                            {
                                "id":"gs_qbchpCMxHPC4D69TmgPd66M4",
                                "name":"Right Bot",
                                "latency":"1",
                                "health":97,
                                "body":[
                                {
                                    "x":4,
                                    "y":5
                                },
                                {
                                    "x":3,
                                    "y":5
                                },
                                {
                                    "x":2,
                                    "y":5
                                }
                                ],
                                "head":{
                                "x":4,
                                "y":5
                                },
                                "length":3,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#33beff",
                                "head":"missile",
                                "tail":"ion"
                                }
                            },
                            {
                                "id":"gs_tthRHJQrjy4WYvJyqH7Y4qXP",
                                "name":"Hungry Bot",
                                "latency":"1",
                                "health":99,
                                "body":[
                                {
                                    "x":3,
                                    "y":0
                                },
                                {
                                    "x":2,
                                    "y":0
                                },
                                {
                                    "x":1,
                                    "y":0
                                },
                                {
                                    "x":1,
                                    "y":1
                                }
                                ],
                                "head":{
                                "x":3,
                                "y":0
                                },
                                "length":4,
                                "shout":"",
                                "squad":"",
                                "customizations":{
                                "color":"#00cc00",
                                "head":"alligator",
                                "tail":"alligator"
                                }
                            }
                        ],
                        "food":[
                            {
                                "x":10,
                                "y":4
                            },
                            {
                                "x":6,
                                "y":0
                            },
                            {
                                "x":0,
                                "y":4
                            },
                            {
                                "x":5,
                                "y":5
                            },
                            {
                                "x":0,
                                "y":5
                            },
                            {
                                "x":8,
                                "y":3
                            }
                        ],
                        "hazards":[
                            
                        ]
                    },
                    "you":{
                        "id":"gs_QMbXX9gPhwVchxJ9dk8dCwTP",
                        "name":"isapizi",
                        "latency":"48",
                        "health":99,
                        "body":[
                            {
                                "x":5,
                                "y":10
                            },
                            {
                                "x":4,
                                "y":10
                            },
                            {
                                "x":4,
                                "y":9
                            },
                            {
                                "x":5,
                                "y":9
                            }
                        ],
                        "head":{
                            "x":5,
                            "y":10
                        },
                        "length":4,
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

            assert response['move'] == 'right'

    def test_move_dodge_future_head(self):
        request = {
                "game":{
                    "id":"1f4d3f50-4578-4642-9a0b-d4807f394287",
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
                    "source":"ladder"
                },
                "turn":102,
                "board":{
                    "height":11,
                    "width":11,
                    "snakes":[
                        {
                            "id":"gs_mrw7SVbTtxmWFDw8gd7dx4PJ",
                            "name":"isapizi",
                            "latency":"70",
                            "health":83,
                            "body":[
                            {
                                "x":4,
                                "y":8
                            },
                            {
                                "x":4,
                                "y":9
                            },
                            {
                                "x":5,
                                "y":9
                            },
                            {
                                "x":6,
                                "y":9
                            },
                            {
                                "x":7,
                                "y":9
                            },
                            {
                                "x":8,
                                "y":9
                            },
                            {
                                "x":9,
                                "y":9
                            },
                            {
                                "x":9,
                                "y":10
                            },
                            {
                                "x":8,
                                "y":10
                            },
                            {
                                "x":7,
                                "y":10
                            },
                            {
                                "x":6,
                                "y":10
                            },
                            {
                                "x":5,
                                "y":10
                            },
                            {
                                "x":4,
                                "y":10
                            }
                            ],
                            "head":{
                            "x":4,
                            "y":8
                            },
                            "length":13,
                            "shout":"Salve, cria!",
                            "squad":"",
                            "customizations":{
                            "color":"#9370db",
                            "head":"villain",
                            "tail":"weight"
                            }
                        },
                        {
                            "id":"gs_xVWG6rbhdJFw98HVGmwmhdY3",
                            "name":"Qwik Boi",
                            "latency":"4",
                            "health":100,
                            "body":[
                            {
                                "x":4,
                                "y":6
                            },
                            {
                                "x":4,
                                "y":5
                            },
                            {
                                "x":5,
                                "y":5
                            },
                            {
                                "x":6,
                                "y":5
                            },
                            {
                                "x":7,
                                "y":5
                            },
                            {
                                "x":8,
                                "y":5
                            },
                            {
                                "x":9,
                                "y":5
                            },
                            {
                                "x":9,
                                "y":6
                            },
                            {
                                "x":9,
                                "y":7
                            },
                            {
                                "x":8,
                                "y":7
                            },
                            {
                                "x":7,
                                "y":7
                            },
                            {
                                "x":6,
                                "y":7
                            },
                            {
                                "x":5,
                                "y":7
                            },
                            {
                                "x":5,
                                "y":7
                            }
                            ],
                            "head":{
                            "x":4,
                            "y":6
                            },
                            "length":14,
                            "shout":"I HAVE NO MOUTH BUT I MUST SCREAM",
                            "squad":"",
                            "customizations":{
                            "color":"#ac7ef4",
                            "head":"beluga",
                            "tail":"mouse"
                            }
                        }
                    ],
                    "food":[
                        {
                            "x":4,
                            "y":2
                        }
                    ],
                    "hazards":[
                        
                    ]
                },
                "you":{
                    "id":"gs_mrw7SVbTtxmWFDw8gd7dx4PJ",
                    "name":"isapizi",
                    "latency":"70",
                    "health":83,
                    "body":[
                        {
                            "x":4,
                            "y":8
                        },
                        {
                            "x":4,
                            "y":9
                        },
                        {
                            "x":5,
                            "y":9
                        },
                        {
                            "x":6,
                            "y":9
                        },
                        {
                            "x":7,
                            "y":9
                        },
                        {
                            "x":8,
                            "y":9
                        },
                        {
                            "x":9,
                            "y":9
                        },
                        {
                            "x":9,
                            "y":10
                        },
                        {
                            "x":8,
                            "y":10
                        },
                        {
                            "x":7,
                            "y":10
                        },
                        {
                            "x":6,
                            "y":10
                        },
                        {
                            "x":5,
                            "y":10
                        },
                        {
                            "x":4,
                            "y":10
                        }
                    ],
                    "head":{
                        "x":4,
                        "y":8
                    },
                    "length":13,
                    "shout":"Salve, cria!",
                    "squad":"",
                    "customizations":{
                        "color":"#9370db",
                        "head":"villain",
                        "tail":"weight"
                    }
                }
                }
         
        response = move(request)

        assert response['move'] == 'left'

    def test_move_try_kill(self):
        request = {
            "game":{
                "id":"80e0e750-4e1e-41fa-a7da-a05777086983",
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
                        "allowBodyCollisions":True,
                        "sharedElimination":True,
                        "sharedHealth":True,
                        "sharedLength":True
                        }
                    }
                },
                "map":"standard",
                "timeout":500,
                "source":"custom"
            },
            "turn":37,
            "board":{
                "height":11,
                "width":11,
                "snakes":[
                    {
                        "id":"gs_hBJY3VWXhpVScmTr94BcSvXT",
                        "name":"isapizi",
                        "latency":"27",
                        "health":100,
                        "body":[
                        {
                            "x":5,
                            "y":6
                        },
                        {
                            "x":5,
                            "y":5
                        },
                        {
                            "x":5,
                            "y":4
                        },
                        {
                            "x":5,
                            "y":3
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
                            "x":2,
                            "y":4
                        },
                        {
                            "x":2,
                            "y":4
                        }
                        ],
                        "head":{
                        "x":5,
                        "y":6
                        },
                        "length":9,
                        "shout":"Salve, cria!",
                        "squad":"",
                        "customizations":{
                        "color":"#9370db",
                        "head":"villain",
                        "tail":"coffee"
                        }
                    },
                    {
                        "id":"gs_SrPCTVVp78WGfMPydGpcdG3b",
                        "name":"Bombastic Bob",
                        "latency":"61",
                        "health":67,
                        "body":[
                        {
                            "x":6,
                            "y":7
                        },
                        {
                            "x":7,
                            "y":7
                        },
                        {
                            "x":7,
                            "y":8
                        },
                        {
                            "x":6,
                            "y":8
                        },
                        {
                            "x":6,
                            "y":9
                        }
                        ],
                        "head":{
                        "x":6,
                        "y":7
                        },
                        "length":5,
                        "shout":"",
                        "squad":"",
                        "customizations":{
                        "color":"#aa66cc",
                        "head":"trans-rights-scarf",
                        "tail":"default"
                        }
                    },
                    {
                        "id":"gs_SrhPMKYg7P63W9TPgpGfKRkG",
                        "name":"Devious Devin",
                        "latency":"412",
                        "health":96,
                        "body":[
                        {
                            "x":5,
                            "y":0
                        },
                        {
                            "x":4,
                            "y":0
                        },
                        {
                            "x":3,
                            "y":0
                        },
                        {
                            "x":3,
                            "y":1
                        },
                        {
                            "x":4,
                            "y":1
                        },
                        {
                            "x":5,
                            "y":1
                        },
                        {
                            "x":6,
                            "y":1
                        },
                        {
                            "x":6,
                            "y":2
                        }
                        ],
                        "head":{
                        "x":5,
                        "y":0
                        },
                        "length":8,
                        "shout":"",
                        "squad":"",
                        "customizations":{
                        "color":"#99cc00",
                        "head":"trans-rights-scarf",
                        "tail":"rbc-necktie"
                        }
                    }
                ],
                "food":[
                    {
                        "x":7,
                        "y":0
                    },
                    {
                        "x":7,
                        "y":2
                    }
                ],
                "hazards":[
                    
                ]
            },
            "you":{
                "id":"gs_hBJY3VWXhpVScmTr94BcSvXT",
                "name":"isapizi",
                "latency":"27",
                "health":100,
                "body":[
                    {
                        "x":5,
                        "y":6
                    },
                    {
                        "x":5,
                        "y":5
                    },
                    {
                        "x":5,
                        "y":4
                    },
                    {
                        "x":5,
                        "y":3
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
                        "x":2,
                        "y":4
                    },
                    {
                        "x":2,
                        "y":4
                    }
                ],
                "head":{
                    "x":5,
                    "y":6
                },
                "length":9,
                "shout":"Salve, cria!",
                "squad":"",
                "customizations":{
                    "color":"#9370db",
                    "head":"villain",
                    "tail":"coffee"
                }
            }
            }

        response = move(request)

        assert response['move'] == 'right' ## TODO fix two possible path, how to choose one?