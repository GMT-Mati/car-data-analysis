"""
The config module contains global app configuration variables.
"""

# The config.py module contains global configuration variables for the app. In this example,
# we have configuration variables for the database connection, CSV export, and security settings.
# The DB_HOST, DB_PORT, DB_USER, DB_PASSWORD,
# and DB_NAME variables contain the details for connecting to the MySQL database.
# The CSV_DELIMITER and CSV_QUOTECHAR variables specify the delimiter and quote character for CSV exports.
# The SECRET_KEY variable is used for authentication and authorization, and should be kept secret.
# The HASH_ALGORITHM variable specifies the hashing algorithm to use for passwords.
# The ENCRYPTION_ALGORITHM, ENCRYPTION_KEY, ENCRYPTION_MODE,
# and IV_LENGTH variables specify the encryption settings for sensitive data.
# In this example, we use AES encryption in CBC mode with a 128-bit key and a 16-byte initialization vector (IV).
# The ENCRYPTION_KEY variable should be kept secret.

# Database configuration
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'username'
DB_PASSWORD = 'password'
DB_NAME = 'otomoto_data'

# CSV export configuration
CSV_DELIMITER = ','
CSV_QUOTECHAR = '"'

# Security configuration
SECRET_KEY = 'mysecretkey'
HASH_ALGORITHM = 'sha256'
ENCRYPTION_ALGORITHM = 'AES'
ENCRYPTION_KEY = b'myencryptionkey'
ENCRYPTION_MODE = 'CBC'
IV_LENGTH = 16
