from fasthtml.common import * # type: ignore
from fasthtml.common import (
    Button, Html, Head, Body, Div, Title, Link, Meta, Script, Form, H1,
)
import random

# for Docker
app, rt = fast_app(static_path="static") # type: ignore

# for local
# app, rt = fast_app(static_path="app/static") # type: ignore


@rt("/")
def homepage(session):
    session["multiplier"] = 1
    result = session.get("result", "")
    session["to_all"] = 0
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
                H1("Dice Roller", cls="title", style="padding-left: 4rem;"),
                Button(
                    "(i)", hx_get="/to_about", hx_push_url="true", hx_trigger="click",
                    cls="buttonAbout", style="width: 50px; font-variant: none; font-family:Georgia, 'Times New Roman', Times, serif;"),
                cls="container",
                style="flex-direction: row;",
            ),
            Div(
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
                Div(
                    Button("x11", id="eleven", hx_get="/select", hx_vals={"multiplier": 11}, type="submit", hx_swap="none"),
                    Button("x12", id="twelve", hx_get="/select", hx_vals={"multiplier": 12}, type="submit", hx_swap="none"),
                    Button("x13", id="thirteen", hx_get="/select", hx_vals={"multiplier": 13}, type="submit", hx_swap="none"),
                    Button("x14", id="fourteen", hx_get="/select", hx_vals={"multiplier": 14}, type="submit", hx_swap="none"),
                    Button("x15", id="fifteen", hx_get="/select", hx_vals={"multiplier": 15}, type="submit", hx_swap="none"),
                    cls="grid-1x5"
                ),
                 Div(
                    Button("x16", id="sixteen", hx_get="/select", hx_vals={"multiplier": 16}, type="submit", hx_swap="none"),
                    Button("x17", id="seventeen", hx_get="/select", hx_vals={"multiplier": 17}, type="submit", hx_swap="none"),
                    Button("x18", id="eighteen", hx_get="/select", hx_vals={"multiplier": 18}, type="submit", hx_swap="none"),
                    Button("x19", id="nineteen", hx_get="/select", hx_vals={"multiplier": 19}, type="submit", hx_swap="none"),
                    Button("x20", id="twenty", hx_get="/select", hx_vals={"multiplier": 20}, type="submit", hx_swap="none"),
                    cls="grid-1x5"
                ),
                # put it into container for future possibility of scrolling the multipliers to higher values
                cls="container",
                style="width: 100%; padding: 0; gap: 0;"
            ),
            Div(style="padding: 10px"),
            Div(
                Button("d3", id="d3", hx_get="/d3", hx_target="#result", type="submit", cls="buttonD"),
                Button("d4", id="d4", hx_get="/d4", hx_target="#result", type="submit", cls="buttonD"),
                Button("d6", id="d6", hx_get="/d6", hx_target="#result", type="submit", cls="buttonD"),
                Button("d8", id="d8", hx_get="/d8", hx_target="#result", type="submit", cls="buttonD"),
                cls="grid-1x4"
            ),
            Div(
                Button("d10", id="d10", hx_get="/d10", hx_target="#result", type="submit", cls="buttonD"),
                Button("d12", id="d12", hx_get="/d12", hx_target="#result", type="submit", cls="buttonD"),
                Button("d100", id="d100", hx_get="/d100", hx_target="#result", type="submit", cls="buttonD"),
                Button("d20", id="d20", hx_get="/d20", hx_target="#result", type="submit", cls="button20",
                       title="Critical Fail(1) always shows (1); Critical Success(20) is converted to (99)"),
                cls="grid-1x4"
            ),
            # displaying results
            Div(
                Div(style="padding: 10px;"),
                Div("Result", id="result", style="font-size: 1.6rem; color: rgba(245, 245, 245, 0);"),
                Div(style="padding: 10px;"),
                Div("Dice Result", id="dice", style="font-size: 1rem; height: 3rem; color: rgba(245, 245, 245, 0);"),
                Div("Dice Result with Bonus", id="dice-w-bonus", style="font-size: 1rem; height: 3rem; color: rgba(245, 245, 245, 0);"),
                cls="container",
                style="padding: 0; gap: 0;"
            ),
            # testing bonus damage (example: +5 form strength to each die)
            Div(style="padding: 10px"),
            Div(
                Div(
                    Button("+1", id="p-one", hx_get="/plus", hx_vals={"bonus": 1}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+2", id="p-two", hx_get="/plus", hx_vals={"bonus": 2}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+3", id="p-three", hx_get="/plus", hx_vals={"bonus": 3}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+4", id="p-four", hx_get="/plus", hx_vals={"bonus": 4}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+5", id="p-five", hx_get="/plus", hx_vals={"bonus": 5}, type="submit", hx_swap="none", cls="buttonPlus"),
                    cls="grid-1x5"
                ),
                Div(
                    Button("+6", id="p-six", hx_get="/plus", hx_vals={"bonus": 6}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+7", id="p-seven", hx_get="/plus", hx_vals={"bonus": 7}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+8", id="p-eight", hx_get="/plus", hx_vals={"bonus": 8}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+9", id="p-nine", hx_get="/plus", hx_vals={"bonus": 9}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+10", id="p-ten", hx_get="/plus", hx_vals={"bonus": 10}, type="submit", hx_swap="none", cls="buttonPlus"),
                    cls="grid-1x5"
                ),
                Div(
                    Button("+11", id="p-1one", hx_get="/plus", hx_vals={"bonus": 11}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+12", id="p-1two", hx_get="/plus", hx_vals={"bonus": 12}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+13", id="p-1three", hx_get="/plus", hx_vals={"bonus": 13}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+14", id="p-1four", hx_get="/plus", hx_vals={"bonus": 14}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+15", id="p-1five", hx_get="/plus", hx_vals={"bonus": 15}, type="submit", hx_swap="none", cls="buttonPlus"),
                    cls="grid-1x5"
                ),
                Div(
                    Button("+16", id="p-1six", hx_get="/plus", hx_vals={"bonus": 16}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+17", id="p-1seven", hx_get="/plus", hx_vals={"bonus": 17}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+18", id="p-1eight", hx_get="/plus", hx_vals={"bonus": 18}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+19", id="p-1nine", hx_get="/plus", hx_vals={"bonus": 19}, type="submit", hx_swap="none", cls="buttonPlus"),
                    Button("+20", id="p-twenty", hx_get="/plus", hx_vals={"bonus": 20}, type="submit", hx_swap="none", cls="buttonPlus"),
                    cls="grid-1x5"
                ),
                cls="container",
                style="width: 100%; padding: 0; gap: 0;"
            ),
            # testing checkbox
            Div(style="padding: 10px"),
            Div(
                Form(
                    CheckboxX(id="my-checkbox", label="Add Bonus to each die?", name="each_die", cls="checkbox"),
                    hx_post="/toggle", hx_trigger="change", target_id="checkbox-target", id="checkbox-form",
                    style="font-variant-caps: all-petite-caps;"
                ),
            ),
            Div("display checkbox text", id="checkbox-target", style="font-size: 1.2rem; color:rgba(245, 245, 245, 0);"),
            # Reset button
            Div(style="padding: 1px"),
            Div(
                Button("Reset", hx_get="/", hx_target="body", style="width: 120px"),
                cls="container"
            )
        )
    )

