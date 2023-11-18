from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4,5,6,7,8,0]

@app.get("/contact")
def get_list():
    return {"name": 'Eddy'}

@app.get("/pagehtml",response_class = HTMLResponse)
def get_html():
     return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """


def run():
    store.get_categories()


if __name__ == "__main__":
    run()