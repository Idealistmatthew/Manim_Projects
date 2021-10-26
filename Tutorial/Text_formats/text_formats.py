 from manim import *

class WriteText(Scene):
    def construct(self):
        logo_blue = "#0633D6"
        background_blue = "#F1F8FF"
        self.camera.background_color = background_blue
        text_1 = Text("Welcome to", color = logo_blue).scale(1.5)
        text_2 = Text("Idealist Matthew's Website.", color = logo_blue).scale(1.5)
        Group(text_1,text_2).arrange(DOWN, buff =.8)
        self.play(Write(text_1))
        self.play(Write(text_2))
        self.wait(3)
