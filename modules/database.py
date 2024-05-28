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

        try:
            # Database connection configuration
            server = "localhost"  # replace with your SQL Server hostname
            database = "QL_BANHANG"  # replace with your database name
            username = "sa"  # replace with your database username
            password = "root@123456"  # replace with your database password

            # # Create a connection to the database
            conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

            # Attempt to establish a connection to the database
            conn = pyodbc.connect(conn_str)
            print("Connected to SQL Server successfully")
            return conn

        except pyodbc.Error as ex:
            # Handle connection errors
            print("Error connecting to SQL Server:", ex)
            return None

    @property
    def connection(self):
        return self._conn


# Create an instance of the database connection
dbConnection = DatabaseConnection().connection
