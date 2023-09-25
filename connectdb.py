# CONNECT TO DB
import sqlite3

conn = sqlite3.connect("datauser.sqlite",check_same_thread=False)