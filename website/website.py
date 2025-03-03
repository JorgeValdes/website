import reflex as rx 


def button():
    return rx.button("Click Me", border_radius="15px", font_size="18px")

def index():
    return rx.box(
        rx.text("Hello World!!!"),
        half_filled_progress(),
        button(),
    )

def half_filled_progress():
    return rx.progress(value=50)



app = rx.App()
app.add_page(index)


