CREATE TABLE books (
    id INTEGER NOT NULL,
    title VARCHAR(50),
    cover VARCHAR(255),
    user_id INTEGER,
    creation_date DATETIME,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users (id)
);
CREATE TABLE parts (
    id INTEGER NOT NULL,
    title VARCHAR(80),
    content TEXT,
    "order" INTEGER,
    book_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(book_id) REFERENCES books (id)
);
CREATE TABLE users (
    id INTEGER NOT NULL,
    name VARCHAR(120),
    email VARCHAR(120),
    password VARCHAR(120),
    role SMALLINT,
    status SMALLINT,
    PRIMARY KEY (id),
    UNIQUE (name),
    UNIQUE (email)
);
