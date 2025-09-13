from typing import Annotated
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from shopping_app.cart_views import shop
import uvicorn

app = FastAPI()

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 包含分支路由
app.include_router(shop)


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,  # 基础类型：一个可选的字符串    定义查询参数?q   因为默认是None，所有可以传入也可以不传入
        Query(
            min_length=3,      # 验证：最小长度为3
            max_length=50,     # 验证：最大长度为50
            pattern="^fixedquery$", # 验证：必须精确匹配 "fixedquery"
            title="Query String", # 文档：标题
            description="Query string for the items to search in the database", # 文档：描述
            alias="item-query" # URL中使用的别名
        )
    ] = None  # 函数的默认值
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 如果你不想添加特定值，而只是让它成为可选项，将查询参数(?q=...)默认值设为 None 。 否则，必须提供该参数。
@app.get("/items/{item_id}",tags=['items接口描述'],description="items接口的详细描述",response_description="items接口的响应描述")
async def read_item(item_id: str, q: Annotated[(str | None), Query(max_length=50)] = None):
    if q:
        return {"item_id": item_id, "q": q}           # /items/{item_id}是路径参数，q是查询参数
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)