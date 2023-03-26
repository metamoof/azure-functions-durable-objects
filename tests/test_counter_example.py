import durable_objects


class DurableCounter(durable_objects.DurableObject):
    def __init__(self, value=0):
        self.value = value

    def add(self, amount):
        self.value += amount

    def reset(
        self,
    ):
        self.value = 0


def test_durable_counter_raw():
    counter = DurableCounter()
    assert counter.value == 0
    counter.add(3)
    assert counter.value == 3
    counter.add(5)
    assert counter.value == 8
    counter.reset()
    assert counter.value == 0
    counter.add(2)
    assert counter.value == 2
    counter.add(1)
    assert counter.value == 3
    counter = DurableCounter(4)
    assert counter.value == 4
    counter.add(6)
    assert counter.value == 10
    counter.reset()
    assert counter.value == 0
    counter.add(7)
    assert counter.value == 7
