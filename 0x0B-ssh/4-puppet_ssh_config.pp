# Script to  to connect to a server without typing a password.
file_line {'identity_file':
path => 'etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton'
}

file_line {'no_password':
path => 'etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

