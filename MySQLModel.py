import mysql.connector

class MySQLModel():
    def __init__(self) -> None:
        self.myDB = None
        self.myCursor = None
    
    def connect(self, host="localhost", user="bluefox", password="bluefox") -> bool:
        try:
            if not self.myDB:
                self.myDB = mysql.connector.connect(
                    host=host, 
                    user=user, 
                    password=password
                )
            if not self.myCursor:
                self.myCursor = self.myDB.cursor(dictionary=True)
        except Exception as e:
            print(f"Failed to connect to MySQL: {e}")
            self.disconnect()
            
    def disconnect(self):
        try:
            if self.myCursor:
                self.myCursor.close()
        except Exception as e:
            print(f"Failed to close to MySQL Cursor: {e}")
        try:
            if self.myDB:
                self.myDB.close()
        except Exception as e:
            print(f"Failed to close to MySQL Connection: {e}")
            
    def read_all_chat_identifiers(self):
        pass
    
    def read_last_used_chat_identifier(self):
        pass
    
    def create_chat_identifier(self, chat_name):
        pass
    
    def remove_chat(self, chat_id):
        pass