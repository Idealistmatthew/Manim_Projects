from manim import *
import math

# Big E against small f
class Kelly_Maxi(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        jarell_color = "#E6B450"
        axes = Axes(
            x_range = [0,0.99,2],
            y_range = [-3,3,4],
            x_length = 10,
            tips= False,
            )

        p = ValueTracker(0)
        o = ValueTracker(2)

        graph = axes.get_graph( lambda x: p.get_value()*math.log(1+ o.get_value()*x) + (1-p.get_value())*math.log(1-x), x_range = [0,0.99], color = jarell_color )
        graph.add_updater(lambda m: m.become(axes.get_graph(lambda x: p.get_value()*math.log(1+ o.get_value()*x) + (1-p.get_value())*math.log(1-x), x_range = [0,0.99], color = jarell_color)))

        self.add(axes)
        self.add(graph)
        self.wait()
        self.play(p.animate.increment_value(1), run_time = 5)
        self.wait()
        self.play(p.animate.increment_value(-1), run_time = 5)
        self.wait()
        # self.play(p.animate.increment_value(1))
        # self.wait()
        # self.play(p.animate.increment_value(-1))
        # self.wait()
        # self.play(p.animate.increment_value(1))
        # self.wait()
        # self.play(p.animate.increment_value(-1))
        # self.wait()
        # self.play(p.animate.increment_value(1))
        # self.wait()
        # self.play(p.animate.increment_value(-1))
        # self.wait()
