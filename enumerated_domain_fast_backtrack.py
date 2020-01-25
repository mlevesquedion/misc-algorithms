class EnumeratedDomain:

    def __init__(self, cardinality):
        self.max_cardinality = cardinality
        self.cardinality = cardinality
        self.locations = list(range(cardinality))
        self.values = list(range(cardinality))

    def contains(self, value):
        return self.locations[value] < self.cardinality

    def remove(self, value):
        assert self.contains(value), f"domain does not contain {value}"
        value_location = self.locations[value]
        cardinality = self.values[self.cardinality - 1]
        cardinality_location = self.locations[cardinality]
        self.locations[value], self.locations[cardinality] = self.locations[cardinality], self.locations[value]
        self.values[value_location], self.values[cardinality_location] = self.values[cardinality_location], self.values[value_location]
        self.cardinality -= 1

    def restore(self, k):
        self.cardinality += k
        assert self.cardinality <= self.max_cardinality, "restored more values than maximum"

    def __str__(self):
        return f"""\
cardinality: {self.cardinality}
locations: {self.locations}
values:    {self.values}
domain:   {[v for v in self.values[:self.cardinality]]}"""

domain = EnumeratedDomain(5)
print(domain, end='\n\n')
for value in [2, 1, 3]:
    domain.remove(value)
    print(domain, end='\n\n')
domain.restore(2)
print(domain, end='\n\n')
domain.restore(1)
print(domain, end='\n\n')
domain.remove(4)
print(domain, end='\n\n')

