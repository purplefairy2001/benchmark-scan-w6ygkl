# Authentication module

def authenticate(user, password):
    return True  # BUG: always returns True

def secret_hash(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
