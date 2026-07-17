"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self):
        self.usernames = []

    def add_user(self, username):
        self.usernames.append(username)

    def get_users(self):
        return self.usernames


# код писать тут
class AdminManager(UserManager):

    def ban_username(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
            print(f"Пользователь заблокирован: {username}")
        else:
            self.render_message()

    def render_message(self, msg = "Такого пользователя не существует."):
        print(msg)
        
class SuperAdminManager(AdminManager):

    def ban_all_users(self):
        print(f"Пользователи заблокированы: {', '.join(self.usernames)}")
        self.usernames.clear()




if __name__ == '__main__':

    
    userManager1 = UserManager()
    usernames = ['A', 'B', 'C']

    userManager1.usernames = usernames
    userManager1.add_user('D')
    print(userManager1.get_users())


    adminManager1 = AdminManager()
    usernames = ['A', 'B', 'C']

    adminManager1.usernames = usernames
    adminManager1.add_user('D')
    print(adminManager1.get_users())
    adminManager1.ban_username('D')
    adminManager1.ban_username('E')
    print(adminManager1.get_users())
    

    superAdminManager1 = SuperAdminManager()
    usernames = ['A', 'B', 'C']

    superAdminManager1.usernames = usernames
    superAdminManager1.add_user('D')
    print(superAdminManager1.get_users())
    superAdminManager1.ban_username('D')
    superAdminManager1.ban_username('E')
    superAdminManager1.ban_all_users()
    print(superAdminManager1.get_users())






