import web

db_host = 'thzz882efnak0xod.cbetxkdyhwsb.us-east-1.rds.amazonaws.com	'
db_name = 'c2buiuqoxcowv0sz'
db_user = 'zao0bi9cjgnbn459'
db_pw = 'chlzfkwhzjrmvrovi1ay'
port = '3306'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    port='3306'
    )