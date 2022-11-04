-- displays the max temp of each state (ordered by State name)

SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY max_temp ORDER BY satate;
