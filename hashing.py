import bcrypt


def encryption(password):

    bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes, salt)

    print(hash)

    return hash


def decryption(password, hash_password):

    bytes = password.encode("utf-8")

    result = bcrypt.checkpw(bytes, hash_password)

    print(result)

    return result
