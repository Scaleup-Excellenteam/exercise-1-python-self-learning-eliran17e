"""
This module provides a Post Office class that allows users to message each other.
"""
class PostOffice:
    """A Post Office class. Allows users to message each other.
    Args:
        usernames (list): Users for which we should create PO Boxes.
    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, title, message_body, urgent=False):
        """Send a message to a recipient.
        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            title (str): The title of the message.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.
        Returns:
            int: The message ID, auto incremented number.
        Raises:
            KeyError: If the recipient does not exist.
        """
        if recipient not in self.boxes:
            raise KeyError(f"User '{recipient}' does not exist.")

        user_box = self.boxes[recipient]
        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'unread': True,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_messages=None):
        """Read messages from the user's inbox.
        Args:
            username (str): The username of the recipient.
            num_messages (int, optional): The number of messages to read. Defaults to None.
        Returns:
            list: The list of messages read.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")

        user_box = self.boxes[username]
        if num_messages is None:
            num_messages = len(user_box)

        messages_to_read = user_box[:num_messages]
        for message in messages_to_read:
            message['unread'] = False
        return messages_to_read

    def search_inbox(self, username, search_string):
        """Search for messages containing the search string in the user's inbox.
        Args:
            username (str): The username of the recipient.
            search_string (str): The string to search for in the messages.
        Returns:
            list: The list of messages containing the search string.
        """
        if username not in self.boxes:
            raise KeyError(f"User '{username}' does not exist.")
        search_string = search_string.lower()
        user_box = self.boxes[username]
        result = []
        for message in user_box:
            if search_string in message['title'].lower() or search_string in message['body'].lower():
                result.append(message)
        return result
