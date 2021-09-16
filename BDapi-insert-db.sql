CREATE DATABASE safelog_analytics;

USE safelog_analytics;

CREATE TABLE analytics (
    id_dado int PRIMARY KEY AUTO_INCREMENT,
    cpu_percent decimal(5, 2),
    ram decimal(5, 2),
    disco decimal(5, 2),
    data_medicao datetime,
);
