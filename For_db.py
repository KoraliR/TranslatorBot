import os.path
import sqlite3, datetime as dt
DB_FILE_NAME = "maindb.db"



def add_user(tg_id, user_name, PATH):
    command = f"SELECT tg_id FROM Users WHERE tg_id = {tg_id}"
    con = sqlite3.connect(os.path.join(PATH, DB_FILE_NAME))
    cur = con.cursor()
    result = cur.execute(command).fetchall()
    if result == []:
        last_id = int(cur.execute("SELECT ID FROM Users").fetchall()[-1][0])
        command = f"INSERT INTO Users(tg_id, username, first_start, ID) VALUES({tg_id}, '{user_name}', '{dt.datetime.now().strftime('%Y.%m.%d %H:%M:%S')}', {last_id + 1})"
        cur.execute(command)
        con.commit()
        con.close()
        return f"OK {last_id + 1}"
    else:
        id_for_usr = cur.execute(f'SELECT ID FROM Users WHERE tg_id = {tg_id}').fetchone()[0]
        con.commit()
        con.close()
        print(id_for_usr)
        return f"ALR {id_for_usr}"

def add_counter_repeat(ID, counter, PATH, flag):
    con = sqlite3.connect(os.path.join(PATH, DB_FILE_NAME))
    cur = con.cursor()
    if flag == "ALR":
        command = f"UPDATE Info SET wordsPerDay = {counter} WHERE ID = {ID}"
    elif flag == "OK":
        command = f"INSERT INTO Info(ID, wordsPerDay, words) VALUES({ID}, {counter}, 0)"
    print(counter, ID)
    cur.execute(command)
    con.commit()
    con.close()