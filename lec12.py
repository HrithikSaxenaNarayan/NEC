class Lec12:

    @staticmethod
    def input(n):
        map_data = {}

        for i in range(n):
            map_data[i] = int(input())

        return map_data

    @staticmethod
    def display(map_data):
        for key, value in map_data.items():
            print(f"{key}: {value}")

    @staticmethod
    def display_gen(map_data):
        for key, value in map_data.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    pass