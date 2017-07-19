-- Countries that speak Slovene
SELECT countries.name
	, languages.language
    , languages.percentage 
FROM countries JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY percentage desc;

-- Cities per Country
SELECT countries.name
	, COUNT(cities.id) AS 'count_of_cities'
FROM countries join cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.id) DESC;

-- Cities in Mexico with a population > 500,000
SELECT t.name
	, t.population 
FROM cities t JOIN countries c ON t.country_id = c.id
WHERE c.name = 'Mexico' 
	AND t.population > 500000
ORDER BY t.population DESC;

-- I know how to do the rest so moving on.