@rt("/toggle")
def toggle(each_die: bool, session):
    # Process the checkbox state (True for checked, False for unchecked)
    checkbox = "Adding to all dice" if each_die else "Adding once"
    if each_die is True:
        session["to_all"] = 1
        return Div(checkbox, style="font-size: 1.2rem; font-variant-caps: all-petite-caps; color: rgba(0, 255, 20, 0.6);")
    else:
        session["to_all"] = 0
        return Div(checkbox, style="font-size: 1.2rem; font-variant-caps: all-petite-caps;")


@rt("/select")
def multiplier_select(multiplier: int, session):
    # Store the first value in session
    session["multiplier"] = multiplier
    session["result"] = None  # Clear previous result
    session.get("to_all", None)

@rt("/plus")
def plus(bonus:int, session):
    try:
        session["bonus"] = bonus
        result = session.get("result", "")
        multiplier = session.get("multiplier", None)
        die_face = session.get("die_face", "")
        to_all = session.get("to_all", None)
        dice = session.get("dice_rolled", None)

        dice_with_bonus = []


        if to_all == 1:
            result_added = result + (multiplier * bonus)

            if die_face == "d20":
                for die in dice:
                    if die == 1:
                        dice_with_bonus.append(1)
                    elif die == 20:
                        dice_with_bonus.append(99)
                    else:
                        dice_with_bonus.append(die + bonus)
            else:
                for die in dice:
                    dice_with_bonus.append(die + bonus)

            return Div(
                    f"{multiplier}{die_face} + ({multiplier}x{bonus}) [{result_added}]",
                    hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
                    f"{dice_with_bonus}",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem; color: rgba(0, 255, 20, 0.6);")
        else:
            result_added = result + bonus
            return Div(
                    f"{multiplier}{die_face} +{bonus} [{result_added}]",
                    hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")

    except:
        return Div("Select multiplier >> die >> optionally add damage bonus.", hx_swap_oob="true", id="result", style="font-size: 1rem; color: red;"),


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
    session["die_face"] = "d3"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d3 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    session["die_face"] = "d4"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d4 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


@rt("/d100")
def d100(session):
    multiplier = session.get("multiplier", None)
    if multiplier is None:
        return Div("Select a multiplier.", id="result")

    dice = []
    total = 0

    for die in range(multiplier):
        dice.append(random.randint(1, 100))
        print(dice)

    for die in dice:
        total += die

    result = total

    session["result"] = result
    session["die_face"] = "d100"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d100 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    session["die_face"] = "d6"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d6 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    session["die_face"] = "d8"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d8 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    session["die_face"] = "d10"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d10 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    session["die_face"] = "d12"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d12 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


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
    # dice.sort()
    # dice.reverse()

    session["result"] = result
    session["die_face"] = "d20"
    session["dice_rolled"] = dice

    return Div(f"{multiplier}d20 [{result}]", hx_swap_oob="true", id="result", style="font-size: 1.6rem;"), Div(
        f"{dice}", hx_swap_oob="true", id="dice", style="font-size: 1rem; height: 3rem;"), Div(
                    "",
                    hx_swap_oob="true", id="dice-w-bonus", style="font-size: 1rem; height: 3rem;")


@rt("/about")
def about(session):
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
            Div(P("About My App and How it Works"),
                P("Also TODO: 1. Fix about section ;)"),
                cls="container"),
            Div(
                Button("Return", hx_get="/return", hx_push_url="true", style="width: 120px"),
                cls="container"
            )
        )
    )

@rt("/to_about")
def to_about(session):
    return Redirect("/about")

@rt("/return")
def to_about(session):
    return Redirect("/")


if __name__ == '__main__':
    # Important: Use host='0.0.0.0' to make the server accessible outside the container
    serve(host='0.0.0.0', port=5066) # type: ignore