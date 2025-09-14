from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
import re
# 分支路由
ch02 = APIRouter(
    prefix="/ch02", tags=["请求体传参"]
)

class Addr(BaseModel):
    """
    地址的模型类
    """
    province: str = Field(..., description="省份")
    city: str = Field(..., description="城市")
    street: str = Field(..., description="街道")

class Emp(BaseModel):
    """
    员工请求参数的模型类
    """
    name: str = Field(description="员工的名字")
    age: int = Field(gt=0, lt=150, description="员工的年龄，必须大于0小于150")
    birthday: str = Field(description="员工的出生日期，格式：yyyy-MM-dd")
    addr: Addr = Field(description="员工的地址信息")
    desc: str | None = Field(None, description="员工的描述信息")

    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        """验证名字格式：必须以小写字母或下划线开头，后跟2-20个字母数字下划线"""
        pattern = r'^[a-z_]\w{2,20}$'
        if not re.match(pattern, value):
            raise ValueError('名字格式不正确：必须以小写字母或下划线开头，长度3-21个字符，只能包含字母数字下划线')
        return value



@ch02.post("/emp/", tags=["请求体传参"], description="请求体传参的接口", response_description="请求体传参的响应描述", summary="创建员工信息")
def create_emp(emp: Emp):
    """
    创建员工信息
    :param emp: 员工信息
    :return: 员工信息
    """
    print(f"员工信息：{emp}")
    return emp