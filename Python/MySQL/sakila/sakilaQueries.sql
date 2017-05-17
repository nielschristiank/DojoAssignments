SELECT customer.first_name, customer.Last_name, customer.email, address.address, customer.address_id, address.city_id
FROM customer
JOIN  address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film_category
JOIN film ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT  customer.store_id, customer.first_name, customer.last_name, customer.email, address.address, customer.address_id AS customer_address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE customer.store_id = 1;

SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name, film.title, film.description, film.release_year, film.rating, film.special_features
FROM film_actor
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE ('%behind the scenes%');

SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name
FROM film_actor
JOIN film ON film_actor.film_id = film.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

SELECT film.rental_rate, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film_category
JOIN film ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Drama" AND film.rental_rate = 2.99;

SELECT CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film.film_id = film_category.film_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER';






