from sql_handling import SQLHandling


def initialize_database():
    connector = SQLHandling("filmflix.db")

    connector.execute(
        """
        CREATE TABLE IF NOT EXISTS tblfilms (
            film_id INTEGER PRIMARY KEY,
            title TEXT,
            year_released INTEGER,
            rating TEXT,
            duration INTEGER,
            genre TEXT
        )
    """
    )

    # Check if the films table is empty
    connector.execute("SELECT COUNT(*) FROM tblfilms")
    result = connector.fetchone()

    if result[0] == 0:  # If the table is empty, insert data
        # data list
        data_list = [
            ("The Shawshank Redemption", 1994, "R", 142, "Drama"),
            ("The Godfather", 1972, "R", 175, "Crime"),
            ("The Dark Knight", 2008, "PG-13", 152, "Action"),
            ("The Godfather: Part II", 1974, "R", 202, "Crime"),
            ("Pulp Fiction", 1994, "R", 154, "Crime"),
            ("Schindler's List", 1993, "R", 195, "Biography"),
            (
                "The Lord of the Rings: The Return of the King",
                2003,
                "PG-13",
                201,
                "Adventure",
            ),
            ("Fight Club", 1999, "R", 139, "Drama"),
            ("Forrest Gump", 1994, "PG-13", 142, "Drama"),
            ("Inception", 2010, "PG-13", 148, "Action"),
            (
                "The Lord of the Rings: The Fellowship of the Ring",
                2001,
                "PG-13",
                178,
                "Adventure",
            ),
            ("The Lord of the Rings: The Two Towers", 2002, "PG-13", 179, "Adventure"),
            ("Goodfellas", 1990, "R", 146, "Biography"),
            ("The Matrix", 1999, "R", 136, "Action"),
            ("Seven Samurai", 1954, "Not Rated", 207, "Drama"),
            (
                "Star Wars: Episode V - The Empire Strikes Back",
                1980,
                "PG",
                124,
                "Action",
            ),
            ("The Silence of the Lambs", 1991, "R", 118, "Crime"),
            ("City of God", 2002, "R", 130, "Crime"),
            ("Se7en", 1995, "R", 127, "Crime"),
            ("The Usual Suspects", 1995, "R", 106, "Crime"),
            ("Life Is Beautiful", 1997, "PG-13", 116, "Comedy"),
            ("It's a Wonderful Life", 1946, "Approved", 130, "Drama"),
            ("Leon: The Professional", 1994, "R", 110, "Crime"),
            ("Spirited Away", 2001, "PG", 125, "Animation"),
            ("Saving Private Ryan", 1998, "R", 169, "Drama"),
            ("The Green Mile", 1999, "R", 189, "Crime"),
            ("Interstellar", 2014, "PG-13", 169, "Adventure"),
            ("Psycho", 1960, "R", 109, "Horror"),
            ("American History X", 1998, "R", 119, "Drama"),
            ("The Pianist", 2002, "R", 150, "Biography"),
            ("City Lights", 1931, "G", 87, "Comedy"),
            ("Casablanca", 1942, "PG", 102, "Drama"),
            ("Whiplash", 2014, "R", 106, "Drama"),
            ("Gladiator", 2000, "R", 155, "Action"),
            ("The Departed", 2006, "R", 151, "Crime"),
            ("The Prestige", 2006, "PG-13", 130, "Drama"),
            ("Apocalypse Now", 1979, "R", 147, "Drama"),
            ("The Lion King", 1994, "G", 88, "Animation"),
            ("Memento", 2000, "R", 113, "Mystery"),
            ("The Avengers", 2012, "PG-13", 143, "Action"),
            ("American Beauty", 1999, "R", 122, "Drama"),
            ("Alien", 1979, "R", 117, "Horror"),
            ("Cinema Paradiso", 1988, "R", 155, "Drama"),
            ("The Great Dictator", 1940, "G", 125, "Comedy"),
            ("Django Unchained", 2012, "R", 165, "Drama"),
            ("Paths of Glory", 1957, "Approved", 88, "Drama"),
            ("WALL·E", 2008, "G", 98, "Animation"),
            ("Sunset Boulevard", 1950, "Passed", 110, "Drama"),
            ("The Lives of Others", 2006, "R", 137, "Drama"),
            ("Princess Mononoke", 1997, "PG-13", 134, "Animation"),
            ("Oldboy", 2003, "R", 120, "Action"),
            ("Once Upon a Time in the West", 1968, "PG-13", 165, "Western"),
            ("Witness for the Prosecution", 1957, "Approved", 116, "Crime"),
            ("Das Boot", 1981, "R", 149, "Adventure"),
            ("Aliens", 1986, "R", 137, "Action"),
            ("Citizen Kane", 1941, "Approved", 119, "Drama"),
            ("Dangal", 2016, "Not Rated", 161, "Action"),
            ("Vertigo", 1958, "PG", 128, "Mystery"),
            ("Amélie", 2001, "R", 122, "Comedy"),
            ("Braveheart", 1995, "R", 178, "Biography"),
            ("Reservoir Dogs", 1992, "R", 99, "Crime"),
            ("Star Wars: Episode IV - A New Hope", 1977, "PG", 121, "Action"),
            ("Requiem for a Dream", 2000, "R", 102, "Drama"),
            ("Your Name.", 2016, "PG", 106, "Animation"),
            ("M", 1931, "Not Rated", 99, "Crime"),
            ("The Hunt", 2012, "R", 115, "Drama"),
            ("Eternal Sunshine of the Spotless Mind", 2004, "R", 108, "Drama"),
            ("A Clockwork Orange", 1971, "R", 136, "Crime"),
            ("Taxi Driver", 1976, "R", 114, "Crime"),
            ("Full Metal Jacket", 1987, "R", 116, "Drama"),
            ("Lawrence of Arabia", 1962, "Approved", 216, "Adventure"),
            ("The Kid", 1921, "Not Rated", 68, "Comedy"),
            ("To Kill a Mockingbird", 1962, "Not Rated", 129, "Crime"),
            ("Dunkirk", 2017, "PG-13", 106, "Action"),
            ("Double Indemnity", 1944, "Approved", 107, "Crime"),
            ("Toy Story", 1995, "G", 81, "Animation"),
            ("Singin' in the Rain", 1952, "G", 103, "Comedy"),
            ("The Sting", 1973, "PG", 129, "Comedy"),
            ("Bicycle Thieves", 1948, "Not Rated", 93, "Drama"),
            ("Snatch", 2000, "R", 102, "Comedy"),
            ("The 400 Blows", 1959, "Not Rated", 99, "Crime"),
            ("Monty Python and the Holy Grail", 1975, "PG", 91, "Adventure"),
            ("Scarface", 1983, "R", 170, "Crime"),
            ("Rashomon", 1950, "Not Rated", 88, "Crime"),
            ("Star Wars: Episode VI - Return of the Jedi", 1983, "PG", 131, "Action"),
            ("Inglourious Basterds", 2009, "R", 153, "Adventure"),
            ("The Apartment", 1960, "Approved", 125, "Comedy"),
            ("Metropolis", 1927, "Not Rated", 153, "Drama"),
            ("Indiana Jones and the Last Crusade", 1989, "PG-13", 127, "Action"),
            ("Three Billboards Outside Ebbing, Missouri", 2017, "R", 115, "Crime"),
            ("A Separation", 2011, "PG-13", 123, "Drama"),
            ("Yojimbo", 1961, "Not Rated", 110, "Drama"),
            ("Raging Bull", 1980, "R", 129, "Biography"),
            ("Batman Begins", 2005, "PG-13", 140, "Action"),
            ("Some Like It Hot", 1959, "Approved", 121, "Comedy"),
            ("All About Eve", 1950, "Not Rated", 138, "Drama"),
            ("Unforgiven", 1992, "R", 131, "Western"),
            ("The Treasure of the Sierra Madre", 1948, "Passed", 126, "Adventure"),
            ("Up", 2009, "PG", 96, "Animation"),
            ("The Third Man", 1949, "Not Rated", 93, "Film-Noir"),
        ]

        connector.executemany(
            "INSERT INTO tblfilms (title, year_released, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
            data_list,
        )
        connector.close_connection()


if __name__ == "__main__":
    initialize_database()
