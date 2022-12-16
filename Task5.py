# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# point_a = []
# for i in range(2):
#     point_a.append(int(input('Введите координаты точки А: ')))
# point_b = []
# for i in range(2):
#     point_b.append(int(input('Введите координаты точки B: ')))
# distance = round((((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2) ** 0.5), 2)
# print(distance)

x1 = int(input('Введите координату х точки А: '))
y1 = int(input('Введите координату y точки А: '))
x2 = int(input('Введите координату х точки B: '))
y2 = int(input('Введите координату y точки B: '))
distance = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 2)
print(f'A ({x1},{y1}); B ({x2},{y2}) -> {distance}')

