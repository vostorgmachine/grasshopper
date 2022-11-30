# Совместить оба блока с питоновым кодом в один массивный. По возможности
# перенести максимум элементов из grasshopper в python.

import rhinoscriptsyntax as rs

# Блок с viborka rectangle:

viborka_x_size = main_rectangle_x_size - 120
viborka_y_size = float(main_rectangle_y_size) - float(rifle_length) - float(120)

viborka_x_size = float(viborka_x_size) 
viborka_y_size = float(viborka_y_size)

print()
print("Ширина выборки: ")
print(viborka_x_size)
print()
print("Высота выборки: ")
print(viborka_y_size)
print()

# Стартовая точка для выборки:

viborka_x_point_res = viborka_x_point + 60
viborka_y_point_res = viborka_y_point + 60

# Rifle end line block

# start_point:
end_line_x_dot_1 = main_x_coordinate - 5
end_line_y_dot_1 = main_y_coordinate + main_rectangle_y_size - rifle_length

# end_point:
end_line_x_dot_2 = main_x_coordinate + main_rectangle_x_size + 5
end_line_y_dot_2 = main_y_coordinate + main_rectangle_y_size - rifle_length

# rifle (rifle lines)

amount_of_lines = main_rectangle_x_size // 10
amount_of_lines = int(amount_of_lines)

rifle_y_start_point = main_rectangle_y_size - rifle_length

# Логика с формированием рифлёнки. Основная задача состоит в том, чтобы сделать
# такую логику, которая при чётном значении переменной list_lenght удаляет
# последнюю точку в списке и соответствующим образом меняет прочие параметры.

# Построение логики для автоматизации рифлёнки.

rifle_step = main_rectangle_x_size - (amount_of_lines * 10) 
rifle_x_line_size = int(rifle_step) / amount_of_lines
rifle_x_line_size = rifle_x_line_size + 10
rifle_x_scaling = rifle_x_line_size / 10

rifle_start_position_y = main_rectangle_y_size - rifle_length
rifle_start_position_y = rifle_start_position_y +  main_y_coordinate + 1
rifle_start_position_y = float(rifle_start_position_y)

rifle_y_size = rifle_length + 4
rifle_y_size = int(rifle_y_size)

print()
print("Кол-во рифлёнок: ")
print(amount_of_lines)
print()
print("Множитель (для компонента scaling)")
print(rifle_x_scaling)
print()

# if list_lenght % 2 == 0:
#     print(int(1))
# else:
#     print(int(0))
