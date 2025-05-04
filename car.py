class Car:
    def __init__(self, name, mass, max_speed, length):
        self._name = name
        self._mass = mass
        self._max_speed = max_speed
        self._length = length
        
    def max_impulse(self):
        return self._mass * self._max_speed
    
    def __len__(self):
        return self._length
    
    def __str__(self):
        return f"i am a {self._name}"
    
ford = Car("ford", 1.5, 100, 3)