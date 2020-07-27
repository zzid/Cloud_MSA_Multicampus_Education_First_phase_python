class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    # 함수의 첫번째 파라미터에 self 가 있어야 클래스에 속한 함수가 됩니다.
    # 파라미터명이 꼭 self 가 아니라도 됩니다.
    def change_back_number(self, new_number):
        print("{} 등번호 변경 : {} 에서 {} 로"
                    .format(self.name, self.back_number, new_number))
        self.back_number = new_number

    # toString() method와 동일한 역할
    # 객체의 주소가 아니라 객체가 가진 특정 인스턴스 값을 출력
    def __str__(self):
        return f'My name is {self.name}, I play in {self.position} in center'

    def introduce(self):
        return f'My name is {self.name}, my position is {self.position}, my back number is {self.back_number}'

