from fastapi import FastAPI
from philosopher_main import getphilosophical
from requestmodel import RequestModel
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:4200"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
request = RequestModel(userinput = "Hello")
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/getphilosophy/")
async def getphilosophy(request: RequestModel):
    return getphilosophical(request);
