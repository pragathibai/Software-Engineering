def signup(username, password):
    if not username:
        return "Username is required"

    if len(password) < 6:
        return "Password must be at least 6 characters"

    return "Signup successful"


print(signup("John", "abc123"))
