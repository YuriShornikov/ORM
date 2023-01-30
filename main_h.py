import sqlalchemy
from sqlalchemy.orm import sessionmaker


from models_h import create_tables, Publisher, Book, Stock, Shop, Sale

from DSN import DSN

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

publisher1 = Publisher(name='Пушкин')
book1 = Book(title="Капитанская дочка", id_publisher=1)
shop1 = Shop(name="Буквоед")
sale1 = Sale(price=600, date_sale="09-11-2022", id_stock=1)
stock1 = Stock(id_book=1, id_shop=1)
book2 = Book(title="Руслан и Людмила", id_publisher=1)
shop2 = Shop(name="Буквоед")
sale2 = Sale(price=500, date_sale="08-11-2022", id_stock=2)
stock2 = Stock(id_book=2, id_shop=1)
book3 = Book(title="Капитанская дочка", id_publisher=1)
shop3 = Shop(name="Лабиринт")
sale3 = Sale(price=500, date_sale="05-11-2022", id_stock=3)
stock3 = Stock(id_book=3, id_shop=2)
book4 = Book(title="Евгений Онегин", id_publisher=1)
shop4 = Shop(name="Книжный дом")
sale4 = Sale(price=490, date_sale="02-11-2022", id_stock=4)
stock4 = Stock(id_book=4, id_shop=3)
book5 = Book(title="Капитанская дочка", id_publisher=1)
shop5 = Shop(name="Буквоед")
sale5 = Sale(price=600, date_sale="26-10-2022", id_stock=5)
stock5 = Stock(id_book=1, id_shop=1)

session.add(publisher1)
session.add_all([book1, book2, book3, book4, book5])
session.add_all([shop1, shop2, shop3, shop4, shop5])
session.add_all([sale1, sale2, sale3, sale4, sale5])
session.add_all([stock1, stock2, stock3, stock4, stock5])
session.commit()

query = session.query(Book, Stock, Shop, Sale).join(Shop).join(Sale).join(Book).join(Publisher).filter(Publisher.name.like('%Пушкин%')).all()
for i in query:
    print(i[0], i[1], i[2], i[3])


session.commit()
session.close()
