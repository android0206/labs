import json


# TODO решите задачу
def task() -> float:
    with open("input.json") as inpfile:
        data = json.load(inpfile)
        multiply = [dict_["score"] * dict_["weight"] for dict_ in data]
        return round(sum(multiply), 3)


print(task())
