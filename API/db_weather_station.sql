CREATE TABLE Weather_Station_Test.Sonde (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `Temperature` DECIMAL(6,2) not null,
    `Humidity` DECIMAL(6,2) not null,
    PRIMARY KEY (`id`),
    `Added` TIMESTAMP NOT NULL DEFAULT current_timestamp
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
INSERT INTO Weather_Station_Test.sonde1 (Temperature, Humidity) values (30,70), (30.5, 69.9), (40.5, 15.9), (15.5, 78.6);

