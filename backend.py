from fastapi import FastAPI
from philosopher_main import getphilosophical
from requestmodel import RequestModel
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import uvicorn

origins = ["http://localhost:4200"]
app = FastAPI()
handler = Mangum(app)

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
    print("In get function");
    return {"message": "Hello World"}

@app.post("/getphilosophy")
async def getphilosophy(request: RequestModel):
    print("In Post function");
    return getphilosophical(request);

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)
