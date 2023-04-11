-- Найти AVG, SUM, MIN и MAX возраста пассажиров
SELECT AVG(age), SUM(age), MIN(age), MAX(age) FROM passengers;

-- Написать выборку для ввода на экран уникальных рейсов из Flights
-- SELECT DISTINCT(where_from || ' ' || where_to) FROM flights;

-- Написать выборку для ввода на экран уникальных городов из where_from в таблице Trips
-- SELECT DISTINCT where_from FROM trips

-- Найти медиану age для passengers. 
-- SELECT MEDIAN(age) FROM passengers;

-- Написать запрос AVG, SUM, MIN и MAX возраста с предложения GROUP BY для каждой страны и сортировка с SUM 
-- SELECT SUM(age) summa, ROUND(AVG(age), 1), MIN(age), MAX(age) FROM passengers
-- GROUP BY citizen
-- ORDER BY summa;

-- Написать запрос AVG age, где age <= 20 для таблицы Passengers
-- SELECT avg(age) FROM passengers
-- WHERE age <= 20;

-- Соединение более двух таблиц Trips, Train_tickets, Train_classes
-- SELECT * FROM trips t1
-- JOIN train_tickets t2 ON t1.trip_id = t2.trip_id
-- JOIN train_classes t3 ON t3.class_id = t2.class_id; 

-- Написать выборку Outer Join из таблиц Flights and Companies
-- SELECT * FROM flights f
-- OUTER JOIN companies c ON f.company_id = c.company_id ;

-- Написать выборку с кросс-соединением (Cross join) из таблиц Flights and Companies
-- SELECT * FROM flights
-- CROSS JOIN companies;

-- Написать выборку с естественных объединений (Natural join) из таблиц Flights and Companies
-- SELECT * FROM flights
-- Natural JOIN companies;

-- Написать выборку LEFT OUTER JOIN из таблиц Flights and Companies
-- SELECT * FROM flights f
-- LEFT OUTER JOIN companies c ON f.company_id = c.company_id ;

-- Написать выборку RIGHT OUTER JOIN из таблиц Flights and Companies и сделать сортировку по убыванию
-- SELECT * FROM flights f
-- RIGHT OUTER JOIN companies c ON f.company_id = c.company_id ;

-- Написать выборку FULL OUTER JOIN из таблиц Flights and Companies и сделать сортировку
-- SELECT * FROM flights f
-- FULL OUTER JOIN companies c ON f.company_id = c.company_id ;
