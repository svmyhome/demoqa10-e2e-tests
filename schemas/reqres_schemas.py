list_users = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "avatar": {"type": "string"},
                },
                "additionalProperties": False,
                "required": ["id", "email", "first_name", "last_name", "avatar"],
            },
            "additionalItems": False,
        },
        "support": {
            "type": "object",
            "properties": {"url": {"type": "string"}, "text": {"type": "string"}},
            "additionalProperties": False,
            "required": ["url", "text"],
        },
    },
    "additionalProperties": False,
    "required": ["page", "per_page", "total", "total_pages", "data", "support"],
}

create_user = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
    },
    "additionalProperties": False,
    "required": ["name", "job", "id", "createdAt"],
}

update_user = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "additionalProperties": False,
    "required": ["name", "job", "updatedAt"],
}

update_user_patch = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job1": {"type": "string"},
        "updatedAt": {"type": "string"},
    },
    "additionalProperties": False,
    "required": ["name", "job1", "updatedAt"],
}

user_not_found = {"type": "object", "additionalProperties": False}

register_user_fail = {
    "type": "object",
    "properties": {"error": {"type": "string"}},
    "additionalProperties": False,
    "required": ["error"],
}
