-- Создание Таблиц

CREATE TABLE train_classes (
	class_id INT NOT NULL PRIMARY KEY,
	class_name char(30) NOT NULL
);

CREATE TABLE airline_classes (
	class_id INT NOT NULL PRIMARY KEY,
	class_name char(30) NOT NULL
);

CREATE TABLE trips (
	trip_id INT NOT NULL PRIMARY KEY,
	trip_date datetime NOT NULL,
	travel_time TIME NOT NULL,
	train сhar(50) NOT NULL,
	where_from char(50) NOT NULL,
	where_to char(50) NOT NULL
);

CREATE TABLE train_seats (
	train_seat_id INT NOT NULL PRIMARY KEY,
	train_seat_num INT NOT NULL,
	trip_id INT NOT NULL,
	FOREIGN KEY(trip_id) REFERENCES trips(trip_id)
);

CREATE TABLE passengers (
	passenger_id int NOT NULL PRIMARY KEY,
	passenger_name char(50) NOT NULL,
	passenger_surname char(50) NOT NULL,
	IIN int NOT NULL,
	birth_date date NOT NULL,
	gender char(10) NOT NULL,
	citizen char(50) NOT NULL,
	document_type VARCHAR(30) NOT NULL,
	document_number INT NOT NULL
);

CREATE TABLE companies (
	company_id int NOT NULL PRIMARY KEY,
	company_name char(50) NOT NULL
);

CREATE TABLE flights (
	flight_id int NOT NULL PRIMARY KEY,
	company_id INT NOT NULL,
	flight_date datetime NOT NULL,
	travel_time TIME NOT NULL,
	airplane сhar(50)  NOT NULL,
	where_from char(50) NOT NULL,
	where_to char(50) NOT NULL,
	FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

CREATE TABLE airline_seats (
	airline_seat_id INT NOT NULL PRIMARY KEY,
	seat_num CHAR(5) NOT NULL,
	flight_id INT NOT NULL,
	FOREIGN KEY(flight_id) REFERENCES flights(flight_id)
);

CREATE TABLE airline_tickets (
	ticket_id INT NOT NULL PRIMARY KEY, 
	passenger_id int NOT NULL,
	where_from char(50) NOT NULL,
	where_to char(50) NOT NULL,
	flight_id INT NOT NULL,
	class_id сhar(50) NOT NULL,
	airline_seat_id INT NOT NULL,
	FOREIGN KEY(passenger_id) REFERENCES passengers(passenger_id),
	FOREIGN KEY(flight_id) REFERENCES flights(flight_id),
	FOREIGN KEY(class_id) REFERENCES airline_classes(class_id),
	FOREIGN KEY(airline_seat_id) REFERENCES airline_seats(airline_seat_id)
);

CREATE TABLE train_tickets (
	ticket_id INT NOT NULL PRIMARY KEY,
	passenger_id int NOT NULL,
	where_from char(50) NOT NULL,
	where_to char(50) NOT NULL,
	trip_id INT NOT NULL,
	class_id сhar(50) NOT NULL,
	train_seat_id INT NOT NULL,
	FOREIGN KEY(passenger_id) REFERENCES passengers(passenger_id),
	FOREIGN KEY(trip_id) REFERENCES trips(trip_id),
	FOREIGN KEY(class_id) REFERENCES train_classes(class_id),
	FOREIGN KEY(train_seat_id) REFERENCES train_seats(train_seat_id)
);




-- Данные для train_classes и airline_classes

INSERT INTO train_classes VALUES 
(1, 'Плацкарт'),
(2, 'Купе'),
(3, 'Тальго Сидячий'),
(4, 'Тальго Купе'),
(5, 'Тальго Люкс');


INSERT INTO airline_classes VALUES 
(1, 'Эконом'),
(2, 'Бизнес');