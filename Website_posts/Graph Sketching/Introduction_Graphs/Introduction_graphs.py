from manim import *
import math
logo_blue = "#0633D6"
background_blue = "#F1F8FF"

class IntroductionGraphs(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
            x_range=[0, 10, 15],
            y_range=[-0.5, 10, 15],
            axis_config={"color": logo_blue},
        )
        axes.scale(0.5)
        axes.shift(3.2*LEFT)
        potential_graph = axes.get_graph(lambda x: 1/(x**12) - 1/(x**6), color=RED, x_range=[0.8,10,0.01])

        potential_label = MathTex("\\displaystyle f(x) = \\left( \\frac{1}{x} \\right)^{12} + \\left( \\frac{1}{x} \\right)^6", color = RED).next_to(axes, UP, buff=0.2).scale(0.8)
        potential_name = Text("Lennard-Jones Potential", color = RED).next_to(axes, DOWN, buff = 0.2).scale(0.6)

        graph_1 = VGroup(axes, potential_graph,potential_label, potential_name)
        # self.add(plot, labels)
        ax = Axes(
            x_range=[0, 5,15],
            y_range=[-0.5, 6,15],
            axis_config = {"color": logo_blue},
        )
        ax.scale(0.5)

        ax.next_to(axes, RIGHT, buff = 0.7)

        indiff_curve = ax.get_graph(lambda x: 1/x, x_range=[0.15, 4,0.01], color=GREEN)
        indiff_label = MathTex("\\displaystyle g(x) = \\left( \\frac{1}{x} \\right)", color = GREEN).next_to(ax,UP , buff = 0.2).scale(0.8)
        indiff_name = Text("Indifference Curve", color = GREEN).next_to(ax, DOWN, buff = 0.2).scale(0.6 )

        graph_2 = VGroup(ax, indiff_curve,indiff_label,indiff_name)
        self.add(graph_1,graph_2)

