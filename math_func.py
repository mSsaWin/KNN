import math
def dot(v, w): # скалярное произведение векторов
  return sum(v_i * w_i for v_i, w_i in zip(v, w))
def sum_of_squares(v): # квадрат модуля вектора
  return dot(v, v)
def scalar_multiply(c, v): # умножение вектора v на число c
  return [c * v_i for v_i in v]
def vector_add(v,w): # сложение векторов
  return [v_i + w_i for v_i,w_i in zip(v, w)]
def squared_distance(v, w): # квадрат расстояния
  return sum_of_squares(vector_add(v, scalar_multiply(-1, w)))
def distance(v, w): # расстояние
  return math.sqrt(squared_distance(v, w))
  