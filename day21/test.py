from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name}, {self.job}, ({self.age})'


person1 = Person("Tomas", "SalesManager", 26, 99)
person2 = Person("Anna", "Dancer", 23)
person3 = Person("Anna", "Dancer", 23)

print(id(person2))
print(id(person3))
print(person1)

print(person1 > person2)
