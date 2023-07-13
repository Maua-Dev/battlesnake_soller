from fastapi import FastAPI
from mangum import Mangum
from src.app.entities.battlesanke import Battlesnake

from src.app.entities.board import Board

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
    board = Board.from_json(request["board"])
    me = Battlesnake.from_json(request["you"])

    return


@app.post("/move")
def move(request: dict):
    board = Board.from_json(request["board"])
    me = Battlesnake.from_json(request["you"])

    moviment = board.navigate_to(me.head, board.get_closest_food(me))

    return moviment

# @app.post("/end")




handler = Mangum(app, lifespan="off")
