class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        if len(self._data) == 0:
            return 0
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.__len__() is not None:
            return self._data.pop(0)
        return None

    def search(self, indexParams):
        if (type(indexParams) != int or len(self._data)-1 < indexParams
                or indexParams < 0):
            raise IndexError("O Index passado é inválido...")

        for eachIndex in range(self.__len__()):
            if indexParams == eachIndex:
                return self._data[indexParams]
