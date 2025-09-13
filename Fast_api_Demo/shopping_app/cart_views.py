from fastapi import APIRouter

# 分支路由
shop = APIRouter(
    prefix="/shop",
)

shops = [{"id": 1, "name": "Shop A"},
    {"id": 2, "name": "Shop B"},
    {"id": 3, "name": "Shop C"},
]
@shop.get("/carts/{cart_id}", tags=["cart接口描述"], description="cart接口的详细描述", response_description="cart接口的响应描述")
async def find_cart(cart_id: int):
    for cart in shops:
        if cart["id"] == cart_id:
            print(f"您找的购物车是:{cart}")
            return cart
    return None