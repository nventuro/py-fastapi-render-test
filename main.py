from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola!"}

@app.get("/game/{game_id}")
def read_game(game_id):
    return {"game_id": game_id}
