CREATE TABLE IF NOT EXISTS passengers (
    id INT PRIMARY KEY,
    pclass INT,
    survived INT,
    pname VARCHAR(255),
    sex VARCHAR(10),
    age FLOAT,
    sibsp INT,
    parch INT,
    ticket VARCHAR(50),
    fare FLOAT,
    cabin VARCHAR(50),
    embarked VARCHAR(10),
    boat VARCHAR(10),
    body INT,
    homedest VARCHAR(50)
);
