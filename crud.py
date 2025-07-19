from models import Product
from database import SessionLocal
from datetime import datetime

def add_product(name, category, quantity, price):
    session = SessionLocal()
    product = Product(name=name, category=category, quantity=quantity, price=price, last_updated=datetime.now())
    session.add(product)
    session.commit()
    session.close()
    print("✅ Product added.")

def view_products():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

def update_quantity(product_id, new_quantity):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        product.quantity = new_quantity
        product.last_updated = datetime.now()
        session.commit()
        print("🔁 Quantity updated.")
    else:
        print("❌ Product not found.")
    session.close()

def delete_product(product_id):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print("🗑️ Product deleted.")
    else:
        print("❌ Product not found.")
    session.close()

def search_product(name):
    session = SessionLocal()
    products = session.query(Product).filter(Product.name.ilike(f"%{name}%")).all()
    session.close()
    return products

def low_stock_report(threshold):
    session = SessionLocal()
    products = session.query(Product).filter(Product.quantity < threshold).all()
    session.close()
    return products

def get_all_products_for_chart():
    session = SessionLocal()
    products = session.query(Product.name, Product.quantity).all()
    session.close()
    return products