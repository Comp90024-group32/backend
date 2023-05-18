import couchdb

# 创建连接对象
server = couchdb.Server('http://localhost:5984/')

# 连接到数据库
db = server['mydatabase']
results = db.view('_all_docs', include_docs=True, key='John')
for row in results:
    print(row['doc'])