class ConverterInFullMetre:

    def __init__(self, value: int, measure_unit: str = "m") -> None:
        self.value = value
        self.measure_unit = measure_unit # ключ словаря
        self.measures = {"m": 1, "dm": 10, "cm": 100, "mm": 1000} # словарь

    def converter(self) -> int:
        return self.value // self.measures[self.measure_unit]

    def __str__(self) -> str:
        return str(self.converter())

    def __call__(self) -> None:
        print(self)

if __name__ == "__main__":
    ConverterInFullMetre(value=int(input()), measure_unit="cm")()
