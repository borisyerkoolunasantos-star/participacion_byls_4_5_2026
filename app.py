from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = "products"

    id    = db.Column(db.Integer,  primary_key=True)
    name  = db.Column(db.String,   nullable=False)
    price = db.Column(db.Float,    nullable=False)
    stock = db.Column(db.Integer,  default=0)        

    def __repr__(self):
        return f"{self.id} {self.name} , Precio: Bs.{self.price:.2f} , Stock: {self.stock}"


def init_db():
    with app.app_context():
        db.create_all()
        print(" Tabla 'products' creada exitosamente")


def insert_products():
    with app.app_context():
        p1 = Product(name="Laptop Gamer",   price=1299.99, stock=10)
        p2 = Product(name="Mouse Inalámbrico", price=29.99, stock=50)
        p3 = Product(name="Teclado Mecánico", price=89.99, stock=25)
        p4 = Product(name="Monitor 4K",     price=499.99, stock=8)

        db.session.add_all([p1, p2, p3, p4])   
        db.session.commit()
        print(" Productos insertados correctamente")

def query_products():
    with app.app_context():
        productos = Product.query.all()
        print("\n Lista de productos:")
        print("-"*50)
        for p in productos:
            print(p)
        print("-"*50)    

def update_product():
    with app.app_context():
        producto = Product.query.filter_by(id=1).first()
        if producto:
            producto.price = 100.20   
            producto.stock = 5       
            db.session.commit()
            print(f"\n Producto actualizado → {producto}")
        else:
            print("\n Producto no encontrado")

def delete_product():
    with app.app_context():
        producto = Product.query.filter_by(id=1).first()
        if producto:
            db.session.delete(producto)
            db.session.commit()
            print(f"\n  Producto eliminado: {producto}")
        else:
            print("\n Producto no encontrado")


if __name__ == "__main__":
    init_db()           
    #insert_products()   
    #query_products()  
    #update_product()    
    #query_products()    
    delete_product()    
    query_products()    