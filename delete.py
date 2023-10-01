from db_config import Message


def delet_message(id):
    message = Message.get_by_id(id)
    message.delete_instance()


if __name__ == "__main__":
    id = 3
    delet_message(id)
