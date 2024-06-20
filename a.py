import os

# Vulnerable
user_input = "/evil/code" # value supplied by user
os.execl(user_input, '/foo/bar', '--do-smth')

# Vulnerable
user_input = "cat /etc/passwd" # value supplied by user
os.execve("/bin/bash", ["/bin/bash", "-c", user_input], os.environ)
