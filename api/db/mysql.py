from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import logging

def query_exec(mysql ,query, params=None, fetch=None, autoclose=True, assoc=None):
    try:
        cur = mysql.connection.cursor()
    except Exception:
        print("MySQL connexion Error")
        raise
    else:
        print("connection successful")
        try:
            result = cur.execute(query, params)
            print("Executed Query: {}".format(cur._executed))
        except Exception:
            cur.close()
            raise
        else:
            mysql.connection.commit()
            if fetch == 'all':
                result = cur.fetchall()
            elif fetch == 'one':
                result = cur.fetchone()
            elif fetch == 'lastid':
                result = cur.lastrowid
        if autoclose:
            cur.close()
        return result

def fetchone(mysql, query, params=None):
    return query_exec(mysql, query, params, fetch='one')

def fetchall(mysql, query, params=None, assoc=False):
    return query_exec(mysql, query, params, fetch='all')


