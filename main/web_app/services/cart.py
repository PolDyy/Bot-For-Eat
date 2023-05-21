from flask import session
from typing import Dict
import json


class Cart:
    def __init__(self):
        if session.get("order"):
            self.order = self._load_json(session.get("order"))
        else:
            self.order: Dict[str, (int, dict)] = {
                'total_cost': 0,
                "product_id": 0
            }

    def add_product(self, product: dict):
        index = str(self.order["product_id"])
        values = self.order.values()
        if product not in values:
            self.order[index] = product
            self.order["product_id"] += 1
        else:
            index = list(filter(lambda x: self.order[x] == product, self.order))[0]
            self.order[index]["quantity"] += 1
        self.order["total_cost"] += int(product["cost"])
        self._save_order()

    def remove(self, product: dict):
        index = list(filter(lambda x: self.order[x] == product, self.order))[0]
        product_in_order = self.order[index]
        if product_in_order['quantity'] == 1:
            del product_in_order
        else:
            product['quantity'] -= 1
        self.order["total_cost"] -= int(product['cost'])
        self._save_order()

    def _save_order(self):
        session['order'] = self._dump_json(self.order)
        session.modified = True

    @staticmethod
    def _load_json(order):
        return json.loads(order)

    @staticmethod
    def _dump_json(order):
        return json.dumps(order, ensure_ascii=False)
