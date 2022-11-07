-- creates the database 'hbtn_0d_usa' and the table 'cities' in the database
-- shouldn't fail if hbtn_0d_usa or cities exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256),
    CONSTRAINT fk_state_id FOREIGN KEY (state_id)
    REFERENCES states(id)
);
