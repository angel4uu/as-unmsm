COPY professional_career(code, name, creation_date)
FROM '/data/careers.csv' DELIMITER ',' CSV HEADER;

COPY student(code, last_name, first_name, age, gender, weight, height, color, province, career_code, entry_date)
FROM '/data/students.csv' DELIMITER ',' CSV HEADER;