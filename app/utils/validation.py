class InvalidRequestError(ValueError):
    pass

def validate_message_request(data):
    required_fields = ["user_id", "message", "msg_id"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        missing_fields_str = ", ".join(missing_fields)
        raise InvalidRequestError(f"Missing required fields: {missing_fields_str}")

    if not isinstance(data['user_id'], str):
        raise InvalidRequestError("The 'user_id' field must be a string.")

    if not isinstance(data['message'], str):
        raise InvalidRequestError("The 'message' field must be a string.")

    if not isinstance(data['msg_id'], str):
        raise InvalidRequestError("The 'msg_id' field must be a string.")
