import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="####",
    user="####",
    password="####",
    database="fruits_and_vegetables"
)

MyCur = mydb.cursor()

# # первый sql запрос
# calories_limit = 50
# sql = f"""SELECT * FROM fruits_and_vegetables WHERE type = 'овощ' AND calories < {calories_limit}"""
# MyCur.execute(sql)
#
# result = MyCur.fetchall()
# for element in result:
#     print(element)
#
#
# # второй sql запрос
# calories_lower_limit = 30
# calories_upper_limit = 100
# sql = f"""SELECT * FROM fruits_and_vegetables WHERE type = 'фрукт' AND calories BETWEEN {calories_lower_limit} AND {calories_upper_limit}"""
# MyCur.execute(sql)
#
#
# result = MyCur.fetchall()
# for element in result:
#     print(element)
#
#
# # третий sql запрос
# MyCur = mydb.cursor()
# search_word = "морковь да короче"
# sql = f"""SELECT * FROM fruits_and_vegetables WHERE description LIKE '%{search_word}'"""
# MyCur.execute(sql)
#
# result = MyCur.fetchall()
# for element in result:
#     print(element)
#
#
# # четвертый sql запрос
# MyCur = mydb.cursor()
# sql = f"""SELECT * FROM fruits_and_vegetables WHERE color IN ('желтый', 'красный')"""
# MyCur.execute(sql)
# result = MyCur.fetchall()
# for element in result:
#     print(element)


# 2


# # 1 sql запрос
# sql = """SELECT COUNT(*) FROM fruits_and_vegetables WHERE type = 'овощ'"""
# MyCur.execute(sql)
# result = MyCur.fetchall()
# print("Количество овощей:", result[0])
#
#
# # 2 sql запрос
# sql = """SELECT COUNT(*) FROM fruits_and_vegetables WHERE type = 'фрукт'"""
# MyCur.execute(sql)
# result = MyCur.fetchall()
# print("Количество фруктов:", result[0])
#
#
# # 3 sql запрос
# color = 'красный'
# sql = f"""SELECT COUNT(*) FROM fruits_and_vegetables WHERE color = '{color}'"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print(f"Количество овощей и фруктов цвета '{color}':", result[0])
#
#
# # 4 sql запрос
# sql = """SELECT color, COUNT(*) FROM fruits_and_vegetables GROUP BY color"""
# MyCur.execute(sql)
# result = MyCur.fetchall()
# for row in result:
#     print(f"Количество овощей и фруктов цвета '{row[0]}': {row[1]}")
#
#
# # 5 sql
# sql = """SELECT color, COUNT(*) AS total_count FROM fruits_and_vegetables GROUP BY color ORDER BY total_count ASC LIMIT 1"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print(f"Цвет с минимальным количеством овощей и фруктов: {result[0]}")
#
#
# # 6 sql
# sql = """SELECT color, COUNT(*) AS total_count FROM fruits_and_vegetables GROUP BY color ORDER by total_count DESC LIMIT 1"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print(f"Цвет с максимальным количеством овощей и фруктов: {result[0]}")
#
#
# # 7 sql
# sql = """SELECT MIN(calories) FROM fruits_and_vegetables"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print("Минимальный калорийность овощей и фруктов:", result[0])
#
#
# # 8 sql
# sql = """SELECT MAX(calories) FROM fruits_and_vegetables"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print("Максимальная калорийность овощей и фруктов:", result[0])
#
#
# # 9 sql
# sql = """SELECT AVG(calories) FROM fruits_and_vegetables"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print("Средняя калорийность оповщей и фруктов:", result[0])
#
#
# # 10 sql
# sql = """SELECT name FROM fruits_and_vegetables WHERE type = 'фрукт' ORDER BY calories ASC LIMIT 1"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print(f"Фрукт с минимальной калорийностью:", {result[0]})
#
#
# # 11 sql
# sql = """SELECT name FROM fruits_and_vegetables WHERE type = 'фрукт' ORDER BY calories DESC LIMIT 1"""
# MyCur.execute(sql)
# result = MyCur.fetchone()
# print(f"Фрукт с максимальной калорийностью: {result[0]}")

MyCur.close()
mydb.commit()
mydb.close()