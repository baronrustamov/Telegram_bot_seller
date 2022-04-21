import sqlite3
from sqlite_db import UserDB as user

base = sqlite3.connect("Files.db")
cur = base.cursor()

# get_commands-------


def get_balans(id):
    cur.execute('SELECT money FROM users WHERE user_id=?', (id,))
    for i in cur.fetchone():
        return i


def get_all_money(id):
    cur.execute('SELECT all_money FROM users WHERE user_id=?', (id,))
    for i in cur.fetchone():
        return i


def get_purchased(id):
    cur.execute('SELECT purchased FROM users WHERE user_id=?', (id,))
    for i in cur.fetchone():
        return i


def get_referal(id):
    cur.execute('SELECT refer FROM users WHERE user_id=?', (id,))
    for i in cur.fetchone():
        return i


def add_referal(id_user, id_dad):
    if(user.bool_check_id(id_user) == False):
        cur.execute('UPDATE users SET refer=? WHERE user_id=?',
                    (get_referal(id_dad)+1, id_dad))
        base.commit()
# -----------------------------


def add_purchased(id):
    cur.execute('UPDATE users SET purchased=? WHERE user_id=?',
                (get_purchased(id)+1, id))
    base.commit()


def add_allmoney(id, money):
    cur.execute('UPDATE users SET all_money=? WHERE user_id=?',
                (get_all_money(id) + money, id))
    base.commit()


def add_money(id, money):
    cur.execute('UPDATE users SET money=? WHERE user_id=?',
                (get_balans(id) + money, id))
    add_allmoney(id, money)
    base.commit()


def minus_money(id, money):
    cur.execute('UPDATE users SET money=? WHERE user_id=?',
                (get_balans(id) - money, id))
    base.commit()

# ------------------------------------------


def get_file(id):
    cur.execute('SELECT file_id FROM file_v2 WHERE card_name=?',
                (user.get_last_girl(id),))
    for i in cur.fetchone():
        return i