from fastapi import FastAPI
from mangum import Mangum
from .entities.battlesanke import Battlesnake

from .entities.board import Board

app = FastAPI()

@app.get("/")
def read_root():
    response = {
        "apiversion": "1",
        "author": "VgsStudio",
        "color": "#9370DB",
        "head": "caffeine",
        "tail": "weight",
        "version": "0.0.1-beta"
        }
    return response


@app.post("/start")
def start_battle(request: dict):
    print("Start")
    print(request)

    board = Board.from_json(request["board"])
    me = Battlesnake.from_json(request["you"])

    return


@app.post("/move")
def move(request: dict):
    print("Move")
    print(request)

    board = Board.from_json(request["board"])
    me = Battlesnake.from_json(request["you"])

    move = board.navigate_to(me.head, board.get_closest_food(me))

    maybe_snake = board.is_snake(move, me.head)

    if type(maybe_snake) == Battlesnake:
        print("Dodge snake")
        move = board.dodge_snake_body(me, maybe_snake)

    print(move)

    response = {
        "move": move,
        "shout": Battlesnake.random_shout()
    }

    print("Response")
    print(response)

    return response

@app.post("/end")
def end_battle(request: dict):
    return




handler = Mangum(app, lifespan="off")
