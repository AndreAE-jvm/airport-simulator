# Класс AirportSimulator

# Хранилища:
# • scheduled_flights — список рейсов
# • log — список всех событий


# Методы:
# • add_flight(plane)
# • assign_gate(flight_number, gate)
# • start_boarding(flight_number)
# • delay_flight(flight_number, reason)
# • depart_flight(flight_number)
# • display_status()
# • export_log(filename)
# Сохранение лога в JSON.



import json
from datetime import datetime
from plane import Plane


class AirportSimulator:
    def __init__(self):
        self.scheduled_flights = []
        # Лог остается, но заполняется только в ключевых методах
        self.log = []


    """Используем метод _find_flight для поиска рейса по номеру в списке scheduled_flights.
Это вспомогательный метод, который используется в нескольких других методах класса AirportSimulator 
(таких как assign_gate, start_boarding, delay_flight, depart_flight).
Благодаря этому избегаем повторения одного и того же кода поиска в каждом из этих методов.
Метод возвращает объект Plane (рейс) если найден, или None если рейс с таким номером не существует."""

    """метод не предназначен для использования извне класса (protected)
Его нужно вызывать только внутри других методов класса AirportSimulator"""

    def _find_flight(self, flight_number):
        for flight in self.scheduled_flights:
            if flight.flight_number == flight_number:
                return flight
        return None

    def add_flight(self, plane):
        """Добавить рейс в расписание - логируем только это"""
        if not isinstance(plane, Plane):
            return "Ошибка: можно добавлять только объекты класса Plane"

        self.scheduled_flights.append(plane)

        # Логируем только добавление рейса
        log_entry = {
            "timestamp": datetime.now().isoformat(),  #создание временной метки в стандартном формате
            "event": f"Добавлен рейс {plane.flight_number}",
            "details": f"{plane.airline} в {plane.destination}"
        }
        self.log.append(log_entry)

        return f"Рейс {plane.flight_number} добавлен в расписание"

    def assign_gate(self, flight_number, gate):
        """ Назначение выходов"""
        flight = self._find_flight(flight_number)
        if flight:
            return flight.assign_gate(gate)
        return f"Рейс {flight_number} не найден"

    def start_boarding(self, flight_number):
        """Начало посадки """
        flight = self._find_flight(flight_number)
        if flight:
            return flight.start_boarding()
        return f"Рейс {flight_number} не найден"

    def delay_flight(self, flight_number, reason):
        """Задержки рейсов"""
        flight = self._find_flight(flight_number)
        if flight:
            result = flight.delay(reason)

            # Логируем только задержки - это важные события
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "event": f"Задержан рейс {flight_number}",
                "details": f"Причина: {reason}"
            }
            self.log.append(log_entry)

            return result
        return f"Рейс {flight_number} не найден"

    def depart_flight(self, flight_number):
        """выполняет отправку рейса (вылет), отметить рейс как "вылетевший" в системе аэропорта"""
        flight = self._find_flight(flight_number)
        if flight:
            result = flight.depart()
            # Логируем вылеты - это ключевые события
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "event": f"Вылетел рейс {flight_number}",
                "details": f"Направление: {flight.destination}"
            }
            self.log.append(log_entry)

            return result
        return f"Рейс {flight_number} не найден"

    def display_status(self):
        print("\nТЕКУЩИЙ СТАТУС РЕЙСОВ")
        print(f"{'Рейс':<10} {'Авиакомпания':<15} {'Направление':<15} {'Статус':<12} {'Выход':<6}")
        print("-" * 65)
        for flight in self.scheduled_flights:
            gate_display = flight.gate if flight.gate else "---"
            status_translation = {
                "scheduled": "по расписанию",
                "boarding": "посадка",
                "departed": "вылетел",
                "delayed": "задержан"
            }
            status_display = status_translation.get(flight.status, flight.status)
            print(
                f"{flight.flight_number:<10} {flight.airline:<15} {flight.destination:<15} {status_display:<12} {gate_display:<6}")

    def export_log(self, filename):
        """Экспортировать лог в JSON файл"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.log, f, ensure_ascii=False, indent=2)
            return f"Лог экспортирован в файл {filename}"
        except Exception as e:
            return f"Ошибка при экспорте лога: {e}"
