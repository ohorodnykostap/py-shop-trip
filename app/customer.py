import math
from typing import Dict, List
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: List[float],
        money: float,
        car: Dict[str, float]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
        self.home_location = location[:]

    def distance_to(self, shop_location: List[float]) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        return math.dist([x1, y1], [x2, y2])

    def products_total(self, shop_products: Dict[str, float]) -> float:
        total = 0.0
        for product, qty in self.product_cart.items():
            total += shop_products[product] * qty
        return total

    def go_to(self, location: List[float]) -> None:
        self.location = location[:]

    def go_home(self) -> None:
        self.location = self.home_location[:]
