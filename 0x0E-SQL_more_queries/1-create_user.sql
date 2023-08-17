-- creates the MySQL server user user_0d_1.
-- GRANTS <permissions type> ON <permissions zone> TO <user name>
CREATE USER IF NOT EXISTS user_0d_1@localhost;
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
ALTER USER user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
