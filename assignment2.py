import socket

class Assignment2:
    def __init__(self, year): #task 1
        self.year = year

    def tellAge(self, currentYear): #task 2
        print("Your age is",currentYear - self.year)

    def listAnniversaries(self): #task 3
        a = []
        i= 10
        while i <= 2022 - self.year:
            if i % 10 == 0:
                a.append(i)
                i = i + 10
        return a

    def modifyYear(self, n): #task 4
        result = ""
        new = self.year
        num = str(new)

        for i in range(n):
            result += num[0] + num[1]

        x = str(self.year * n)
        num2 = ""
        for i in range(0, len(x)):
            if(i%2 == 0):
                num2 += x[i]
        return result + num2

    @staticmethod #task 5
    def checkGoodString(string): #task 5
        num = 0
        for i in range(0, len(string)):
            if(string[i].isdigit()):
                num = num + 1
                if(num > 1):
                    break
        return (len(string) >= 9 and string[0].islower() and num == 1)

    @staticmethod #task 6
    def connectTCP(host = str, port = int):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                return True
        except:
            return False






