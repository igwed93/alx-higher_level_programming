-- creates the databse hbtn_0d_2 and the user user_0d_2
-- grants only select privilege to the user in the database hbtn_0d_2
-- script shouldn't fail if hbtn_0d_2 and user_0d_2 already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
