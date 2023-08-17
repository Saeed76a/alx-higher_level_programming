-- all records
SELECT DISTINCT name
  FROM tv_genres AS g
       INNER JOIN tv_show_genres
       ON g.id = tv_show_genres.genre_id

       INNER JOIN tv_shows AS t
       ON tv_show_genres.show_id = t.id
       WHERE g.name NOT IN
             (SELECT name
                FROM tv_genres AS g
	             INNER JOIN tv_show_genres
		     ON g.id = tv_show_genres.genre_id
		INNER JOIN tv_shows AS t
		ON tv_show_genres.show_id = t.id
	WHERE t.title = "Dexter")
 ORDER BY g.name;
