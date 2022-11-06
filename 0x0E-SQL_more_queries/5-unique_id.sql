-- creates the table 'unique_id'
-- shouldn't fail if unique_id already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
