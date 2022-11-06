-- creates the table 'id_not_null'
-- shouldn't fail if the table id_not_null already exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
