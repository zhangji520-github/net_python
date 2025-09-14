from decimal import Decimal
import enum
import sys
import os
# 将当前脚本所在目录的上一级目录添加到 Python 的模块搜索路径中。
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from regex import F
from sqlalchemy import DECIMAL, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from db_main import Base
from db_main import engine
from datetime import date
from sqlalchemy.sql import func

# 枚举Enum性别类
class SexValues(enum.Enum):
    """性别枚举类"""
    MALE = '男'
    FEMALE = '女'


# 定义 ORM 模型类 Employee
class Employee(Base):
    """员工表"""

    __tablename__ = 't_emp'       # 指定该模型映射到数据库中的表名为 t_emp。

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # 主键id 属性对应于表的字段 
    name: Mapped[str] = mapped_column(String(50), nullable=False, name='emp_name', comment="员工姓名")  # 员工姓名 不允许为空 (nullable=False)
    
    # 当你从数据库读取 DECIMAL 字段时，SQLAlchemy 会自动将其转换为 Python 的 Decimal 对象：
    sal: Mapped[Decimal] = mapped_column(DECIMAL(10, 2), nullable=False, comment="员工薪资")  # 员工薪资 不允许为空 (nullable=False) DECIMAL(10, 2) 表示该字段最多有10位数字，其中2位是小数。
    bonus: Mapped[int] = mapped_column(default=0, nullable=False, comment="员工奖金")  # 员工奖金 不允许为空 (nullable=False)
    is_leave: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, comment="是否离职")  # 是否离职 不允许为空 (nullable=False)

    gender: Mapped[SexValues] 
    # 入职时间
    entry_date: Mapped[date] = mapped_column(insert_default=func.now(), nullable=False, comment='入职时间')

    
# if __name__ == '__main__':
#     # 创建所有的表结构
#     Base.metadata.create_all(engine)      #  Base.metadata 包含所有继承自 Base 的模型类（如 Employee）的表结构定义。
#     # mployee.__table__.create(engine, checkfirst=True)  # Employee.__table__ 访问 Employee 模型类对应的表对象。 create 方法用于在数据库中创建该表。