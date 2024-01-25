#change login to hb  and log in without any error message.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
