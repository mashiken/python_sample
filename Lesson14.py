class Student:
    def __init__(self,name):
        self.name = name
    
    def calculate_avg(self,date):
        sum = 0

        for num in date:
            sum += num
        
        avg = sum/len(date)
        return avg

    def jedge(self,avg):
        if (avg >= 60):
            result="passed"
        else:
            result="faild"
        return result

a001 = Student("sato")
date = [70,65,50,10,30]
avg = a001.calculate_avg(date)
result = a001.jedge(avg)

print(avg)
print(a001.name+" "+result)

a002 = Student("yamato")
date2 = [45,55,55,46,11]
avg2 = a002.calculate_avg(date)
result2 = a002.jedge(avg)


print(avg2)
print(a001.name+" "+result2)