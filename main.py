from plane import Plane
from airport_simulator import AirportSimulator


def main():
    airport = AirportSimulator()
    print("СИМУЛЯТОР АЭРОПОРТА")

    airport.add_flight(Plane("SU100", "Аэрофлот", "Лондон"))
    airport.add_flight(Plane("BA123", "British Airways", "Нью-Йорк"))
    airport.add_flight(Plane("LH456", "Lufthansa", "Берлин"))
    airport.add_flight(Plane("EY789", "Etihad", "Дубай"))

    airport.assign_gate("SU100", "A15")
    airport.start_boarding("SU100")
    airport.delay_flight("BA123", "технические неполадки")

    print("Текущий статус рейсов:")
    airport.display_status()

    airport.depart_flight("SU100")
    airport.depart_flight("EY789")

    print("\nФинальный статус рейсов:")
    airport.display_status()

    airport.export_log("airport_log.json")
    print("Лог экспортирован")


if __name__ == "__main__":
    main()