class user:
    def __init__(self, first_name, last_name, email, age):
        self.firstname = first_name
        self.lastname = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print('this user',self.firstname, self.lastname, self.email, self.age, sep= "\n")
    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a member.')
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True 

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self.gold_card_points


andriy = user('Andriy', 'Ostapyuk', 'ostapyuk@gmail.com', '22')
andriy.display_info()
andriy.enroll()
print(andriy.spend_points(50))

        