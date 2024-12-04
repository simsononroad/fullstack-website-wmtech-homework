import hashlib
def normal_to_hash(atalakitando, encode):
    password = atalakitando
    if encode == "":
        encode = "UTF-8"
    password_hash = hashlib.sha256(password.encode(encode)).hexdigest()
    return password_hash

