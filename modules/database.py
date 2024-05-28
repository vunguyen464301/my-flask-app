import pyodbc


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._conn = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        # Database connection configuration
        server = "your_server_name"  # replace with your SQL Server hostname
        database = "your_database_name"  # replace with your database name
        username = "your_username"  # replace with your database username
        password = "your_password"  # replace with your database password

        # Create a connection to the database
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        return pyodbc.connect(conn_str)

    @property
    def connection(self):
        return self._conn


# Create an instance of the database connection
dbConnection = DatabaseConnection().connection
