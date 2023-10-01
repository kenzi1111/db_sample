from db_config import Message


def display_all_message():
    messages = Message.select().where(Message.user == "Bob")

    for message in messages:
        print(message.id, message.user, message.content, message.pub_date)


if __name__ == "__main__":
    display_all_message()
