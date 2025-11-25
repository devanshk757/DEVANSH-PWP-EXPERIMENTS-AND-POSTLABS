from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Define the main layout
class CounterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CounterLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Initial counter value
        self.counter = 0

        # Label to display counter
        self.label = Label(text="Count: 0", font_size=40)
        self.add_widget(self.label)

        # Button to increment counter
        self.button = Button(text="Increment", font_size=30, size_hint=(1, 0.5))
        self.button.bind(on_press=self.increment_counter)
        self.add_widget(self.button)

    # Function to increment the counter
    def increment_counter(self, instance):
        self.counter += 1
        self.label.text = f"Count: {self.counter}"

# Define the app class
class CounterApp(App):
    def build(self):
        return CounterLayout()

# Run the app
if __name__ == '__main__':
    CounterApp().run()
