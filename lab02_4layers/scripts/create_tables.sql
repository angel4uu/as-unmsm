CREATE TABLE professional_career (
    code INT PRIMARY KEY,               
    name VARCHAR(255) NOT NULL,         
    creation_date DATE NOT NULL          
);

CREATE TABLE student (
    code BIGINT PRIMARY KEY,       
    last_name VARCHAR(100) NOT NULL,  
    first_name VARCHAR(100) NOT NULL, 
    age INT NOT NULL,            
    gender CHAR(1) NOT NULL,      
    weight DECIMAL(5, 2) NOT NULL,  
    height DECIMAL(4, 2) NOT NULL,  
    color VARCHAR(50) NOT NULL,   
    province VARCHAR(100) NOT NULL,  
    career_code INT NOT NULL,     
    entry_date DATE NOT NULL,
    CONSTRAINT fk_career_code
      FOREIGN KEY (career_code) 
      REFERENCES professional_career(code)      
);



