import sqlite3
# with sqlite3.connect('instance\\test.db') as conexao:
#     cursor = conexao.cursor()
#     felipe = cursor.execute("SELECT * FROM user WHERE id=1")
#     user_data = felipe.fetchone()
#     print(user_data[1], user_data[2])


nome = "Jorge"
senha = "111"
with sqlite3.connect('instance\\test.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM user WHERE username = ? \
                    AND password = ?", (nome, senha))
    user_data = cursor.fetchone()
    print(user_data)
