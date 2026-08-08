import crypt

def test_password(stored_hash, plaintext_password):
    """
    Compare a plaintext password against a stored hash.
    """
    return crypt.crypt(plaintext_password, stored_hash) == stored_hash


def read_dictionary(dictionary_file):
    """
    Read the dictionary file and return a list of passwords.
    """
    with open(dictionary_file, "r") as f:
        return f.read().splitlines()


def read_shadow(shadow_file):
    """
    Read a shadow-style file and return a list of
    (username, password_hash) tuples.
    """
    users = []

    with open(shadow_file, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            fields = line.split(":")

            if len(fields) < 2:
                continue

            username = fields[0]
            password_hash = fields[1]

            # Skip locked/disabled accounts
            if password_hash in ("*", "!", "!!"):
                continue

            users.append((username, password_hash))

    return users


# Load password dictionary
password_dictionary = read_dictionary("top1000.txt")

# Load users from shadow file
shadow_users = read_shadow("shadow")

# Test every password for every user
for username, hashed_password in shadow_users:

    print(f"Checking {username}...")

    found = False

    for password in password_dictionary:
        if test_password(hashed_password, password):
            print(f"  Match found!")
            print(f"  Username : {username}")
            print(f"  Password : {password}\n")
            found = True
            break

    if not found:
        print("  No match found.\n")