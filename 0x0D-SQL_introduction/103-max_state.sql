-- displays the max temp of each state (ordered by State name)

SELECT `state`, MAX(value) as `max_temp` FROM tempearatures GROUP BY state ORDER BY satate;
