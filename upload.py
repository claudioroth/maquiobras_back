
# #df = pd.read_excel("Lista de precios Maquiobras 4-4-24.xlsm")

# #engine = create_engine("mysql+pymysql://root:root@localhost:8889/maquiobrasdb")


# # coding: utf-8

# # In[1]:


# import pymysql
# import pandas as pd
# import os

# # In[2]:


# database = pymysql.connect (host="localhost" , port=8889 , user="root" , passwd="root" ,db="maquiobrasdb")
# cursor = database.cursor()


# # In[3]:


# #product_details_table = ("CREATE TABLE IF NOT EXISTS product_details(id int,product_id varchar(255) NOT NULL,product_name text,product_price varchar(255),product_rating BLOB,product_star_rating float,product_url LONGTEXT, PRIMARY KEY (product_id))")

# product_details_table = (
#     "CREATE TABLE IF NOT EXISTS product_details "
#     "(id int, "
#     "prov_nro varchar (50), "
#     "sales varchar (255), "
#     "product_name text, "
#     "product_price varchar(255), "
#     "product_rating BLOB, "
#     "product_star_rating float)")

# # In[4]:


# cursor.execute(product_details_table)


# # In[5]:


# #read excel_sheet


# # In[6]:


# #excel_sheet = xlrd.open_workbook('Lista de precios Maquiobras 4-4-24.xlsm')
# #excel_sheet

# df1 = pd.read_excel(os.path.join("Lista de precios Maquiobras 4-4-24.xlsm"),engine='openpyxl')

# # In[7]:


# #sheet_name = excel_sheet.sheet_names()
# #sheet_name


# # In[8]:


# insert_query = "INSERT INTO product_details (id,prov_nro,sales,product_name,product_price,product_rating,product_star_rating ) VALUES (%s,%s,%s,%s,%s,%s,%s)"


# # In[9]:


# for sh in range(0,len(df1)):
#     sheet= df1.sheet_by_index(sh)
    
#     for r in range(1,sheet.nrows):
#         id = sheet.cell(r,0).value

#         prov_nro = sheet.cell(r,1).value

#         sales = sheet.cell(r,2).value
     
#         product_name = sheet.cell(r,3).value
      
#         product_price = sheet.cell(r,4).value
        
#         product_rating = sheet.cell(r,5).value
        
#         product_star_rating = sheet.cel(r,6).value
        
#         product_details_value = (id, prov_nro,sales,product_name,product_price,product_rating,product_star_rating)
        
        
#         cursor.execute(insert_query,product_details_value)
#         database.commit()


import pandas as pd
from sqlalchemy import create_engine, text


#df = pd.read_excel("Lista de precios Maquiobras 4-4-24.xlsm")
df = pd.read_excel("Lista2.xlsm")
df.index += 1
#engine = create_engine("mysql+pymysql://root:root@localhost:3306/maquiobrasdb")
engine = create_engine("mysql+pymysql://root:@localhost:3306/maquiobrasdb")
#engine = create_engine("mysql+pymysql://root:Char#123@localhost:3306/maquiobrasdb")
df.to_sql("product_detail", con=engine)

connection = engine.connect()
qry = text("ALTER TABLE `product_detail` CHANGE `index` `index` BIGINT(20) NOT NULL AUTO_INCREMENT, add PRIMARY KEY (`index`)")
connection.execute(qry)




#SE CORRE APENAS SE GENERA LA TABLA CON PYTHON
#ALTER TABLE `product_detail` CHANGE `IMPORTE S/IVA` `IMPORTE S/IVA` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `C/IVA 10.5%` `C/IVA 10.5%` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `OFERTA SIN IVA` `OFERTA SIN IVA` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `OFERTA COSTO` `OFERTA COSTO` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `COSTO MAS BAJO` `COSTO MAS BAJO` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `RENTAB.` `RENTAB.` TEXT NULL DEFAULT NULL;
#ALTER TABLE `product_detail` CHANGE `ULT.MODIF.` `ULT.MODIF.` DATETIME NULL DEFAULT NULL;
#ALTER TABLE `product_detail` ADD `STOCK` DOUBLE NULL DEFAULT NULL AFTER `RENTAB.`;
#ALTER TABLE `product_detail` ADD `SUC1` DOUBLE NULL DEFAULT NULL AFTER `STOCK`;
#ALTER TABLE `product_detail` ADD `SUC2` DOUBLE NULL DEFAULT NULL AFTER `SUC1`;
#ALTER TABLE `product_detail` ADD `DEPO` DOUBLE NULL DEFAULT NULL AFTER `SUC2`;


#SE ARREGLA LUEGO VALORES EN NULL Y *
#UPDATE `product_detail` SET `C/IVA 21%`=0 WHERE `C/IVA 21%` is NULL;
#UPDATE `product_detail` SET `C/IVA 21%`=0 WHERE `C/IVA 21%`='*';

#UPDATE `product_detail` SET `C/IVA 10.5%`=0 WHERE `C/IVA 10.5%` is NULL;
#UPDATE `product_detail` SET `C/IVA 10.5%`=0 WHERE `C/IVA 10.5%`='*';

#UPDATE `product_detail` SET `OFERTA COSTO`=0 WHERE `OFERTA COSTO` is NULL;
#UPDATE `product_detail` SET `OFERTA COSTO`=0 WHERE `OFERTA COSTO`='*';


#UPDATE `product_detail` SET `STOCK`=0 WHERE `STOCK` is NULL;
#UPDATE `product_detail` SET `SUC1`=0 WHERE `SUC1` is NULL;
#UPDATE `product_detail` SET `SUC2`=0 WHERE `SUC2` is NULL;
#UPDATE `product_detail` SET `DEPO`=0 WHERE `DEPO` is NULL;


#ALTER TABLE `control` ADD `destino` VARCHAR(50) NULL DEFAULT NULL AFTER `local`;

#ALTER TABLE `users` ADD `sucursal` INT(11) NULL DEFAULT NULL AFTER `fecha`;