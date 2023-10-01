from db_config import Message


# インスタンスを作成してから実行
def craete_message():
    message = Message(user="Bob", content="my name is Bob!!")
    message.save()
    # インスタンスを作成しないでcreate
    Message.create(user="Tom", content="Hello Bob!")


if __name__ == "__main__":
    craete_message()
