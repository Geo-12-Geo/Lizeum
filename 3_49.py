starts = [float(x) for x in input().split()]
ends = [float(x) for x in input().split()]
interval_coordinates = zip(starts, ends) # zip объединяет в кортежи элементы из последовательностей переданных в качестве аргументов.
length_with_coords = [(coords[1] - coords[0], coords) for coords in interval_coordinates]
longest_interval_with_length = sorted(length_with_coords)[-1] # функция sorted() возвращает список каждый раз, несмотря на то, какой тип был передан. 
longest_interval_coords = longest_interval_with_length[1]
print(*longest_interval_coords)