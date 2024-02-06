from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base
from configuration import CONNECTION_ROW

# Замените 'mysql://user:password@localhost/db_name' на ваши реальные данные
# user - имя пользователя, password - пароль, localhost - хост базы данных, db_name - название базы данных
engine = create_engine(CONNECTION_ROW)

# Создайте соединение
connection = engine.connect()



# Закройте соединение
connection.close()
