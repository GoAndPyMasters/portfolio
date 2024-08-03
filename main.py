from fasthtml import FastHTML, A, Nav, Ul, Li, Div, H1
from fasthtml.common import *

app = FastHTML()

@app.get("/")
def create_navbar():
    return Nav(
        Div(
            H1("Muhammad Ishaque Nizamani", style="display: inline-block; margin-right: auto; color: white;"),
            Ul(
                Li(A("Home", href="#home", style="color: white; text-decoration: none;" )),
                Li(A("About", href="#about", style="color: white; text-decoration: none;")),
                Li(A("Resume", href="#resume", style="color: white; text-decoration: none;")),
                Li(A("Portfolio", href="#portfolio", style="color: white; text-decoration: none;")),
                Li(A("Contact", href="#contact",  style="color: white; text-decoration: none;")),
                style="list-style-type: none; display: flex; gap: 20px; justify-content: flex-end;"
            ),
            style="display: flex; justify-content: space-between; align-items: center; padding: 10px; background-color: #222;"
        ),
    )
# print(html.render())

serve()
