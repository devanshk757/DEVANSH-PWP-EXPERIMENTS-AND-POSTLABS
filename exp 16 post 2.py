from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Set the background color to black
Window.clearcolor = (0, 0, 0, 1)  # Black background

class TextInputLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(TextInputLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        # Text input field
        self.text_input = TextInput(
            hint_text="Type something here...",
            multiline=False,
            font_size=24,
            size_hint=(1, 0.2),
            foreground_color=(1, 1, 1, 1),    # White text
            background_color=(0.2, 0.2, 0.2, 1)  # Dark gray background
        )
        self.add_widget(self.text_input)

        # Button
        self.button = Button(
            text="Show Text",
            font_size=24,
            background_color=(0.2, 0.6, 0.8, 1),  # Light blue
            color=(1, 1, 1, 1),  # White text
            size_hint=(1, 0.2)
        )
        self.button.bind(on_press=self.display_text)
        self.add_widget(self.button)

        # Label to show the text
        self.label = Label(
            text="",
            font_size=28,
            color=(1, 1, 1, 1)  # White text
        )
        self.add_widget(self.label)

    def display_text(self, instance):
        user_input = self.text_input.text
        self.label.text = f"You typed: {user_input}"

# Main App class
class TextInputApp(App):
    def build(self):
        return TextInputLayout()

# Run the app
if __name__ == '__main__':
    TextInputApp().run()
