from db import mycursor

def emailCheck(email):
    query = f"SELECT * From `users` Where `Email` = '{email}'"
    mycursor.execute(query)
    res = mycursor.fetchall()
    numOfUser = len(res)
    if (numOfUser > 0):
        return "User Already Exists", False
    else:
        return True

def register(name, email, phone, password):
    query = f""

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
