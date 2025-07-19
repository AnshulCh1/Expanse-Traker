from database import SessionLocal, init_db
from models import Product

# Initialize the DB and session
init_db()
session = SessionLocal()

# Sample inventory data
sample_products = [
    Product(name="Apple", category="Fruits", quantity=20, price=40.0),
    Product(name="Banana", category="Fruits", quantity=30, price=10.0),
    Product(name="Milk", category="Dairy", quantity=15, price=50.0),
    Product(name="Bread", category="Bakery", quantity=25, price=25.0),
    Product(name="Shampoo", category="Personal", quantity=10, price=120.0),
    Product(name="Rice", category="Grains", quantity=8, price=60.0),
    Product(name="Sugar", category="Grains", quantity=18, price=35.0),
    Product(name="Soap", category="Personal", quantity=5, price=30.0),
    Product(name="Cheese", category="Dairy", quantity=12, price=70.0),
    Product(name="Tomato", category="Vegetables", quantity=22, price=20.0),
]

session.add_all(sample_products)
session.commit()
session.close()

print("Sample data inserted successfully.")
