from decimal import Decimal
import enum
import sys
import os
# 将当前脚本所在目录的上一级目录添加到 Python 的模块搜索路径中。
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from datetime import date
from sqlalchemy.orm import sessionmaker
from regex import E, F
from sqlalchemy import DECIMAL, Boolean, String
from sqlalchemy.orm import Mapped, mapped_column
from db_main import Base
from db_main import engine
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

    # 需要在Employee模型类中增加一个__str__函数 用于打印员工信息
    def __str__(self):
        return f'姓名：{self.name},性别：{self.gender.value},薪资：{self.sal},入职时间：{self.entry_date},津贴：{self.bonus},是否离职： {self.is_leave}'

    
if __name__ == '__main__':

    
#     # 创建所有的表结构
#     Base.metadata.create_all(engine)      #  Base.metadata 包含所有继承自 Base 的模型类（如 Employee）的表结构定义。
#     # mployee.__table__.create(engine, checkfirst=True)  # Employee.__table__ 访问 Employee 模型类对应的表对象。 create 方法用于在数据库中创建该表。
    '''
    session用于创建程序和数据库之间的会话，所有对象的载入和保存都需通过session对象 。在Web项目中，一个请求共用一个session对象。
    '''
    with sessionmaker(engine).begin() as session:
        # 新增数据
        emp1 = Employee(
            name="张三",
            sal=Decimal('5000.00'),  # ✅ 正确
            bonus=500,
            is_leave=False,
            gender=SexValues.MALE,
            entry_date=date(2023, 1, 1)
        )
        emp2 = Employee(
            name="李四",
            sal=Decimal('6000.00'),  # ✅ 正确
            bonus=600,
            is_leave=False,
            gender=SexValues.FEMALE,
            entry_date=date(2023, 3, 2)
        )
        emp3 = Employee(
            name="王五",
            sal=Decimal('7000.00'),  # ✅ 正确
            bonus=700,
            is_leave=True,
            gender=SexValues.MALE,
            entry_date=date(2023, 5, 15)
        )
        # session.add(emp1)  # 将新创建的 Employee 对象添加到当前的数据库会话中。
        session.add_all([emp1, emp2, emp3])  # 批量添加

        # 先删除可能存在的错误数据
        # session.query(Employee).delete()
        
        
        # 查询数据（在同一个事务中）
        emp = session.get(Employee, 1)  # 根据主键查询
        print(emp)