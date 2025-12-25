
DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS marks;
DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS students;


CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    roll_no TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    class TEXT NOT NULL
);



CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT NOT NULL,
    max_marks INTEGER NOT NULL
);


CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    marks_obtained INTEGER NOT NULL,

    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);


CREATE TABLE results (
    student_id INTEGER PRIMARY KEY,
    total_marks INTEGER,
    percentage REAL,
    status TEXT,
    category TEXT,

    FOREIGN KEY (student_id) REFERENCES students(id)
);
