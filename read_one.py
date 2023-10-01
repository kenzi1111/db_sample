from db_config import Message

if __name__ == "__main__":
    # 複数のデータの先頭の一件を取得
    msg1 = Message.select().get()
    print(msg1.user, msg1.content)

    # primary_keyで指定して取得
    msg2 = Message.get_by_id(4)
    print(msg2.user, msg2.content)
