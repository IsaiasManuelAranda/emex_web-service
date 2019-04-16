import web

db_host = 'w29ifufy55ljjmzq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'o6r07j748r3suvwt'
db_user = 'boy7mvc3jdw8ywki'
db_pw = 'jwz8ekcf8w1o8a9w'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )