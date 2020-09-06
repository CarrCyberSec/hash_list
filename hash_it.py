import hashlib


def md5_hash(new_file_name):
    md5_alg = hashlib.md5()
    new_file = open(new_file_name, "rb")
    new_file_content = new_file.read()
    md5_alg.update(new_file_content)

    new_file_digest = md5_alg.hexdigest()

    return new_file_digest


def sha1_hash(new_file_name):
    sha1_alg = hashlib.sha1()
    new_file = open(new_file_name, "rb")
    new_file_content = new_file.read()
    sha1_alg.update(new_file_content)

    new_file_digest = sha1_alg.hexdigest()

    return new_file_digest


def sha256_hash(new_file_name):
    sha256_alg = hashlib.sha256()
    new_file = open(new_file_name, "rb")
    new_file_content = new_file.read()
    sha256_alg.update(new_file_content)

    new_file_digest = sha256_alg.hexdigest()

    return new_file_digest


def sha512_hash(new_file_name):
    sha512_alg = hashlib.sha512()
    new_file = open(new_file_name, "rb")
    new_file_content = new_file.read()
    sha512_alg.update(new_file_content)

    new_file_digest = sha512_alg.hexdigest()

    return new_file_digest
