from db_config import Message

def display_all_message():
    messages = Message.select()

    for message in messages:
        print(message.id, message.user, message.content, message.pub_date)

def update_message(id):
    msg = Message.get_by_id(id)
    msg.user = "Bob Dylan"
    msg.save()

if __name__ == "__main__":
    display_all_message()

    id = 2
    update_message(id)
    display_all_message()