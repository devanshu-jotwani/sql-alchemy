import sqlalchemy as db

engine = db.create_engine("mysql://root:abc456@localhost/21dec21",echo = True)
connection=engine.connect()
metadata=db.MetaData()
employee=db.Table('employee',metadata,autoload=True,autoload_with=engine)
'''
#printing column names
print(employee.columns.keys())
#printing meta data
print("-------------------")
print(repr(metadata.tables['employee']))
print("-------------------")
'''
#Equivalent to 'SELECT * FROM employee'
query = db.select([employee])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print("Query- Select * from employee")
print("Resul of select Query \n",ResultSet[:])

print("--------------------")

#Where Query
query=db.select([employee.columns.name,employee.columns.salary]).where(employee.columns.salary<25000)
whereQuery=connection.execute(query)
result=whereQuery.fetchall()
print("Query- select name,salary from employee where salary<25000")
print("Result of Where Query \n",result[:])
print("--------------------")

#In Query
query=db.select([employee.columns.id,employee.columns.name,employee.columns.salary]).where(employee.columns.salary.in_([20000,25000]))
inQuery=connection.execute(query)
result=inQuery.fetchall()

print("Query select id,name,salary from employee where salary in(20000,25000)")
print("Result of IN Query",result[:])
print("--------------------")
#Order by Query
query=db.select([employee]).order_by(db.desc(employee.columns.salary))
orderBy=connection.execute(query)
result=orderBy.fetchall()
print("Query- select * from employee order by salary")
print("Result of Order By Query \n", result)
