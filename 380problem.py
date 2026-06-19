import random

class RandomizedSet:
    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)


# ---- driver code to simulate LeetCode's test runner ----
if __name__ == "__main__":
    operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    args = [[], [1], [2], [2], [], [1], [2], []]

    output = []
    obj = None

    for op, arg in zip(operations, args):
        if op == "RandomizedSet":
            obj = RandomizedSet()
            output.append(None)
        elif op == "insert":
            output.append(obj.insert(arg[0]))
        elif op == "remove":
            output.append(obj.remove(arg[0]))
        elif op == "getRandom":
            output.append(obj.getRandom())

    print(output)