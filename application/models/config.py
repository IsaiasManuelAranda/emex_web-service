import web

db_host = 'w29ifufy55ljjmzq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'ct0tol61e74dzche'
db_user = 'w2oy7rp28n6wt8f5'
db_pw = 'iu29b88f8o085yu0'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )