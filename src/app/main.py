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

    moviment = board.navigate_to(me.head, board.get_closest_food(me))

    print(moviment)

    response = {
        "move": moviment,
        "shout": Battlesnake.random_shout()
    }
    print("Response")
    print(response)

    return {
  "move": "right",
  "shout": "Moving up!"
}

@app.post("/end")
def end_battle(request: dict):
    return




handler = Mangum(app, lifespan="off")
