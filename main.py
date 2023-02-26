from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
with open("most-maidens-till-2022.json") as a:
    data1 = json.load(a)  # maidens
    with open("best-bowling-figs-till-2022.json") as b:
        data2 = json.load(b)  # bowling
        with open("fastest50-till-2022.json") as c:
            data3 = json.load(c)  # 50
            with open("most-SR-till-2022.json") as d:
                data4 = json.load(d)  # SR
                with open("most-runs-till-2022.json") as e:
                    data5 = json.load(e)  # runs
                    with open("most-wickets-till-2022.json") as f:
                        data6 = json.load(f)  # wickets

app = FastAPI()

@app.get("/")
def my_main_page():
    return {"message": "Welcome, this is the main homepage of this class"}

@app.get("/maidens")
async def get_maidens():
    return data1

@app.get("/bowling")
async def get_bowling():
    return data2

@app.get("/50")
async def get_50():
    return data3

@app.get("/runs")
async def get_runs():
    return data5

@app.get("/wickets")
async def get_wickets():
    return data5

@app.get("/SR")
async def get_sr():
    return data4

@app.get("/About")
def about():
    return {"message": 'Welcome, Our startup is about providing statistics on players to the team management. It can be any sport - Cricket, Football, Volleyball and many more. With the help of our analysis and reports team management can easily asses players and their capabilities. Our aim is to help our clients to make a better team and win championships.'}
