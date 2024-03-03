from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(family, 1, 14))
print(slice_me(family, 3, 10))
print("-------------------------------")
family2 = [[1.80, 78.4],
           [2.15, 102.7],
           [2.10, 98.5, 5],
           [1.88, 75.2]]
print(slice_me(family2, 3, 10))
print(slice_me(family2, 1.5, -2))
print(slice_me(family2, 1, 2.5))
print(slice_me(family2, 1, 'yolo'))
print(slice_me(18, 1, 2))
