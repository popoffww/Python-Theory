time = int(input())
hour = time // 60
minutes = time % 60
print(time, 'мин - это', hour, 'час', minutes, 'минут.')


class TimeConverter:
    def __init__(self, value, list_key="hour"):
        self.value=value
        self.list_key=list_key
        self.list={"hour": 1, "min": 60, "sec": 3600}

    def converter(self):
        result = self.value // self.list[self.list_key], self.value % self.list[self.list_key]
        return result

    def __str__(self):
        return str(self.converter())

    def __call__(self):
        print(f"{self.value} минут составляет {self} часа")

if __name__ == "__main__":
    TimeConverter(value=int(input()), list_key="min")()
                 