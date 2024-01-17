-- This script creates a database and a new user
-- The new user will only have SELECT privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* to 'user_0d_2'@'localhost'
WITH GRANT OPTION;
