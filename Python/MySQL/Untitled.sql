SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = "Slovene";

SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id;

SELECT countries.name, cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY population DESC;

SELECT countries.name
FROM countries
WHERE countries.surface_area > 501 AND countries.population > 100000;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language.percentage > 0.89 
ORDER BY languages.percentage DESC;
