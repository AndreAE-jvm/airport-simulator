# from plane import Plane
# from airport_simulator import AirportSimulator
#
# # Создаем аэропорт
# airport = AirportSimulator()
#
# # Создаем рейсы
# flights = [
#     Plane("SU100", "Аэрофлот", "Лондон"),
#     Plane("BA123", "British Airways", "Нью-Йорк"),
#     Plane("LH456", "Lufthansa", "Берлин")
# ]
#
# # Добавляем рейсы
# for flight in flights:
#     print(airport.add_flight(flight))
#
# # Назначаем выходы
# print(airport.assign_gate("SU100", "A15"))
# print(airport.assign_gate("BA123", "B22"))
#
# # Начинаем посадку
# print(airport.start_boarding("SU100"))
#
# # Показываем статус
# airport.display_status()
#
# # Вылетаем
# print(airport.depart_flight("SU100"))
#
# # Финальный статус
# airport.display_status()
#
# # Сохраняем лог
# print(airport.export_log("simple_airport_log.json"))


from plane import Plane
from airport_simulator import AirportSimulator


def main():
    # Создаем симулятор аэропорта
    airport = AirportSimulator()

    print("СИМУЛЯТОР АЭРОПОРТА")

    # Создаем несколько рейсов
    flight1 = Plane("SU100", "Аэрофлот", "Лондон")
    flight2 = Plane("BA123", "British Airways", "Нью-Йорк")
    flight3 = Plane("LH456", "Lufthansa", "Берлин")
    flight4 = Plane("EY789", "Etihad", "Дубай")

    print("\n1. Добавляем рейсы в расписание:")
    print(airport.add_flight(flight1))
    print(airport.add_flight(flight2))
    print(airport.add_flight(flight3))
    print(airport.add_flight(flight4))

    print("\n2. Назначаем выходы на посадку:")
    print(airport.assign_gate("SU100", "A15"))
    print(airport.assign_gate("BA123", "B22"))
    print(airport.assign_gate("LH456", "C07"))

    print("\n3. Начинаем посадку на некоторые рейсы:")
    print(airport.start_boarding("SU100"))
    print(airport.start_boarding("LH456"))

    print("\n4. Задерживаем один рейс:")
    print(airport.delay_flight("BA123", "технические неполадки"))

    print("\n5. Отображаем текущий статус всех рейсов:")
    airport.display_status()

    print("\n6. Отправляем рейс SU100:")
    print(airport.depart_flight("SU100"))

    print("\n7. Пытаемся отправить рейс, который еще не на посадке:")
    print(airport.depart_flight("EY789"))  # Должен вернуть ошибку

    print("\n8. Отображаем финальный статус:")
    airport.display_status()

    print("\n9. Экспортируем лог событий:")
    print(airport.export_log("airport_log.json"))

    print("\nДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")


def demo_serialization():
    """Демонстрация работы сериализации/десериализации"""
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ СЕРИАЛИЗАЦИИ")
    print("=" * 50)

    # Создаем и настраиваем рейс
    original_plane = Plane("TEST777", "Test Airlines", "Токио")
    original_plane.assign_gate("Z99")
    original_plane.start_boarding()

    print("Исходный объект:")
    print(f"  Рейс: {original_plane.flight_number}")
    print(f"  Статус: {original_plane.status}")
    print(f"  Выход: {original_plane.gate}")

    # Сериализуем в словарь
    plane_dict = original_plane.to_dict()
    print(f"\nСловарь после to_dict(): {plane_dict}")

    # Десериализуем обратно в объект
    restored_plane = Plane.from_dict(plane_dict)
    print("\nВосстановленный объект:")
    print(f"  Рейс: {restored_plane.flight_number}")
    print(f"  Статус: {restored_plane.status}")
    print(f"  Выход: {restored_plane.gate}")


if __name__ == "__main__":
    main()
    demo_serialization()