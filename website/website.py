import reflex as rx

def check_even(num):
    # Ensure num is an integer
    if isinstance(num, tuple):
        raise TypeError("Expected an integer, but got a tuple.")
    return num % 2 == 0

class MyState3(rx.State):
    count: int = 0,
    text : str = "even"

    @rx.event
    def increment(self):
        if check_even(self.count):
            self.text = "even"
        else:
            self.text = "odd"
        self.count += 1

def index():
    return rx.box(
        rx.heading(MyState3.text),
        rx.button("Increment", on_click=MyState3.increment),
    )

app = rx.App()
app.add_page(index)