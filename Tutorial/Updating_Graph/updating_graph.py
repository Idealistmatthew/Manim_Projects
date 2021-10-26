from manim import *

class amp(Scene):
    def construct(self):
        A = ValueTracker(1)
        graph = FunctionGraph(lambda x: np.arctan(A.get_value()* np.sin(x)))
        graph.add_updater(lambda func : func.become(FunctionGraph(lambda x: np.arctan(A.get_value()* np.sin(x)))))
        self.play(Write(graph))
        self.play(A.animate.set_value(1000),run_time=10)
