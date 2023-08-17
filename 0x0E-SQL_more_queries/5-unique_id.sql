-- ID?? is a Unique ID 
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT,
    name VARCHAR(256)
    UNIQUE(id)
)
