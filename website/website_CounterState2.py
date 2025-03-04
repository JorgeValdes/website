import reflex as rx 

class CounterState2(rx.State):
    count: int = 0
    #color : str = "red"

    def increment(self, amount):
        self.count += amount
        #self.color = "blue"

    def decrement(self, amount):
        self.count -= amount
        #self.color = "blue"

def counter_variable():
    return rx.hstack(
        rx.heading(CounterState2.count),
        #rx.heading("Counter", color=MyState.color),
        #rx.heading(MyState.count),
        rx.button("Increment by 1", on_click=lambda: CounterState2.increment(1)),
        rx.button("Increment by 5", on_click=lambda: CounterState2.increment(5)),
        rx.button("Decrement by 5", on_click=lambda: CounterState2.decrement(5)),
    )

#def button():
#    return rx.button("Click Me", border_radius="15px", font_size="18px", color_scheme="red")

def index():
    return rx.box(
        #rx.text("Hello World!!!"),||
        #half_filled_progress(),
        #button(),
        counter_variable(),
    )

def half_filled_progress():
    return rx.progress(value=50)



app = rx.App()
app.add_page(index)
app.add_page(counter_variable)


