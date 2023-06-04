import unittest


def kmi(svoris, ugis):
    if svoris < 20 or svoris > 239 or ugis <= 0.4 or ugis >= 2.5:
        raise ValueError("Invalid weight or height value")

    kmi_reiksme = svoris / (ugis ** 2)
    return round(kmi_reiksme, 14)


if __name__ == "__main__":
    unittest.main()
