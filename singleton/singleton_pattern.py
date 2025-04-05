class Database:
    _instance = None
    _connection_established = False
    query_counter = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.fire_db_connection()
            cls._connection_established = True
        return cls._instance

    @classmethod
    def fire_db_connection(cls):
        if cls._connection_established:
            return
        print("Staring connection ...")


a = Database()
b = Database()

a.query_counter = 100
print(id(a) == id(b))
print(a is b)
print(b.query_counter)

b.query_counter = 200
print(a.query_counter)
