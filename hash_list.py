import sys
import hash_it

md5_hashes = []
sha1_hashes = []
sha256_hashes = []
sha512_hashes = []

# select new file to analyze.
new_file_name = input('Please enter the name of the file you wish to analyze.\n: ')
# rush the file through the hash algorithms in hash_it.
new_md5 = hash_it.md5_hash(new_file_name)
new_sha1 = hash_it.sha1_hash(new_file_name)
new_sha256 = hash_it.sha256_hash(new_file_name)
new_sha512 = hash_it.sha512_hash(new_file_name)
# print out the hash values
print("The MD5 hash value of: ", new_file_name, " is: ", new_md5)
print("The SHA1 hash value of: ", new_file_name, " is: ", new_sha1)
print("The SHA256 hash value of: ", new_file_name, " is: ", new_sha256)
print("The SHA512 hash value of: ", new_file_name, " is: ", new_sha512)

# add each hash to each list
md5_hashes.append(new_md5)
sha1_hashes.append(new_sha1)
sha256_hashes.append(new_sha256)
sha512_hashes.append(new_sha512)

# print the lists
print("Here is your list of MD5 hashes:\n", md5_hashes)
print("Here is your list of SHA1 hashes:\n", sha1_hashes)
print("Here is your list of SHA256 hashes:\n", sha256_hashes)
print("Here is your list of SHA512 hashes:\n", sha512_hashes)

# exit the program

sys.exit()
