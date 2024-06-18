import fastapi
import uvicorn

app = fastapi.FastAPI()

count = 0

def get_count():
    global count
    count = count+1
    return count

@app.get('/')
def home():
    return "home"

@app.get('/counter')
def counter():
    return "counting : " + str(get_count())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2200)