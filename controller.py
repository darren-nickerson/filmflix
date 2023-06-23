from sql_handling import SQLHandling


class Controller:
    def __init__(self):
        """
        Initializes the Controller class by creating an instance of the SQLHandling class.
        """
        self.connector = SQLHandling("filmflix.db")

    def insert_film(self, title, year_released, rating, duration, genre):
        """
        Inserts a film record into the database with the provided details.

        Args:
            title (str): The title of the film.
            year_released (str): The year the film was released.
            rating (str): The rating of the film.
            duration (str): The duration of the film.
            genre (str): The genre of the film.

        Returns:
            str or list: If successful, returns "Film inserted successfully." If errors occur, returns a list of error messages.
        """
        errors = []

        if not title.strip():
            errors.append("Title is empty.")

        if not year_released.isdigit():
            errors.append("Year released must be a valid integer.")

        if not rating.strip():
            errors.append("Rating is empty.")

        if not duration.isdigit():
            errors.append("Duration must be a valid integer.")

        if not genre.strip():
            errors.append("Genre is empty.")

        if errors:
            return errors

        try:
            query = "INSERT INTO tblfilms (title, year_released, rating, duration, genre) VALUES (?, ?, ?, ?, ?)"
            values = (
                title.strip(),
                year_released.strip(),
                rating.strip(),
                duration.strip(),
                genre.strip(),
            )
            self.connector.execute(query, values)
            return "Film inserted successfully."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def select_all_films_by_genre(self, lookup_genre):
        """
        Retrieves all film records from the database that match the provided genre.

        Args:
            lookup_genre (str): The genre to search for.

        Returns:
            list: A list of film records matching the provided genre.
        """
        try:
            query = "SELECT rowid, * FROM tblfilms WHERE genre LIKE ?"
            self.connector.execute(query, (lookup_genre,))
            records = self.connector.fetchall()
            return records
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def select_film_by_title(self, lookup_title):
        """
        Retrieves all film records from the database that match the provided title.
        Returns the retrieved records or an error message if an exception occurs.

        Args:
            lookup_title (str): The title to search for.

        Returns:
            list: A list of film records matching the provided title.
        """
        try:
            query = "SELECT rowid, * FROM tblfilms WHERE title LIKE ?"
            self.connector.execute(query, ("%{}%".format(lookup_title),))
            records = self.connector.fetchall()
            return records
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def select_film_by_id(self, film_id):
        """
        Retrieves a film record from the database that matches the provided ID.

        Args:
            film_id (int): The ID of the film.

        Returns:
            tuple: A film record matching the provided ID.
        """
        try:
            query = "SELECT rowid, * FROM tblfilms WHERE rowid = ?"
            self.connector.execute(query, (film_id,))
            records = self.connector.fetchone()
            return records
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def select_all_films_by_wildcard(self, title_like):
        """
        Retrieves all film records from the database that match the provided title pattern.

        Args:
            title_like (str): The title pattern to search for.

        Returns:
            list: A list of film records matching the provided title pattern.
        """
        try:
            query = "SELECT rowid, * FROM tblfilms WHERE title LIKE ?"
            self.connector.execute(query, ("%{}%".format(title_like),))
            records = self.connector.fetchall()
            return records
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def select_all_films(self):
        """
        Retrieves all film records from the database.

        Returns:
            list: A list of all film records in the database.
        """
        try:
            query = "SELECT rowid, * FROM tblfilms"
            self.connector.execute(query)
            records = self.connector.fetchall()
            return records
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def delete_record(self, film_id):
        """
        Deletes a film record from the database that matches the provided ID.

        Args:
            film_id (int): The ID of the film to delete.
        """
        try:
            query = "DELETE FROM tblfilms WHERE rowid = ?"
            self.connector.execute(query, (film_id,))
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def update_record(self, oid, title, year_released, rating, duration, genre):
        """
        Updates a film record in the database with the provided details.

        Args:
            oid (int): The ID of the film to update.
            title (str): The updated title of the film.
            year_released (str): The updated year the film was released.
            rating (str): The updated rating of the film.
            duration (str): The updated duration of the film.
            genre (str): The updated genre of the film.

        Returns:
            str or list: If successful, returns "Record updated successfully." If errors occur, returns a list of error messages.
        """
        errors = []

        if not title.strip():
            errors.append("Title is empty.")

        if not year_released.strip().isdigit():
            errors.append("Year released must be a valid integer.")

        if not rating.strip():
            errors.append("Rating is empty.")

        if not duration.strip().isdigit():
            errors.append("Duration must be a valid integer.")

        if not genre.strip():
            errors.append("Genre is empty.")

        if errors:
            return errors

        try:
            query = """
                UPDATE tblfilms SET
                title = ?,
                year_released = ?,
                rating = ?,
                duration = ?,
                genre = ?
                WHERE rowid = ?
            """
            values = (
                title.strip(),
                year_released.strip(),
                rating.strip(),
                duration.strip(),
                genre.strip(),
                oid.strip(),
            )
            self.connector.execute(query, values)
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
        else:
            return "Record updated successfully"
