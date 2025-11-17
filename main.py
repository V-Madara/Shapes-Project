from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivy.core.window import Window
import CircleGenerator

Window.size = (600, 700)
Window.left= 400
Window.top=100

class Main(MDApp):
    def lengthInput(self, instance):
        try:
            self.length = int(instance.text)
            toast(f"Length set to {self.length}")
        except ValueError:
            toast("Please enter a valid number for length")

    def sidesInput(self, instance):
        try:
            self.sides = int(instance.text)
            toast(f"Sides set to {self.sides}")
        except ValueError:
            toast("Please enter a valid number for sides")

    def action(self, *args):
        if hasattr(self, 'length') and hasattr(self, 'sides'):
            toast("Drawing polygon...")
            CircleGenerator.Shapes().draw(self.length, self.sides)
            self.stop()
        else:
            toast("Enter both length and sides first!")

    def build(self):
        # 🌙 Theme setup
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Dark"

        screen = MDScreen()

        # 🟣 Main card container
        card = MDCard(
            orientation="vertical",
            padding=40,
            spacing=30,
            size_hint=(None, None),
            size=(500, 550),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=8,
            radius=[25, 25, 25, 25],
        )

        heading = MDLabel(
            text="Polygon Constructor",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )

        self.length_input = MDTextField(
            hint_text="Enter side length",
            helper_text="Press Enter to confirm",
            helper_text_mode="on_focus",
            icon_right="ruler",
            size_hint_x=1,
            mode="rectangle"
        )
        self.length_input.bind(on_text_validate=self.lengthInput)

        self.sides_input = MDTextField(
            hint_text="Enter number of sides",
            helper_text="Press Enter to confirm",
            helper_text_mode="on_focus",
            icon_right="shape-polygon-plus",
            size_hint_x=1,
            mode="rectangle"
        )
        self.sides_input.bind(on_text_validate=self.sidesInput)

        draw_btn = MDRaisedButton(
            text="Draw Polygon",
            pos_hint={"center_x": 0.5},
            md_bg_color=self.theme_cls.primary_color,
            on_release=self.action,
            elevation=6,
        )

        # Add everything to card
        card.add_widget(heading)
        card.add_widget(self.length_input)
        card.add_widget(self.sides_input)
        card.add_widget(draw_btn)

        # Add to screen
        screen.add_widget(card)
        return screen


if __name__ == "__main__":
    Main().run()
