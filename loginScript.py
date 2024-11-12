from db import mycursor


def login(username, password):
    query = f"SELECT * FROM `users` WHERE `username` = '{username}'"

    mycursor.execute(query)

    res = mycursor.fetchall()

    numberOfUsers = len(res)

    if (numberOfUsers != 1):
        return "Incorrect username or password", False
    else:
        dbPass = res[0][3]
        if (password == dbPass):
            return "Login successful!", True
        else:
            return "Incorrect username or password", False