class FunctionMachine(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        funcrectangle = Rectangle(stroke_color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.8)
        function = MathTex("f(x) = x^2", color = logo_blue).move_to(funcrectangle.get_center())
        machine = VGroup(funcrectangle, function)
        input_1 = MathTex("2", color = YELLOW_E).next_to(machine, LEFT, buff = 1).scale(1.5)
        output_1 = MathTex("4", color = YELLOW_E).next_to(machine,RIGHT, buff = 1).scale(1.5)
        input_2 = MathTex("-2", color = RED_E).next_to(machine, LEFT, buff = 1).scale(1.5)
        output_2 = MathTex("4", color = RED_E).next_to(machine,RIGHT, buff = 1).scale(1.5)
        self.play(DrawBorderThenFill(funcrectangle))
        self.play(FadeIn(function))
        self.play(FadeIn(input_1))
        self.play(Transform(input_1,output_1))
        self.play(FadeOut(input_1))
        self.play(FadeIn(input_2))
        self.play(Transform(input_2,output_2))
        self.play(FadeOut(input_2))

class ShiftGraph(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,5,1],
        y_range = [0,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        line = NumberLine(
        x_range = [-2,2.5],
        length = 4.5,
        color = logo_blue,
        decimal_number_config = {"color": logo_blue, "num_decimal_places": 0},
        include_numbers = True,
        include_tip = True
        )
        axes.add_coordinates()
        axes.scale(0.75)
        line.next_to(axes, DOWN, buff = 0.5)
        line.scale(0.75)
        function = MathTex("f(x+a) = (x+a)^2", color = BLUE_C).next_to(axes, UP, buff = 0.5)
        a_text = MathTex("a", color = BLUE_C).next_to(line, RIGHT, buff = 0.1)
        a = ValueTracker(0)
        tracker = Dot(point = line.number_to_point(a.get_value()), color = BLUE_C)
        tracker.add_updater(lambda m:m.become(Dot(point = line.number_to_point(a.get_value()), color = BLUE_C)))
        graph = axes.get_graph(lambda x: (x+a.get_value())**2, color = BLUE_C)
        graph.add_updater(lambda m: m.become(axes.get_graph(lambda x: (x+a.get_value())**2, color = BLUE_C)))

        self.play(Create(tracker), Write(line), Write(axes), Write(function), Write(a_text))
        self.add(graph)
        self.play(a.animate.increment_value(2), run_time = 2)
        self.play(a.animate.increment_value(-4), run_time = 4)

class StretchGraph(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,5,1],
        y_range = [0,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        line = NumberLine(
        x_range = [0,3],
        length = 3,
        color = logo_blue,
        decimal_number_config = {"color": logo_blue, "num_decimal_places": 0},
        include_numbers = True,
        include_tip = True
        )
        axes.add_coordinates()
        axes.scale(0.75)
        line.next_to(axes, DOWN, buff = 0.5)
        line.scale(0.75)
        function = MathTex("f(ax) = (ax)^2", color = BLUE_C).next_to(axes, UP, buff = 0.5)
        a_text = MathTex("a", color = BLUE_C).next_to(line, RIGHT, buff = 0.1)
        a = ValueTracker(1)
        tracker = Dot(point = line.number_to_point(a.get_value()), color = BLUE_C)
        tracker.add_updater(lambda m:m.become(Dot(point = line.number_to_point(a.get_value()), color = BLUE_C)))
        graph = axes.get_graph(lambda x: (x*a.get_value())**2, color = BLUE_C)
        graph.add_updater(lambda m: m.become(axes.get_graph(lambda x: (x*a.get_value())**2, color = BLUE_C)))

        self.play(Create(tracker), Write(line), Write(axes), Write(function), Write(a_text))
        self.add(graph)
        self.play(a.animate.increment_value(2))
        self.play(a.animate.increment_value(-2.5))

class ReciGraph1(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,5,1],
        y_range = [-2,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        axes.add_coordinates()
        axes.scale(0.8)
        initfunc = MathTex("f(x) = x^2 - 3x", color = BLUE_C).next_to(axes,UP, buff = 0.5)
        initfunc.shift(LEFT*3)
        finfunc = MathTex("\\frac{1}{f(x)} = \\frac{1}{x^2 - 3x}", color = BLUE_C).next_to(axes,UP,buff = 0.2)
        finfunc.shift(LEFT*3)
        initgraph = axes.get_graph(lambda x: (x**2 - 3*x),x_range = [-4,4], color = BLUE_C)
        fingraph_1 = axes.get_graph(lambda x : (1)/(x**2 - 3*x),x_range = [3.05,4,0.005], color = BLUE_C)
        fingraph_2 = axes.get_graph(lambda x : (1)/(x**2 - 3*x ),x_range = [-4,-0.05,0.005], color = BLUE_C)
        fingraph_3 = axes.get_graph(lambda x : (1)/(x**2 - 3*x ),x_range = [0.2,2.8,0.005], color = BLUE_C)
        fingraph = VGroup(fingraph_1,fingraph_2,fingraph_3)

        self.add(axes, initfunc, initgraph)
        self.play(FadeIn(fingraph), FadeOut(initgraph), Transform(initfunc,finfunc), run_time = 3)

class EvenFunc(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,5,1],
        y_range = [-5,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        axes.scale(0.9)
        func = MathTex("f(x) = f(-x) = x^2", color = BLUE_C).next_to(axes,UP, buff = 0.5)
        text = Text("Even Function",color = BLUE_C).next_to(axes,DOWN, buff = 0.5)
        initgraph = axes.get_graph(lambda x: (x**2) ,x_range = [0,4], color = BLUE_C)
        fingraph = axes.get_graph(lambda x: (x**2) ,x_range = [-4,0], color = BLUE_C)
        self.add(axes, func, initgraph, text)
        self.play(Write(fingraph), run_time = 2)

class OddFunc(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,5,1],
        y_range = [-5,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        axes.scale(0.9)
        func = MathTex("f(x) = -f(-x) = x^3", color = BLUE_C).next_to(axes,UP, buff = 0.5).scale(0.8)
        text = Text("Odd Function",color = BLUE_C).next_to(axes,DOWN, buff = 0.5)
        trans1 = Text("Reflection 1",color = BLUE_C).next_to(axes,DOWN, buff = 0.5)
        trans2 = Text("Reflection 2",color = BLUE_C).next_to(axes,DOWN, buff = 0.5)
        initgraph = axes.get_graph(lambda x: (x**3) ,x_range = [0,4], color = BLUE_C)
        fingraph_1 = axes.get_graph(lambda x: -(x**3) ,x_range = [-4,0], color = BLUE_C)
        fingraph_2 = axes.get_graph(lambda x: (x**3) ,x_range = [-4,0], color = BLUE_C)
        self.add(axes, func, initgraph, text)
        self.play(Write(fingraph_1),Transform(text,trans1), run_time = 2)
        self.play(Transform(fingraph_1,fingraph_2),Transform(trans1,trans2),run_time = 2)

class EnvelopeGraph(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range = [-5,3,1],
        y_range = [-5,5,1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        func = MathTex("f(x) = e^x \\sin (3x)", color = BLUE_C).next_to(axes,UP, buff = 0.5).scale(0.8)
        exp = axes.get_graph(lambda x: math.e**x, color = TEAL_B)
        exp_2 = axes.get_graph(lambda x: -math.e**x, color = TEAL_B)
        graph = axes.get_graph(lambda x: (math.e**x)*math.sin(3*x), color = BLUE_C)
        self.add(axes,exp,exp_2,graph,func)

class DiffGraph(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range=[0, 3, 1],
        y_range=[0, 5, 1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        axes.scale(0.7)
        axes.add_coordinates()
        labels = axes.get_axis_labels().set_color(logo_blue)
        func = MathTex("f_1(x) = \\left( \\frac{1}{x} \\right)^{12}", color = TEAL_B).next_to(axes,UP, buff = 0.5).scale(0.8)
        func_2 = MathTex("f_2(x) = \\left( \\frac{1}{x} \\right)^{6}", color = GOLD_B).next_to(func,RIGHT, buff = 3).scale(0.8)
        func.shift(RIGHT*3)
        g1 = axes.get_graph(lambda x: (1/x)**(12), x_range =[0.8,3,0.01], color = TEAL_B)
        g2 = axes.get_graph(lambda x: (1/x)**(6), x_range =[0.70,3,0.01], color = GOLD_B)
        self.add(axes,g1,g2,func,func_2, labels)

class LJGraph(Scene):
    def construct(self):
        self.camera.background_color = background_blue
        axes = Axes(
        x_range=[0, 3, 1],
        y_range=[0, 2, 1],
        axis_config = {'color':logo_blue, "decimal_number_config": {"color": logo_blue, "num_decimal_places": 0}},
        )
        axes.scale(0.7)
        axes.add_coordinates()
        labels = axes.get_axis_labels().set_color(logo_blue)
        func = MathTex("V_{LJ}(x) = \\left( \\frac{1}{x} \\right)^{12} - \\left( \\frac{1}{x} \\right)^{6}", color = RED).next_to(axes,UP, buff = 0.5).scale(0.8)
        func.shift(RIGHT*2)
        g1 = axes.get_graph(lambda x: (1/x)**(12) - (1/x)**(6), x_range =[0.8,3,0.01], color = RED)
        self.add(axes,g1,func, labels)
