class Transport:
    def __init__(self, name, distance, time):
        self.name = name
        self.distance = distance
        self.time = time

class Route:
    def __init__(self, transport, next_transport=None):
        self.transport = transport
        self.next_transport = next_transport

class Planner:
    def __init__(self):
        self.routes = []

    def add_route(self, transport, next_transport=None):
        self.routes.append(Route(transport, next_transport))

    def plan_route(self, start, end):
        current_transport = None
        for route in self.routes:
            if route.transport.name == start:
                current_transport = route
                break
        if current_transport is None:
            return "Boshlanish joyi topilmadi"
        current_transport = current_transport.next_transport
        route = []
        while current_transport is not None:
            route.append(current_transport.transport.name)
            current_transport = current_transport.next_transport
        return route

# Hardcode qismlar
planner = Planner()
planner.add_route(Transport("Metro", 10, 30), Transport("Trolleybus", 20, 40))
planner.add_route(Transport("Trolleybus", 20, 40), Transport("Avtobus", 30, 50))
planner.add_route(Transport("Avtobus", 30, 50), Transport("Taksi", 5, 10))

print(planner.plan_route("Metro", "Taksi"))
```

Kodda quyidagilar mavjud:

- `Transport` klasi transport vositalarini ifodalaydi.
- `Route` klasi transport vositalarini bir-biriga bog'laydi.
- `Planner` klasi transport vositalarini qo'shish va yo'nalishni tuzish uchun metodlar beradi.
- `plan_route` metod yo'nalishni tuzib qaytaradi.
- Hardcode qismlar transport vositalarini qo'shish uchun ishlatiladi.
