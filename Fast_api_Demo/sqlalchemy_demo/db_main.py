from sqlalchemy import DateTime, func
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
# 创建数据库引擎
engine = create_engine(r'sqlite:///E:\Workspace\ai\net_python\Fast_api_Demo\sqlalchemy_demo\sqlorm_Demo.db', echo=True)

# 定义一个模型类的基类

class Base(DeclarativeBase):
    
    # 只要继承自Base的模型类，都会有的属性和字段映射 python属性: Mapped[字段类型] = mapped_column(表的字段约束)
    # Mapped[datetime] → 表示这个字段在 Python 层是 datetime 类型（类型提示） mapped_column() 函数的参数指定了字段在数据库中对应的列的类型 ->
    # DateTime 这是 SQLAlchemy 提供的“列类型”，用于告诉 SQLAlchemy：“这个字段在数据库中应该是什么类型”。 SQLite → DATETIME MySQL → DATETIME 或 TIMESTAMP
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), comment="记录的创建时间")  # 创建时间
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), onupdate=func.now(), comment='记录的修改时间')  # 更新时间  # ← 告诉 SQLAlchemy：数据库列类型是 DATETIME
