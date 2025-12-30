CREATE DATABASE SOCIETY;
USE SOCIETY;
CREATE TABLE residents (
    name VARCHAR(100) NOT NULL,
    authorization ENUM('Home Owner', 'President', 'Vice') NOT NULL,
    total_family_members INT NOT NULL CHECK (total_family_members > 0),
    block CHAR NOT NULL,
    flat_number VARCHAR(10) NOT NULL,
    PRIMARY KEY (block, flat_number)
);
CREATE TABLE gatepasses (
    pass_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    block CHAR NOT NULL,
    flat_number VARCHAR(10) NOT NULL,
    qr_token VARCHAR(255) UNIQUE NOT NULL,
    valid_from DATETIME NOT NULL,
    valid_until DATETIME NOT NULL,
    FOREIGN KEY (block, flat_number)
        REFERENCES residents(block, flat_number)
        ON DELETE CASCADE
);
CREATE TABLE entry_logs (
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    block CHAR,
    flat_number VARCHAR(10),
    visitor_name VARCHAR(100),
    visitor_type ENUM('ZOMATO','SWIGGY','MAID','DELIVERY','GUEST','MAINTENANCE'),
    pass_mode ENUM('QR','AUTO','INSTANT'),
    status ENUM('ALLOWED','DENIED'),
    scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM GATEPASSES;
SELECT * FROM ENTRY_LOGS;
-- INSTANT - Unexpected guests or deliveries
-- AUTO - Regular attendees (maid, milk, groceries, maintenanace staff)
-- QR - Pre-approved guests