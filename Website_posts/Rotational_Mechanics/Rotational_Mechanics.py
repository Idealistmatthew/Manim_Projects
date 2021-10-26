from manim import *
import math
logo_blue = "#0633D6"
background_blue = "#F1F8FF"

class Spinning_Stuff(ThreeDScene):
    def construct(self):
        self.camera.background_color = background_blue
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        sphere = Sphere(center = [1,1,1], radius = 1.5, resolution = (16,16))
        sphere.set_color(logo_blue)
        prism = Prism(dimensions= [1,2,3]).move_to([-2,-2,-2])
        self.add(sphere)
        self.add(prism)
        self.play(Rotate(sphere), Rotate(prism))

class Rotating_logo(ThreeDScene):
    def construct(self):
        self.camera.background_color = background_blue
        self.set_camera_orientation(phi=2*PI / 6, theta= 0)
        prism_ilong = Prism(dimensions = [0.4,0.4,4]).move_to([3,1,0]).set_color(logo_blue)
        prism_iup = Prism(dimensions = [0.22,3,0.22]).move_to([3,1,2]).set_color(logo_blue)
        prism_idown = Prism(dimensions = [0.22,3,0.22]).move_to([3,1,-2]).set_color(logo_blue)
        I = VGroup(prism_ilong,prism_iup,prism_idown)
        self.add(I)
        # self.play(Rotate(I))
