На Марс заброшена партия стационарных роботов-исследователей. Марсоход должен перевезти их на определённые точки планеты.

Для перевозки роботов есть неограниченное количество транспортных платформ, каждая из которых способна выдерживать определённый вес limit. На одной платформе можно перевезти либо одного робота, либо двух — при условии, что их совокупный вес не превышает limit. Роботы имеют разный вес.

Программа получает на вход массив, каждый элемент которого — это вес робота. Второй параметр — это значение limit, грузоподъёмность одной платформы.

Алгоритм определяет минимальное количество транспортных платформ, необходимое для перевозки всех роботов, описанных в массиве.

- Количество платформ неограниченно.
- Каждая платформа выдерживает максимальный вес limit.
- На каждой платформе можно перевезти не более двух роботов при условии, что их совокупный вес не превышает limit.
- Вес отдельного робота не может превышать limit.

Алгоритм основан на методе двух указателей, модернизированный под данную задачу.