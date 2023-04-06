import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bert import my_bert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,BLOB
from sqlalchemy.orm import sessionmaker
from pre import split_sentences

# 配置信息
host = '47.104.244.100'
port = 3306
password = 'root'
username = 'root'
database = '401_db'
my_url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

# 连接
engine = create_engine(my_url)
connection = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

#创建对象的基类：
Base = declarative_base()

#定义User对象：
class User(Base):
    #表的名字：
    __tablename__ = 'isimple'

    #表的结构:
    id = Column(Integer,primary_key=True)
    my_string = Column(String(20))
    my_number = Column(BLOB)

# 调用模型
all_level = []
all_sentences = ''' 徐静长的真好看。早安！今天天气真好，早饭吃什么？我买了一支新钢笔，它有金色的笔杆，黑色的笔尖，写起字来非常流畅。我非常喜欢它，每天都会用它写字。'''

sentecnes = split_sentences(all_sentences)
for sentence in sentecnes:
    level = my_bert(sentence=sentence)
    all_level.append(level)
    print(level)

# 插入数据
data_list = User(my_string=all_sentences, my_number=all_level)
session.add(data_list)

# 提交
session.commit()

# 关闭当前会话中的所有连接
session.close()

# 关闭整个引擎中的所有连接池
engine.dispose()

print("Done!!!")