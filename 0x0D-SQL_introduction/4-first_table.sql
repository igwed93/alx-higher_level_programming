-- creates a table called first_table; shouldn't fail if it already exists

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
