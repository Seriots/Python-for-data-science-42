from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = [2.71, 1.15, 1.65]
weight = [165.3, 38.4, 58]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = [2, 1, 'yolo']
weight = [165, 38.4, 83]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

height = [2, 1]
weight = [165, 38.4, 83]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
print("-----")

print(apply_limit([1, 2, 3], 26))
print(apply_limit([1, 2, 3], 'yolo'))
print(apply_limit([1, 2, 3], 26.5))
print(apply_limit([1, 2, 'yolo'], 26))
print(apply_limit([1, 2.5, 3], 26))
