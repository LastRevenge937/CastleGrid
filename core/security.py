import hashlib

def verify_password(input_pw: str, stored_hash: str) -> bool:
    return hashlib.sha256(input_pw.encode()).hexdigest() == stored_hash
