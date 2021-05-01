class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


    def greetion(self):
        print('안녕하세요. 제 이름은 ' + self.name +'이고, 나이는 ' + self.age + '살이고, ' + self.address + '에서 거주합니다.' )


    @staticmethod
    def main():
        maria = Person('마리아', '10', '서울')
        maria.greetion()

        tom = Person('톰', '20', '인천')
        tom.greetion()


if __name__ == '__main__':
    Person.main()



