import reflex as rx

class TextState(rx.State):
    text: str = ""

    @rx.event
    def update_text(self, new_text: str):
        self.text = new_text


def index():
    return rx.vstack(
        rx.heading(TextState.text),
        rx.input(
            default_value=TextState.text,
            on_blur=TextState.update_text,
        ),
    )

app  = rx.App()
app.add_page(index)