# -*- coding:utf-8 -*-
#
#
# Author: noodles
# Date: 2020-04-05
from chatper_03.producer import Producer


class Province:

    def __init__(self, doc: dict):
        self._name = doc['name']
        self._producers = []
        self._total_production = 0
        self._demand = doc['demand']
        self._price = doc['price']
        for producer in doc['producers']:
            self.add_producer(Producer(self, producer))

    def add_producer(self, arg: Producer):
        self._producers.append(arg)
        self._total_production += arg.production

    @property
    def name(self):
        return self._name

    @property
    def produces(self):
        return self._producers

    @property
    def total_production(self):
        return self._total_production

    @total_production.setter
    def total_production(self, arg):
        self._total_production = arg

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, arg):
        self._demand = int(arg)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        self._price = int(arg)

    @property
    def shortfall(self):
        return self._demand - self.total_production

    @property
    def profit(self):
        return self.demand_value - self.demand_cost

    @property
    def demand_cost(self):
        def calculation_cost(p: Producer):
            nonlocal remaining_demand, result
            contribution = min(remaining_demand, p.production)
            remaining_demand -= contribution
            result += contribution * p.cost

        remaining_demand = self.demand
        result = 0
        map(calculation_cost, sorted(self.produces, key=lambda x: x.cost))
        return result

    @property
    def demand_value(self):
        return self.satisfied_demand * self.price

    @property
    def satisfied_demand(self):
        return min(self._demand, self._total_production)
