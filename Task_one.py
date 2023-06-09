# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами
# не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

while True:
    try:
        a = int(input("Введите длину первой стороны треугольника: "))
        b = int(input("Введите длину второй стороны треугольника: "))
        c = int(input("Введите длину третьей стороны треугольника: "))
        print("Вы ввели следующие числа: а = {0}, b = {1}, c = {2}".format(a, b, c))
        break
    except ValueError:
        print("Вы неправильно ввели данные, повторите ввод.")
if (a <= b + c) & (b <= a + c) & (c <= a + b):
    print("Есть такой треугольник.")
    if a == b == c:
        print("Треугольник равносторонний.")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний.")
else:
    print("С такими данными треугольника не может быть.")

