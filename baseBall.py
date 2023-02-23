    def calPoints(self, operations: List[str]) -> int:
        newRecord = []
        for i in operations:
            if newRecord and i == "+" :
                newRecord.append(newRecord[-1]+newRecord[-2])
            elif newRecord and i == "C":
                del newRecord[-1]
            elif newRecord and i == "D":
                newRecord.append(newRecord[-1] * 2)
            else:
                newRecord.append(int(i))
        return sum(newRecord)
