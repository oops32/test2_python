url = "https://test.com"
jwt = "eyJhbGciPiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
user = "admin"
password = "qwerty@123"
awsKey = "ASIAZIQ5SEG4MYAZQHT5"
username = input("Who are you? ")
if username == user:
    pas = input("Give me your password!! ")
    if pas == password:
        print("Login Success.")
        print("here is you jwt token : " + jwt)