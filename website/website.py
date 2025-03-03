import reflex as rx 

class MyState(rx.State):
    count: int = 0
    #color : str = "red"

    def increment(self):
        self.count += 1
        #self.color = "blue"

def counter():
    return rx.hstack(
        rx.heading(MyState.count),
        #rx.heading("Counter", color=MyState.color),
        #rx.heading(MyState.count),
        rx.button("Increment", on_click=MyState.increment),
    )

def button():
    return rx.button("Click Me", border_radius="15px", font_size="18px", color_scheme="red")

def index():
    return rx.box(
        #rx.text("Hello World!!!"),
        #half_filled_progress(),
        #button(),
        counter(),
    )

def half_filled_progress():
    return rx.progress(value=50)



app = rx.App()
app.add_page(index)


