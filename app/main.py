from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Titled, Link, Meta, Script, Input, Form, Base, H1, Img, A,
    Redirect, Response, Path
)
import random

# for Docker
# app, rt = fast_app(static_path="static") # type: ignore

# for local
app, rt = fast_app(static_path="app/static") # type: ignore

# TODO:
# 1. Add visual or text indicator what was clicked
# 2. Add text what were each results for each die from the set

@rt("/")
def homepage(session):
    multiplier = session.get("multiplier", None)
    result = session.get("result", "")
    return Html(
        Head(
            Title("Dice Roller"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Script(src="https://unpkg.com/htmx.org"),
            Link(rel="stylesheet", href="styles.css"),
            Link(rel="icon", href="images/favicon.ico", type="image/x-icon"),
            Link(rel="icon", href="images/favicon.png", type="image/png"),
        ),
        Body(
            Div(
                H1("Dice Roller", cls="title"),
                cls="container",
            ),
            Div(
                Button("x1", id="one", hx_get="/select", hx_vals={"multiplier": 1}, type="submit", hx_swap="none"),
                Button("x2", id="two", hx_get="/select", hx_vals={"multiplier": 2}, type="submit", hx_swap="none"),
                Button("x3", id="three", hx_get="/select", hx_vals={"multiplier": 3}, type="submit", hx_swap="none"),
                Button("x4", id="four", hx_get="/select", hx_vals={"multiplier": 4}, type="submit", hx_swap="none"),
                Button("x5", id="five", hx_get="/select", hx_vals={"multiplier": 5}, type="submit", hx_swap="none"),
                cls="grid-1x5"
            ),
            Div(
                Button("x6", id="six", hx_get="/select", hx_vals={"multiplier": 6}, type="submit", hx_swap="none"),
                Button("x7", id="seven", hx_get="/select", hx_vals={"multiplier": 7}, type="submit", hx_swap="none"),
                Button("x8", id="eight", hx_get="/select", hx_vals={"multiplier": 8}, type="submit", hx_swap="none"),
                Button("x9", id="nine", hx_get="/select", hx_vals={"multiplier": 9}, type="submit", hx_swap="none"),
                Button("x10", id="ten", hx_get="/select", hx_vals={"multiplier": 10}, type="submit", hx_swap="none"),
                cls="grid-1x5"
            ),
            Div(style="padding: 10px"),
            Div(
                Button("d3", id="d3", hx_get="/d3", hx_target="#result", type="submit"),
                Button("d4", id="d4", hx_get="/d4", hx_target="#result", type="submit"),
                Button("d5", id="d5", hx_get="/d5", hx_target="#result", type="submit"),
                Button("d6", id="d6", hx_get="/d6", hx_target="#result", type="submit"),
                cls="grid-1x4"
            ),
            Div(
                Button("d8", id="d8", hx_get="/d8", hx_target="#result", type="submit"),
                Button("d10", id="d10", hx_get="/d10", hx_target="#result", type="submit"),
                Button("d12", id="d12", hx_get="/d12", hx_target="#result", type="submit"),
                Button("d20", id="d20", hx_get="/d20", hx_target="#result", type="submit"),
                cls="grid-1x4"
            ),
            Div(style="padding: 10px;"),
            Div("Result", id="result", style="font-size: 2rem; color: rgba(245, 245, 245, 0);")
        )
    )

@rt("/select")
def multiplier_select(multiplier: int, session):
    # Store the first value in session
    session["multiplier"] = multiplier
    session["result"] = None  # Clear previous result


@rt("/d3")
def d3(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 3))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d4")
def d4(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 4))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d5")
def d5(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 5))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d6")
def d6(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 6))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d8")
def d8(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 8))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d10")
def d10(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 10))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d12")
def d12(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 12))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


@rt("/d20")
def d20(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 20))
        print(dice)

    for die in dice:
        total += die

    result = total
    session["result"] = result

    return Div(f"{result}")


serve()

# if __name__ == '__main__':
#     # Important: Use host='0.0.0.0' to make the server accessible outside the container
#     serve(host='0.0.0.0', port=5066) # type: ignore