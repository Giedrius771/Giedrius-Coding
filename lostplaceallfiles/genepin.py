def pin_generator(start_pin):
    pin = start_pin
    while True:
        yield pin
        pin = str(int(pin) + 1).zfill(4)
        if pin == start_pin:
            break


correct_pin = '0549'
generatorius = pin_generator('0000')

for pin in generatorius:
    print(pin)
    if pin == correct_pin:
        print(f"PIN is {correct_pin}")
        break
