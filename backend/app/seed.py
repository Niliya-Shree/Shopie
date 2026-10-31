from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product

SIZES = ["S", "M", "L", "XL"]

PRODUCTS = [
    ("classic-white-tee", "Classic White Tee", "Tops", 499, "Soft cotton crew neck."),
    ("denim-jacket", "Denim Jacket", "Outerwear", 2499, "Medium wash, relaxed fit."),
    ("slim-chinos", "Slim Chinos", "Bottoms", 1499, "Stretch cotton, tapered leg."),
    ("hoodie-charcoal", "Charcoal Hoodie", "Tops", 1799, "Fleece-lined pullover."),
    ("linen-shirt", "Linen Shirt", "Tops", 1299, "Breathable summer shirt."),
    ("cargo-shorts", "Cargo Shorts", "Bottoms", 999, "Six pockets, durable twill."),
    ("floral-kurta", "Floral Kurta", "Ethnic", 1199, "Block-printed cotton."),
    ("track-pants", "Track Pants", "Bottoms", 899, "Comfort fit with zip pockets."),
]


def seed_products(db: Session) -> None:
    if db.scalars(select(Product).limit(1)).first():
        return
    for slug, name, category, price, desc in PRODUCTS:
        db.add(
            Product(
                slug=slug, name=name, category=category, price=price,
                description=desc, image_url=f"/products/{slug}.svg", sizes=SIZES,
            )
        )
    db.commit()