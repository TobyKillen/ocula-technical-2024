import sqlite3

class DatabaseClient:
    def __init__(self) -> None:
        self.Database = sqlite3.connect("weather.db")
        # Ideally here I would use an ORM like SQLAlchemy to interact with the database

    class Weather:
        # UUID, City, Min Temp, Max Temp, Average Mean Temp, Average Mode Temp, Average Humidity, Date, Created At, Updated At, Deleted At
        pass

    class HistoricalFetches:
        # UUID, City, Date, Created At, Updated At, Deleted At
        # or
        # UUID, Hash, Created At, Updated At, Deleted At
        # Using a hash would allow us to store the hash of the city and date and use that as a unique identifier for quick lookups
        # This table would store all the historical fetches so we can return the data from the database if it's already been fetched
        pass
