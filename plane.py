# Класс Plane

# Поля:
# • flight_number
# • airline
# • destination
# • status — "scheduled", "boarding", "departed", "delayed"
# • gate — None или строка

# Методы:
# • assign_gate(gate)
# • start_boarding()
# • delay(reason)
# • depart()

class Plane:
    def __init__(self, flight_number, airline, destination):
        self.flight_number = flight_number
        self.airline = airline
        self.destination = destination
        self.status = "scheduled"  # "по расписанию"
        self.gate = None

    def assign_gate(self, gate):
        """Назначить выход на гейт(выход на посадку в самолет)"""
        if self.status != "departed":  # "вылетел"
            self.gate = gate
            return f"Выход: {gate} назначен для рейса: {self.flight_number}"
        return f"Невозможно назначить выход для вылетевшего рейса"

    def start_boarding(self):
        """Начать посадку"""
        if self.status in ["scheduled", "delayed"]:  # "по расписанию", "задержан"
            self.status = "boarding"
            return f"Посадка начата для рейса: {self.flight_number}"
        return f"Невозможно начать посадку. Текущий статус: {self.status}"

    def delay(self, reason):
        """Задержать рейс"""
        if self.status != "departed":
            self.status = "delayed"  # "задержан"
            return f"Рейс {self.flight_number} задержан. Причина: {reason}"
        return "Невозможно задержать вылетевший рейс "

    def depart(self):
        """Вылететь"""
        if self.status == "boarding":
            self.status = "departed"
            return f"Рейс {self.flight_number} вылетел"
        return f"Невозможно вылететь. текущий статус: {self.status}"

    def to_dict(self):
        """Преобразовать объект Plane в словарь для сериализации"""
        return {
            "flight_number": self.flight_number,
            "airline": self.airline,
            "destination": self.destination,
            "status": self.status,
            "gate": self.gate,
        }

    # возвращаем объект
    # загрузка данных
    @staticmethod
    def from_dict(data):
        """Создать объект Plane из словаря (статический метод)"""
        # Создаем объект с обязательными полями
        plane = Plane(
            data["flight_number"],
            data["airline"],
            data["destination"]
        )
        # Устанавливаем дополнительные поля если они есть в данных
        plane.status = data.get("status", "scheduled")  # по умолчанию "scheduled"
        plane.gate = data.get("gate", None)  # по умолчанию None

        return plane


# # Создаем объект
# plane = Plane("SU100", "Аэрофлот", "Лондон")
# plane.assign_gate("A15")
#
# # Сериализуем в словарь
# plane_dict = plane.to_dict()
# print(plane_dict)
#
# # Десериализуем из словаря
# restored_plane = Plane.from_dict(plane_dict)
# print(restored_plane)
