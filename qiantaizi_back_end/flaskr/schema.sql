DROP TABLE IF EXISTS qiantaizi;
DROP TABLE IF EXISTS qiantaizi_template;

CREATE TABLE qiantaizi(
    studentId TEXT PRIMARY KEY,
    Name TEXT UNIQUE NOT NULL,
    Money REAL NOT NULL DEFAULT 99.99,
    Monfirst INT NOT NULL DEFAULT 0,
    Monsecond INT NOT NULL DEFAULT 0,
    Monthird INT NOT NULL DEFAULT 0,
    Monforth INT NOT NULL DEFAULT 0,
    Tuefirst INT NOT NULL DEFAULT 0,
    Tuesecond INT NOT NULL DEFAULT 0,
    Tuethird INT NOT NULL DEFAULT 0,
    Tueforth INT NOT NULL DEFAULT 0,
    Wedfirst INT NOT NULL DEFAULT 0,
    Wedsecond INT NOT NULL DEFAULT 0,
    Wedthird INT NOT NULL DEFAULT 0,
    Wedforth INT NOT NULL DEFAULT 0,
    Thufirst INT NOT NULL DEFAULT 0,
    Thusecond INT NOT NULL DEFAULT 0,
    Thuthird INT NOT NULL DEFAULT 0,
    Thuforth INT NOT NULL DEFAULT 0,
    Frifirst INT NOT NULL DEFAULT 0,
    Frisecond INT NOT NULL DEFAULT 0,
    Frithird INT NOT NULL DEFAULT 0,
    Friforth INT NOT NULL DEFAULT 0,
    Satfirst INT NOT NULL DEFAULT 0,
    Satsecond INT NOT NULL DEFAULT 0,
    Satthird INT NOT NULL DEFAULT 0,
    Satforth INT NOT NULL DEFAULT 0,
    Sunfirst INT NOT NULL DEFAULT 0,
    Sunsecond INT NOT NULL DEFAULT 0,
    Sunthird INT NOT NULL DEFAULT 0,
    Sunforth INT NOT NULL DEFAULT 0
);

CREATE TABLE qiantaizi_template(
    Time TEXT PRIMARY KEY,
    Mon TEXT NOT NULL DEFAULT ' ',
    Tue TEXT NOT NULL DEFAULT ' ',
    Wed TEXT NOT NULL DEFAULT ' ',
    Thu TEXT NOT NULL DEFAULT ' ',
    Fri TEXT NOT NULL DEFAULT ' ',
    Sat TEXT NOT NULL DEFAULT ' ',
    Sun TEXT NOT NULL DEFAULT ' '
);

INSERT INTO qiantaizi_template (Time) VALUES ('No.1 8:00~10:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.1 12:00~14:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.1 16:00~18:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.1 20:00~22:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.2 8:00~10:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.2 12:00~14:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.2 16:00~18:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.2 20:00~22:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.3 8:00~10:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.3 12:00~14:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.3 16:00~18:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.3 20:00~22:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.4 8:00~10:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.4 12:00~14:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.4 16:00~18:30');
INSERT INTO qiantaizi_template (Time) VALUES ('No.4 20:00~22:30');
