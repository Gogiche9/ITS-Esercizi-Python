#main

from users import User, Privileges, Admin


user1 = User("John", "Doe", "johndoe", "john.doe@example.com")
privileges = Privileges("Admin")
admin = Admin(user1, privileges)

admin.show_information()