from random import choice, seed
import numpy as np
import math
from manim import *

seed(8)
def coin_flip_sim(initial_capital, betting_fraction, iterations):
  wealth = [initial_capital]
  current_capital = initial_capital
  num_flips = [0]
  for i in range(iterations):
    result = choice([(50/49)*betting_fraction*current_capital,
                     -1*betting_fraction*current_capital])
    current_capital += result
    wealth.append(current_capital)
    num_flips.append(i+1)
  return [wealth, num_flips]


data_1 = coin_flip_sim(100, 1/500, 150)
data_2 = coin_flip_sim(100, 1/100, 150)
data_3 = coin_flip_sim(100, 1/5, 150)
data_4 = coin_flip_sim(100, 1, 150)
x_1, y_1 = data_1[1], data_1[0]
x_2, y_2 = data_2[1], data_2[0]
x_3, y_3 = data_3[1], data_3[0]
x_4, y_4 = data_4[1], data_4[0]

class Coin_flip_ani(Scene):
    def construct(self):
        axes_1 = Axes(
        x_range =
        )
